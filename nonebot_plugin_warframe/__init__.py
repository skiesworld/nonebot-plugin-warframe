from nonebot import on_command
from nonebot.internal.adapter import Message
from nonebot.params import CommandArg

from .data_source import chose_way, get_alerts

warframe = on_command("warframe", aliases={"星际战甲", "wf"}, priority=5)


@warframe.handle()
async def receive(args: Message = CommandArg()):
    msg = await chose_way(args.extract_plain_text())
    await warframe.finish(message=msg)
