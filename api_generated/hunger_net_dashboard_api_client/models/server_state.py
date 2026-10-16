from enum import StrEnum


class ServerState(StrEnum):
    OFFLINE = "offline"
    RUNNING = "running"
    STARTING = "starting"
    STOPPING = "stopping"

    def __str__(self) -> str:
        return str(self.value)
