from nonebot import on_command
from nonebot.matcher import Matcher

from nonebot_plugin_warframe.models import Alert

from .api import API

api = API()

alert_command = on_command("警报", priority=5)


@alert_command.handle()
async def handle_alert(matcher: Matcher):
    result: list[Alert] = await api.get_alerts()

    message = "\n".join(map(str, result)) if result else "当前没有警报"
    await matcher.finish(message)


news_command = on_command("新闻", priority=5)


@news_command.handle()
async def handle_news(matcher: Matcher):
    result = await api.get_news()
    formatted_result = (
        "\n".join(map(str, result)) if isinstance(result, list) else str(result)
    )
    await matcher.finish(formatted_result)


cetus_command = on_command("夜灵平原", aliases={"赛特斯", "希图斯"}, priority=5)


@cetus_command.handle()
async def handle_cetus(matcher: Matcher):
    result = await api.get_cetus()
    await matcher.finish(str(result))


earth_command = on_command("地球", priority=5)


@earth_command.handle()
async def handle_earth(matcher: Matcher):
    result = await api.get_earth()
    await matcher.finish(str(result))


solaris_command = on_command("索拉里斯", aliases={"金星"}, priority=5)


@solaris_command.handle()
async def handle_solaris(matcher: Matcher):
    result = await api.get_solaris()
    await matcher.finish(str(result))


fissures_command = on_command("虚空裂隙", aliases={"裂隙"}, priority=5)


@fissures_command.handle()
async def handle_fissures(matcher: Matcher):
    result = await api.get_fissures()
    formatted_result = (
        "\n".join(map(str, result)) if isinstance(result, list) else str(result)
    )
    await matcher.finish(formatted_result)


void_trader_command = on_command("虚空商人", aliases={"奸商"}, priority=5)


@void_trader_command.handle()
async def handle_void_trader(matcher: Matcher):
    result = await api.get_voidTrader()
    formatted_result = str(result)
    await matcher.finish(formatted_result)


sortie_command = on_command("突击", priority=5)


@sortie_command.handle()
async def handle_sortie(matcher: Matcher):
    result = await api.get_sortie()
    formatted_result = str(result)
    await matcher.finish(formatted_result)


daily_deals_command = on_command("每日优惠", priority=5)


@daily_deals_command.handle()
async def handle_daily_deals(matcher: Matcher):
    result = await api.get_dailyDeals()
    formatted_result = (
        "\n".join(map(str, result)) if isinstance(result, list) else str(result)
    )
    await matcher.finish(formatted_result)


invasions_command = on_command("入侵", priority=5)


@invasions_command.handle()
async def handle_invasions(matcher: Matcher):
    result = await api.get_invasions()
    formatted_result = (
        "\n".join(map(str, result)) if isinstance(result, list) else str(result)
    )
    await matcher.finish(formatted_result)


events_command = on_command("事件", priority=5)


@events_command.handle()
async def handle_events(matcher: Matcher):
    result = await api.get_events()
    formatted_result = (
        "\n".join(map(str, result)) if isinstance(result, list) else str(result)
    )
    await matcher.finish(formatted_result)


season_command = on_command("午夜电波", aliases={"电波", "章节"}, priority=5)


@season_command.handle()
async def handle_season(matcher: Matcher):
    result = await api.get_season()
    formatted_result = str(result)
    await matcher.finish(formatted_result)
