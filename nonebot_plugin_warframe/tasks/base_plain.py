from abc import ABC, abstractmethod
from datetime import datetime

from nonebot import logger


class PlainsBase(ABC):
    """抽象基类，定义平原共有的属性和方法"""

    def __init__(self, name: str):
        self.name = name
        self.status = None

    @abstractmethod
    async def initialize_cycle(self, *args, **kwargs):
        pass

    @abstractmethod
    async def switch_cycle(self, *args, **kwargs):
        pass

    @abstractmethod
    async def notify_users(self):
        pass

    def log_status_change(
        self,
        current_status: str,
        next_status: str,
        remaining_time: int,
        switch_time: int,
    ):
        """记录状态切换的日志信息


        :param current_status: 当前状态
        :param next_status: 下一个状态
        :param remaining_time: 剩余时间（秒）
        :param switch_time: 状态切换的时间戳
        """
        switch_time_str = datetime.fromtimestamp(switch_time).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        logger.info(
            f"{self.name} | 状态交替\n"
            f"当前状态: {current_status}\n"
            f"下一个状态: {next_status}\n"
            f"剩余时间: {remaining_time} 秒\n"
            f"交替时间: {switch_time_str}"
        )

    def log_notification(self, current_status: str, next_status: str, switch_time: int):
        """记录通知的日志信息


        :param current_status: 当前状态
        :param next_status: 下一个状态
        :param switch_time: 状态切换的时间戳
        """
        switch_time_str = datetime.fromtimestamp(switch_time).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        logger.info(
            f"{self.name} | 状态切换通知\n"
            f"当前状态: {current_status}\n"
            f"下一个状态: {next_status}\n"
            f"交替时间: {switch_time_str}"
        )
