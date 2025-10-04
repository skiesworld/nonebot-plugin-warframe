from nonebot import get_driver

from .cetus import CetusPlains


@get_driver().on_startup
async def startup_event():
    cetus = CetusPlains()
    # await cetus.initialize_cycle(
    # day_duration=10, night_duration=5, skip_api=True, notify_offset=2
    # )
    await cetus.initialize_cycle()
