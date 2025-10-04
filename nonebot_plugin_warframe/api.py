from typing import TypeVar

from httpx import AsyncClient
from nonebot.compat import type_validate_python

from .models import (
    Alert,
    Bounty,
    Cetus,
    DailyDeal,
    Earth,
    Event,
    Fissure,
    Invasion,
    New,
    Season,
    Solaris,
    Sortie,
    VoidTrader,
)

T = TypeVar("T")


class API:
    url = "https://api.null00.com/world/ZHCN/"

    async def _query(self, endpoint: str, type_: type[T]) -> T:
        async with AsyncClient() as client:
            resp = await client.get(self.url + endpoint)
            resp.raise_for_status()
            return type_validate_python(type_, resp.json())

    async def get_alerts(self) -> list[Alert]:
        return await self._query("alerts", list[Alert])

    async def get_news(self) -> list[New]:
        return await self._query("news", list[New])

    async def get_cetus(self) -> Cetus:
        return await self._query("cetus", Cetus)

    async def get_earth(self) -> Earth:
        return await self._query("earth", Earth)

    async def get_solaris(self) -> Solaris:
        return await self._query("solaris", Solaris)

    async def get_bountys(self) -> list[Bounty]:
        return await self._query("bounty", list[Bounty])

    async def get_fissures(self) -> list[Fissure]:
        return await self._query("fissures", list[Fissure])

    async def get_voidTrader(self) -> VoidTrader:
        return await self._query("trader", VoidTrader)

    async def get_sortie(self) -> Sortie:
        return await self._query("sortie", Sortie)

    async def get_dailyDeals(self) -> list[DailyDeal]:
        return await self._query("deals", list[DailyDeal])

    async def get_invasions(self) -> list[Invasion]:
        return await self._query("invasions", list[Invasion])

    async def get_events(self) -> list[Event]:
        return await self._query("events", list[Event])

    async def get_season(self) -> Season:
        return await self._query("season", Season)

    async def get_additional_alerts(self) -> list[Alert]:
        return await self._query("additional_alerts", list[Alert])

    async def get_additional_news(self) -> list[New]:
        return await self._query("additional_news", list[New])

    async def get_additional_cetus(self) -> Cetus:
        return await self._query("additional_cetus", Cetus)

    async def get_additional_earth(self) -> Earth:
        return await self._query("additional_earth", Earth)

    async def get_additional_solaris(self) -> Solaris:
        return await self._query("additional_solaris", Solaris)

    async def get_additional_bountys(self) -> list[Bounty]:
        return await self._query("additional_bounty", list[Bounty])

    async def get_additional_fissures(self) -> list[Fissure]:
        return await self._query("additional_fissures", list[Fissure])

    async def get_additional_voidTrader(self) -> VoidTrader:
        return await self._query("additional_trader", VoidTrader)

    async def get_additional_sortie(self) -> Sortie:
        return await self._query("additional_sortie", Sortie)

    async def get_additional_dailyDeals(self) -> list[DailyDeal]:
        return await self._query("additional_deals", list[DailyDeal])

    async def get_additional_invasions(self) -> list[Invasion]:
        return await self._query("additional_invasions", list[Invasion])

    async def get_additional_events(self) -> list[Event]:
        return await self._query("additional_events", list[Event])

    async def get_additional_season(self) -> Season:
        return await self._query("additional_season", Season)
