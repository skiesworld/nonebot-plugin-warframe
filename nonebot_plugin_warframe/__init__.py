from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="星际战甲事件查询",
    description="查询星际战甲国服世界状态：警报/裂隙/突击/赏金等（赏金请用 地球赏金/金星赏金/火卫二赏金）",
    usage="发送：警报 / 裂隙 / 地球赏金 / 金星赏金 / 火卫二赏金 / 菜单",
    type="application",
    homepage="https://github.com/17TheWord/nonebot-plugin-warframe",
)

from . import command as command
from . import tasks as tasks
