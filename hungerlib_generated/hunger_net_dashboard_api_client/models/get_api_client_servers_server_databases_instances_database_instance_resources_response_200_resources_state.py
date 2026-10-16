from enum import StrEnum


class GetApiClientServersServerDatabasesInstancesDatabaseInstanceResourcesResponse200ResourcesState(StrEnum):
    OFFLINE = "offline"
    RUNNING = "running"
    STARTING = "starting"
    STOPPING = "stopping"

    def __str__(self) -> str:
        return str(self.value)
