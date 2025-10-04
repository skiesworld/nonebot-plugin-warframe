from typing import Any

from pydantic import BaseModel, Field


class Reward(BaseModel):
    """
    警报/入侵等场景下的奖励物品数据模型。
    """

    id: Any
    """奖励唯一标识符"""
    oid: str
    """奖励对象ID"""
    item: str
    """奖励物品名称"""
    item_count: int = Field(..., alias="itemCount")
    """奖励物品数量"""
    image_url: str = Field(..., alias="imageUrl")
    """奖励物品图片链接"""
    count: bool
    """是否为计数型奖励"""


class Alert(BaseModel):
    oid: str
    """警报对象ID"""
    activation: int
    """警报开始时间（时间戳）"""
    expiry: int
    """警报结束时间（时间戳）"""
    mission_type: str = Field(..., alias="missionType")
    """任务类型"""
    faction: str
    """敌方阵营"""
    location: str
    """任务地点"""
    min_enemy_level: int = Field(..., alias="minEnemyLevel")
    """敌人最低等级"""
    max_enemy_level: int = Field(..., alias="maxEnemyLevel")
    """敌人最高等级"""
    credits: int
    """现金奖励"""
    rewards: list[Reward]
    """奖励列表"""

    def __str__(self) -> str:
        rewards_str = ""
        for reward in self.rewards:
            rewards_str += f"\n\t{reward.item} * {reward.item_count}"
        return (
            f"{self.location}\n"
            f"{self.mission_type}丨{self.faction}（{self.min_enemy_level} ~ {self.max_enemy_level}）\n"
            f"奖励丨星币 * {self.credits}"
            f"{rewards_str}\n=================="
        )

    """
    Warframe世界中的警报事件数据模型。
    """

    oid: str
    """警报对象ID"""
    activation: int
    """警报开始时间（时间戳）"""
    expiry: int
    """警报结束时间（时间戳）"""
    mission_type: str = Field(..., alias="missionType")
    """任务类型"""
    faction: str
    """敌方阵营"""
    location: str
    """任务地点"""
    min_enemy_level: int = Field(..., alias="minEnemyLevel")
    """敌人最低等级"""
    max_enemy_level: int = Field(..., alias="maxEnemyLevel")
    """敌人最高等级"""
    credits: int
    """现金奖励"""
    rewards: list[Reward]
    """奖励列表"""


class New(BaseModel):
    priority: bool
    """是否为重要新闻"""
    date: int
    """发布时间（时间戳）"""
    event_start_date: int | None = Field(..., alias="eventStartDate")
    """活动开始时间（时间戳）"""
    default_messages: str = Field(..., alias="defaultMessages")
    """默认消息内容"""
    oid: str
    """新闻对象ID"""
    image_url: Any = Field(..., alias="imageUrl")
    """新闻图片链接"""
    mobile_only: bool = Field(..., alias="mobileOnly")
    """是否仅限移动端"""
    prop: str
    """其他属性（API扩展字段）"""

    def __str__(self) -> str:
        return (
            f"{self.default_messages}\n"
            f"时间丨{self.date}\n"
            f"链接丨{self.prop}\n=================="
        )

    """
    游戏内新闻公告数据模型。
    """

    priority: bool
    """是否为重要新闻"""
    date: int
    """发布时间（时间戳）"""
    event_start_date: int | None = Field(..., alias="eventStartDate")
    """活动开始时间（时间戳）"""
    default_messages: str = Field(..., alias="defaultMessages")
    """默认消息内容"""
    oid: str
    """新闻对象ID"""
    image_url: Any = Field(..., alias="imageUrl")
    """新闻图片链接"""
    mobile_only: bool = Field(..., alias="mobileOnly")
    """是否仅限移动端"""
    prop: str
    """其他属性（API扩展字段）"""


class Cetus(BaseModel):
    """
    赛特斯昼夜循环状态数据模型。
    """

    oid: str
    """赛特斯对象ID"""
    activation: int
    """昼夜循环开始时间（时间戳）"""
    expiry: int
    """昼夜循环结束时间（时间戳）"""
    cetus_time: int = Field(..., alias="cetusTime")
    """赛特斯昼夜时间（分钟）"""
    day: bool
    """是否为白天"""


class Earth(BaseModel):
    """
    地球昼夜循环状态数据模型。
    """

    earth_date: int = Field(..., alias="earthDate")
    """地球昼夜循环时间（时间戳）"""
    day: bool
    """是否为白天"""


class Solaris(BaseModel):
    """
    索拉里斯昼夜循环状态数据模型。
    """

    oid: str
    """索拉里斯对象ID"""
    activation: int
    """昼夜循环开始时间（时间戳）"""
    expiry: int
    """昼夜循环结束时间（时间戳）"""
    solaris_activation: int = Field(..., alias="solarisActivation")
    """索拉里斯昼夜开始时间"""
    solaris_expiry: int = Field(..., alias="solarisExpiry")
    """索拉里斯昼夜结束时间"""
    solaris_next_long: int = Field(..., alias="solarisNextLong")
    """索拉里斯下次长周期时间"""
    state: int
    """当前昼夜状态"""


class Job(BaseModel):
    """
    赏金任务详细信息数据模型。
    """

    job_type: str = Field(..., alias="jobType")
    """任务类型"""
    rewards: str
    """奖励内容（字符串描述）"""
    min_enemy_level: int = Field(..., alias="minEnemyLevel")
    """敌人最低等级"""
    max_enemy_level: int = Field(..., alias="maxEnemyLevel")
    """敌人最高等级"""
    mastery_req: int = Field(..., alias="masteryReq")
    """所需段位等级"""
    xp_amounts: list[int] = Field(..., alias="xpAmounts")
    """经验奖励列表"""
    vault: bool | None
    """是否为金库任务"""

    def __str__(self) -> str:
        return f"{self.job_type}\n\t奖励：{self.rewards.replace('<br />', '、')}"


class Bounty(BaseModel):
    """
    赏金活动整体数据模型。
    """

    tag: str
    """赏金标签"""
    oid: str
    """赏金对象ID"""
    activation: int
    """赏金开始时间（时间戳）"""
    expiry: int
    """赏金结束时间（时间戳）"""
    jobs: list[Job]
    """赏金任务列表"""

    def __str__(self) -> str:
        jobs_str = ""
        for job in self.jobs:
            jobs_str += f"\n{job}"
        return f"{self.tag}   剩余时间：{self.expiry}\n{jobs_str}\n=================="


class Fissure(BaseModel):
    """
    虚空裂隙事件数据模型。
    """

    oid: str
    """裂隙对象ID"""
    activation: int
    """裂隙开始时间（时间戳）"""
    expiry: int
    """裂隙结束时间（时间戳）"""
    node: str
    """裂隙所在节点"""
    mission_type: str = Field(..., alias="missionType")
    """任务类型"""
    modifier: str
    """裂隙修饰符"""
    faction: str
    """敌方阵营"""
    hard: bool | None
    """是否为高难度裂隙"""

    def __str__(self) -> str:
        return f"{self.modifier}\t丨\t{self.mission_type}\t丨\t{self.node}\t丨\t{self.expiry}\n"


class VoidTrader(BaseModel):
    """
    虚空奸商（Baro Ki'Teer）数据模型。
    """

    oid: str
    """奸商对象ID"""
    activation: int
    """奸商到达时间（时间戳）"""
    expiry: int
    """奸商离开时间（时间戳）"""
    character: str
    """奸商角色名"""
    node: str
    """奸商所在节点"""
    arrivals: bool
    """是否已到达"""
    manifest: Any
    """商品清单（字符串描述）"""

    def __str__(self) -> str:
        return (
            f"==================\n"
            f"{self.character}\n"
            f"地点丨{self.node}\n"
            f"剩余丨{self.expiry}\n=================="
        )


class Variant(BaseModel):
    """
    突击任务变体详细数据模型。
    """

    mission_type: str = Field(..., alias="missionType")
    """任务类型"""
    modifier_type: str = Field(..., alias="modifierType")
    """任务修饰符类型"""
    node: str
    """任务节点"""
    tileset: str
    """地图类型"""


class Sortie(BaseModel):
    def __str__(self) -> str:
        variants_str = ""
        for variant in self.variants:
            variants_str += f"\n\t{variant.mission_type} \t丨\t{variant.node}\t丨\t{variant.modifier_type}"
        return (
            f"==================\n"
            f"{self.boss}  {self.expiry}\n"
            f"{self.faction}"
            f"{variants_str}"
        )

    """
    突击任务整体数据模型。
    """

    oid: str
    """突击对象ID"""
    activation: int
    """突击开始时间（时间戳）"""
    expiry: int
    """突击结束时间（时间戳）"""
    boss: str
    """突击Boss名称"""
    faction: str
    """敌方阵营"""
    reward: str
    """突击奖励"""
    variants: list[Variant]
    """突击任务变体列表"""


class DailyDeal(BaseModel):
    def __str__(self) -> str:
        return f"{self.item}丨{self.discount}%折扣丨{self.sale_price}白金丨剩余 {self.expiry}\n"

    """
    每日特惠商品数据模型。
    """

    item: str
    """商品名称"""
    activation: int
    """优惠开始时间（时间戳）"""
    expiry: int
    """优惠结束时间（时间戳）"""
    discount: int
    """折扣百分比"""
    original_price: int = Field(..., alias="originalPrice")
    """原价"""
    sale_price: int = Field(..., alias="salePrice")
    """现价"""
    total: int
    """总库存"""
    sold: int
    """已售数量"""
    image_url: str = Field(..., alias="imageUrl")
    """商品图片链接"""


class Reward1(BaseModel):
    """
    入侵奖励（进攻方）数据模型。
    """

    id: Any
    """奖励唯一标识符"""
    oid: str
    """奖励对象ID"""
    item: str
    """奖励物品名称"""
    item_count: int = Field(..., alias="itemCount")
    """奖励物品数量"""
    image_url: str = Field(..., alias="imageUrl")
    """奖励物品图片链接"""
    count: bool
    """是否为计数型奖励"""


class Attacker(BaseModel):
    """
    入侵事件进攻方数据模型。
    """

    faction: str
    """阵营名称"""
    rewards: list[Reward1]
    """奖励列表"""


class Reward2(BaseModel):
    """
    入侵奖励（防守方）数据模型。
    """

    id: Any
    """奖励唯一标识符"""
    oid: str
    """奖励对象ID"""
    item: str
    """奖励物品名称"""
    item_count: int = Field(..., alias="itemCount")
    """奖励物品数量"""
    image_url: str = Field(..., alias="imageUrl")
    """奖励物品图片链接"""
    count: bool
    """是否为计数型奖励"""


class Defender(BaseModel):
    """
    入侵事件防守方数据模型。
    """

    faction: str
    """阵营名称"""
    rewards: list[Reward2]
    """奖励列表"""


class Invasion(BaseModel):
    def __str__(self) -> str:
        attacker_str = ""
        if self.attacker.rewards:
            for r in self.attacker.rewards:
                attacker_str += f"{r.item}*{r.item_count}"
            attacker_str += " / "
        defender_str = ""
        for r in self.defender.rewards:
            defender_str += f"{r.item}*{r.item_count}"
        return (
            f"{self.node}  \t丨\t{self.loc_tag}   \t丨\t{attacker_str}{defender_str}\n"
        )

    """
    入侵事件整体数据模型。
    """

    oid: str
    """入侵对象ID"""
    activation: int
    """入侵开始时间（时间戳）"""
    node: str
    """入侵节点"""
    count: int
    """当前进度"""
    goal: int
    """目标进度"""
    loc_tag: str = Field(..., alias="locTag")
    """节点标签"""
    attacker: Attacker
    """进攻方信息"""
    defender: Defender
    """防守方信息"""
    completed: bool
    """是否已完成"""


class Event(BaseModel):
    def __str__(self) -> str:
        return f"{self.tag}丨{self.expiry}\n"

    """
    世界事件（如节点健康等）数据模型。
    """

    oid: str
    """事件对象ID"""
    tag: str
    """事件标签"""
    node: str | None
    """事件节点"""
    activation: int
    """事件开始时间（时间戳）"""
    expiry: int
    """事件结束时间（时间戳）"""
    health_pct: float | None = Field(..., alias="healthPct")
    """节点健康百分比"""


class Challenge(BaseModel):
    def __str__(self) -> str:
        return f"{self.cycle}\t丨\t{self.xp}xp\t丨\t{self.challenge}\n"

    """
    赛季挑战任务数据模型。
    """

    oid: str
    """挑战对象ID"""
    daily: bool
    """是否为每日挑战"""
    activation: int
    """挑战开始时间（时间戳）"""
    expiry: int
    """挑战结束时间（时间戳）"""
    name: str
    """挑战名称"""
    challenge: str
    """挑战内容描述"""
    cycle: str
    """挑战周期"""
    xp: int
    """经验奖励"""


class Season(BaseModel):
    def __str__(self) -> str:
        challenges_str = ""
        for c in self.challenges:
            challenges_str += str(c)
        return challenges_str

    """
    赛季活动整体数据模型。
    """

    activation: int
    """赛季开始时间（时间戳）"""
    expiry: int
    """赛季结束时间（时间戳）"""
    tag: str
    """赛季标签"""
    season: int
    """赛季编号"""
    phase: int
    """当前阶段"""
    params: str
    """赛季参数（字符串描述）"""
    challenges: list[Challenge]
    """挑战列表"""
    reward: str
    """赛季奖励"""


class WarframeData(BaseModel):
    """
    Warframe游戏数据的整体数据模型。
    """

    time: int | None = None
    """数据获取时间（时间戳）"""

    alerts: list[Alert] | None = None
    """警报列表"""

    news: list[New] | None = None
    """新闻列表"""

    cetus: Cetus | None = None
    """塞图斯时间信息"""

    earth: Earth | None = None
    """地球时间信息"""

    solaris: Solaris | None = None
    """太阳系时间信息"""

    bountys: list[Bounty] | None = None
    """赏金任务列表"""

    fissures: list[Fissure] | None = None
    """虚空裂隙列表"""

    void_trader: VoidTrader | None = Field(None, alias="voidTrader")
    """虚空奸商信息"""

    sortie: Sortie | None = None
    """突击任务信息"""

    daily_deals: list[DailyDeal] | None = Field(None, alias="dailyDeals")
    """每日特惠商品列表"""

    invasions: list[Invasion] | None = None
    """入侵事件列表"""

    events: list[Event] | None = None
    """事件列表"""

    sales: Any | None = None
    """促销信息（API扩展字段）"""

    season: Season | None = None
    """赛季活动信息"""
