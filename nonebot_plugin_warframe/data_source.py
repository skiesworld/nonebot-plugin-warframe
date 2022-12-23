import time
import random
import httpx
import json


# 选择
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
            return await get_bounty()
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


# 菜单
async def menu():
    return f"命令头：wf、warframe、星际战甲" \
           f"\n参数：" \
           f"\n==================" \
           f"\n警报丨入侵丨赏金丨突击丨裂隙" \
           f"\n章节丨地球丨赛特斯丨索拉里斯" \
           f"\n奸商丨事件丨新闻丨每日优惠"


# 警报
async def get_alerts():
    data = await get_data_json("alerts")
    temp_alerts = "=================="
    for alert in data:
        temp_alerts += f"\n{alert['location']}" \
                       f"\n{alert['missionType']}丨{alert['faction']}（{alert['minEnemyLevel']} ~ {alert['maxEnemyLevel']}）" \
                       f"\n奖励丨星币 * {alert['credits']}"
        temp_reward = ""
        for alert_reward in alert['rewards']:
            temp_reward += f"\n\t{alert_reward['item']} * {alert_reward['itemCount']}"
        temp_alerts += temp_reward + "\n=================="
    return temp_alerts


# 新闻
async def get_news():
    data = await get_data_json("news")
    temp_news = "=================="
    for new in data:
        temp_news += f"\n{new['defaultMessages']}" \
                     f"\n时间丨{await get_format_time('%Y-%m-%d %H:%M:%S', await get_gm_time(new['date']))}" \
                     f"\n链接丨{new['prop']}" \
                     f"\n=================="
    return temp_news


# 赛特斯
async def get_cetus():
    data = await get_data_json("cetus")
    day = '白天' if data['day'] else '黑夜'
    temp_cetus = f"==================" \
                 f"\n{day}\t丨\t{await get_format_time('%H时%M分%S秒', await get_gm_time(data['cetusTime'] - time.time()))}" \
                 f"\n交替\t丨\t{await get_format_time('%H时%M分%S秒', await get_local_time(data['cetusTime']))}" \
                 f"\n=================="
    return temp_cetus


# 地球
async def get_earth():
    data = await get_data_json("earth")
    temp_earth = "==================" \
                 f"\n{'白天' if data['day'] else '黑夜'}\t丨\t{await get_format_time('%H时%M分%S秒', await get_gm_time(data['earthDate'] - int(time.time())))}" \
                 f"\n交替\t丨\t{await get_format_time('%H时%M分%S秒', await get_local_time(data['earthDate']))}" \
                 f"\n=================="
    return temp_earth


# 索拉里斯
async def get_solaris():
    data = await get_data_json("solaris")
    state = '温暖'
    if data['state'] == 2:
        state = '寒冷'
    elif data['state'] in [4, 1]:
        state = '极寒'
    return "==================" \
           f"\n{state}\t丨\t{await get_format_time('%H时%M分%S秒', await get_gm_time(data['solarisExpiry'] - int(time.time())))}" \
           f"\n交替\t丨\t{await get_format_time('%H时%M分%S秒', await get_local_time(data['solarisExpiry']))}" \
           f"\n=================="


# 赏金
async def get_bounty():
    data = await get_data_json("bounty")
    temp_bounty = "=================="
    for bounty in data:
        temp_bounty += f"\n{bounty['tag']}   剩余时间：{await get_format_time('%H时%M分%S秒', await get_gm_time(bounty['expiry'] - int(time.time())))}"
        temp_jobs = ""
        for job in bounty['jobs']:
            temp_jobs += f"\n\t{job['jobType']}" \
                         f"\n\t\t奖励：{job['rewards'].replace('<br />', '、')}"
        temp_bounty += temp_jobs + "\n=================="
    return temp_bounty


# 裂隙
async def get_fissures():
    data = await get_data_json("fissures")
    temp_fissures = ""
    for fissure in data:
        temp_fissures += f"{fissure['modifier']}\t丨\t{fissure['missionType']}\t丨\t{fissure['node']}\t丨\t{await get_format_time('%H时%M分%S秒', await get_gm_time(fissure['expiry'] - int(time.time())))}\n"
    return temp_fissures


# 奸商
async def get_voidTrader():
    data = await get_data_json("trader")
    if time.time() < data['activation']:
        voidTrader_time = int(data['activation'] - time.time() - 86400)
    else:
        voidTrader_time = int(data['expiry'] - int(time.time()))
    return "==================" \
           f"\n{data['character']}" \
           f"\n地点丨{data['node']}" \
           f"\n剩余丨{await get_format_time('%d天%H时%M分%S秒', await get_gm_time(voidTrader_time))}" \
           f"\n=================="


# 突击
async def get_sortie():
    data = await get_data_json("sortie")
    temp_sortie = "==================" \
                  f"\n{data['boss']}  {await get_format_time('%H时%M分%S秒', await get_gm_time(data['expiry'] - int(time.time())))}" \
                  f"\n{data['faction']}"
    for variants in data['variants']:
        temp_sortie += f"\n\t{variants['missionType']} \t丨\t{variants['node']}\t丨\t{variants['modifierType']}"
    return temp_sortie


# 每日优惠
async def get_dailyDeals():
    data = await get_data_json("deals")
    temp_daily_deals = ""
    for daily_deal in data:
        temp_daily_deals += f"{daily_deal['item']}丨{daily_deal['discount']}%折扣丨{daily_deal['salePrice']}白金丨剩余 {await get_format_time('%H时%M分%S秒', await get_gm_time(daily_deal['expiry'] - time.time()))}\n"
    return temp_daily_deals


# 入侵
async def get_invasions():
    data = await get_data_json("invasions")
    temp_invasions = ""
    for invasion in data:
        temp_invasions += f"{invasion['node']}  \t丨\t{invasion['locTag']}   \t丨\t"
        if invasion['attacker']['rewards']:
            for attacker_reward in invasion['attacker']['rewards']:
                temp_invasions += f"{attacker_reward['item']}*{attacker_reward['itemCount']}"
            temp_invasions += " / "
        for defender_reward in invasion['defender']['rewards']:
            temp_invasions += f"{defender_reward['item']}*{defender_reward['itemCount']}\n"
    return temp_invasions


# 事件
async def get_events():
    data = await get_data_json("events")
    temp_event = ""
    for event in data:
        temp_event += f"{event['tag']}丨{await get_format_time('%H时%M分%S秒', await get_gm_time(event['expiry'] - int(time.time())))}\n"
    return temp_event


# 章节
async def get_season():
    data = await get_data_json("season")
    temp_season = ""
    for challenge in data['challenges']:
        temp_season += f"{challenge['cycle']}\t丨\t{challenge['xp']}xp\t丨\t{challenge['challenge']}\n"
    return temp_season


# 格式化时间
async def get_format_time(f, t):
    return time.strftime(f, t)


# GM 时区时间
async def get_gm_time(t) -> int:
    return time.gmtime(t)


# 当地时区时间
async def get_local_time(t) -> int:
    return time.localtime(t)


# UA 列表
user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
]


# UA
def get_user_agent():
    return {"User-Agent": random.choice(user_agent)}


# API 获取 Json 数据
async def get_data_json(url_arg):
    api_url = "https://api.null00.com/world/ZHCN/" + url_arg
    async with httpx.AsyncClient() as client:
        r = await client.get(url=api_url, headers=get_user_agent())
    return json.loads(r.text)
