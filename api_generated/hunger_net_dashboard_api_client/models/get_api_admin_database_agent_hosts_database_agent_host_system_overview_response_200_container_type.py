from enum import StrEnum


class GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200ContainerType(StrEnum):
    NONE = "none"
    OFFICIAL = "official"
    OFFICIAL_AIO = "official_aio"
    OFFICIAL_HEAVY = "official_heavy"
    OFFICIAL_HEAVY_AIO = "official_heavy_aio"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
