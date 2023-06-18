from nonebot import on_command
from nonebot.plugin import PluginMetadata
from nonebot.internal.adapter import Message
from nonebot.params import CommandArg

from .data_source import chose_way, get_alerts

__plugin_meta__ = PluginMetadata(
    name="星际战甲事件查询",
    description="通过奥迪斯网站API查询星际战甲国服事件",
    usage="wf菜单",
    type="application",
    homepage="https://github.com/17TheWord/nonebot-plugin-warframe"
)

warframe = on_command("warframe", aliases={"星际战甲", "wf"}, priority=5)


@warframe.handle()
async def receive(args: Message = CommandArg()):
    msg = await chose_way(args.extract_plain_text())
    await warframe.finish(message=msg)
