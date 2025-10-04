from datetime import datetime, timedelta
import time

from apscheduler.triggers.interval import IntervalTrigger
from nonebot import logger
from nonebot_plugin_apscheduler import scheduler

from nonebot_plugin_warframe.api import API
from nonebot_plugin_warframe.models import Cetus

from .base_plain import PlainsBase


class CetusPlains(PlainsBase):
    """夜灵平原类，管理昼夜交替逻辑"""

    def __init__(self):
        super().__init__("夜灵平原")
        self.api = API()

    async def initialize_cycle(
        self,
        day_duration: int = 100 * 60,
        night_duration: int = 50 * 60,
        skip_api: bool = False,
        notify_offset: int = 10 * 60,
    ):
        """初始化昼夜交替状态"""
        if skip_api:
            self.status = Cetus(
                oid="test",
                activation=int(time.time()),
                expiry=int(time.time()) + day_duration,
                day=True,
                cetusTime=0,
            )
            logger.info("跳过 API 请求，直接初始化为白天状态")
            remaining_time = day_duration
        else:
            now = int(time.time())
            result = await self.api.get_cetus()
            self.status = result
            remaining_time = result.expiry - now

            scheduler.add_job(
                self.periodic_fetch, IntervalTrigger(hours=1), id="periodic_fetch"
            )

        scheduler.add_job(
            self.switch_cycle,
            "date",
            run_date=datetime.now() + timedelta(seconds=remaining_time),
            id="cetus_cycle_switch",
            kwargs={
                "day_duration": day_duration,
                "night_duration": night_duration,
                "notify_offset": notify_offset,
            },
        )

        notify_time = remaining_time - notify_offset
        if notify_time > 0:
            scheduler.add_job(
                self.notify_users,
                "date",
                run_date=datetime.now() + timedelta(seconds=notify_time),
                id="cetus_notify",
            )

        expiry_time = int(time.time()) + remaining_time
        next_status = "黑夜" if self.status.day else "白天"
        self.log_status_change(
            current_status="白天" if self.status.day else "黑夜",
            next_status=next_status,
            remaining_time=remaining_time,
            switch_time=expiry_time,
        )

    async def switch_cycle(
        self,
        day_duration: int = 100 * 60,
        night_duration: int = 50 * 60,
        notify_offset: int = 10 * 60,
    ):
        """切换昼夜状态"""
        if self.status is None:
            logger.error("状态未初始化！")
            return

        self.status.day = not self.status.day

        next_duration = day_duration if self.status.day else night_duration
        self.status.expiry = int(time.time()) + next_duration

        scheduler.add_job(
            self.switch_cycle,
            "date",
            run_date=datetime.now() + timedelta(seconds=next_duration),
            id="cetus_cycle_switch",
            kwargs={
                "day_duration": day_duration,
                "night_duration": night_duration,
                "notify_offset": notify_offset,
            },
        )

        notify_time = next_duration - notify_offset
        if notify_time > 0:
            scheduler.add_job(
                self.notify_users,
                "date",
                run_date=datetime.now() + timedelta(seconds=notify_time),
                id="cetus_notify",
            )

        expiry_time = int(time.time()) + next_duration
        next_status = "黑夜" if self.status.day else "白天"
        self.log_status_change(
            current_status="白天" if self.status.day else "黑夜",
            next_status=next_status,
            remaining_time=next_duration,
            switch_time=expiry_time,
        )

    async def notify_users(self):
        """通知用户集合打夜灵"""
        if self.status is None:
            logger.error("状态未初始化，无法通知用户！")
            return

        next_status = "黑夜" if self.status.day else "白天"
        self.log_notification(
            current_status="白天" if self.status.day else "黑夜",
            next_status=next_status,
            switch_time=self.status.expiry,
        )

    async def periodic_fetch(self):
        """定期请求信息并校准状态"""
        now = int(time.time())
        result = await self.api.get_cetus()

        logger.info(f"定期更新：当前到期时间为 {result.expiry}")

        if (
            self.status is None
            or self.status.expiry != result.expiry
            or self.status.day != result.day
        ):
            logger.warning("检测到状态偏差，正在重新校准...")

            self.status = result
            remaining_time = result.expiry - now

            scheduler.remove_job("cetus_cycle_switch")
            scheduler.remove_job("cetus_notify")

            scheduler.add_job(
                self.switch_cycle,
                "date",
                run_date=datetime.now() + timedelta(seconds=remaining_time),
                id="cetus_cycle_switch",
            )

            notify_time = remaining_time - 10 * 60
            if notify_time > 0:
                scheduler.add_job(
                    self.notify_users,
                    "date",
                    run_date=datetime.now() + timedelta(seconds=notify_time),
                    id="cetus_notify",
                )

            logger.info(
                f"校准完成：当前状态为 {'白天' if self.status.day else '黑夜'}，到期时间为 {self.status.expiry}"
            )
