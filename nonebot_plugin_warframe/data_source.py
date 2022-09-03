import time
import httpx

data = httpx.get("https://api.null00.com/world/ZHCN").json()


async def chose_way(msg: str):
    match msg:
        case "警报":
            return await get_alerts()
        case "新闻":
            return await get_news()
        case "赛特斯":
            return await get_cetus()
        case "地球":
            return await get_earth()
        case "索拉里斯" | "金星":
            return await get_solaris()
        case "赏金":
            return await get_bounties()
        case "裂隙":
            return await get_fissures()
        case "奸商":
            return await get_voidTrader()
        case "突击":
            return await get_sortie()
        case "每日优惠":
            return await get_dailyDeals()
        case "入侵":
            return await get_invasions()
        case "事件":
            return await get_events()
        case "章节":
            return await get_season()
        case "菜单":
            return await menu()


async def menu():
    return f"命令头：wf、warframe、星际战甲" \
           f"\n参数：" \
           f"\n==================" \
           f"\n警报丨入侵丨赏金丨突击丨裂隙" \
           f"\n章节丨地球丨赛特斯丨索拉里斯" \
           f"\n奸商丨事件丨新闻丨每日优惠"


async def get_alerts():
    temp_alerts = "=================="
    for alert in data['alerts']:
        temp_alerts += f"\n{alert['missionType']}丨{alert['faction']} {alert['minEnemyLevel']} ~ {alert['maxEnemyLevel']}" \
                       f"\n奖励：星币 * {alert['credits']}"
        temp_reward = ""
        for alert_reward in alert['rewards']:
            temp_reward += f"\n\t {alert_reward['item']} * {alert_reward['itemCount']}"
        temp_alerts += temp_reward + "\n=================="
    return temp_alerts


async def get_news():
    temp_news = "=================="
    for new in data['news']:
        temp_news += f"\n标题：{new['defaultMessages']}    发布时间：{await get_format_time('%Y-%m-%d %H:%M:%S', await get_difference_time(new['date']))}" \
                     f"\n链接：{new['prop']}" \
                     f"\n=================="
    return temp_news


async def get_cetus():
    temp_cetus = f"==================" \
                 f"\n现在：{'白天' if data['cetus']['day'] else '黑夜'}" \
                 f"\n剩余：{await get_format_time('%H时%M分%S秒', await get_difference_time(data['cetus']['expiry'] - time.time()))}" \
                 f"\n=================="
    return temp_cetus


async def get_earth():
    temp_earth = "==================" \
                 f"\n现在：{'白天' if data['earth']['day'] else '黑夜'}" \
                 f"\n剩余：{await get_format_time('%H时%M分%S秒', await get_difference_time(data['earth']['earthDate'] - int(time.time())))}" \
                 f"\n交替时间：{await get_format_time('%H时%M分%S秒', await get_difference_time(data['earth']['earthDate']))}" \
                 f"\n=================="
    return temp_earth


async def get_solaris():
    state = '温暖'
    if data['solaris']['state'] == 2:
        state = '寒冷'
    elif data['solaris']['state'] == 3:
        state = '极寒'
    return "==================" \
           f"\n现在：{state}" \
           f"\n剩余时间：{await get_format_time('%H时%M分%S秒', await get_difference_time(data['solaris']['solarisExpiry'] - int(time.time())))}" \
           f"\n交替时间：{await get_format_time('%Y-%m-%d %H时%M分%S秒', await get_difference_time(data['solaris']['solarisExpiry']))}" \
           f"\n=================="


async def get_bounties():
    temp_bounty = "=================="
    for bounty in data['bountys']:
        temp_bounty += f"\n平原：{bounty['tag']}   剩余时间：{await get_format_time('%H时%M分%S秒', await get_difference_time(bounty['expiry'] - int(time.time())))}"
        temp_jobs = ""
        for job in bounty['jobs']:
            temp_jobs += f"\n\t{job['jobType']}" \
                         f"\n\t\t奖励：{job['rewards'].replace('<br />', '、')}"
        temp_bounty += temp_jobs + "\n=================="
    return temp_bounty


async def get_fissures():
    temp_fissures = ""
    for fissure in data['fissures']:
        temp_fissures += f"\n{fissure['modifier']}\t丨\t{fissure['missionType']}\t丨\t{fissure['node']}\t丨\t{await get_format_time('%H时%M分%S秒', await get_difference_time(fissure['expiry'] - int(time.time())))}"
    return temp_fissures


async def get_voidTrader():
    return "==================" \
           f"\n{data['voidTrader']['character']}" \
           f"\n地点：{data['voidTrader']['node']}" \
           f"\n剩余：{await get_format_time('%H时%M分%S秒', await get_difference_time(data['voidTrader']['expiry'] - int(time.time())))}" \
           f"\n=================="


async def get_sortie():
    temp_sortie = "==================" \
                  f"\n{data['sortie']['boss']}  {await get_format_time('%H时%M分%S秒', await get_difference_time(data['sortie']['expiry'] - int(time.time())))}" \
                  f"\n派系：{data['sortie']['faction']}"
    for variants in data['sortie']['variants']:
        temp_sortie += f"\n\t{variants['missionType']} \t丨\t{variants['node']}\t丨\t{variants['modifierType']}"
    return temp_sortie


async def get_dailyDeals():
    temp_daily_deals = ""
    for daily_deal in data['dailyDeals']:
        temp_daily_deals += f"{daily_deal['item']}丨{daily_deal['discount']}%折扣丨{daily_deal['salePrice']}白金\n"
    return temp_daily_deals


async def get_invasions():
    temp_invasions = ""
    for invasion in data['invasions']:
        temp_invasions += f"{invasion['node']}  \t丨\t{invasion['locTag']}   \t丨\t"
        if invasion['attacker']['rewards']:
            for attacker_reward in invasion['attacker']['rewards']:
                temp_invasions += f"{attacker_reward['item']}*{attacker_reward['itemCount']}"
            temp_invasions += " / "
        for defender_reward in invasion['defender']['rewards']:
            temp_invasions += f"{defender_reward['item']}*{defender_reward['itemCount']}"
    return temp_invasions


async def get_events():
    temp_event = ""
    for event in data['events']:
        temp_event += f"{event['tag']}\t剩余：{await get_format_time('%H时%M分%S秒', await get_difference_time(event['expiry'] - int(time.time())))}\n"
    return temp_event


async def get_season():
    temp_season = ""
    for challenge in data['season']['challenges']:
        temp_season += f"{challenge['cycle']}\t丨\t{challenge['xp']}xp\t丨\t{challenge['challenge']}\n"
    return temp_season


async def get_format_time(f, t):
    return time.strftime(f, t)


async def get_difference_time(t) -> int:
    return time.gmtime(t)
