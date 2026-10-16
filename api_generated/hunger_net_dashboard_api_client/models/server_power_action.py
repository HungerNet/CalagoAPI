from enum import StrEnum


class ServerPowerAction(StrEnum):
    KILL = "kill"
    RESTART = "restart"
    START = "start"
    STOP = "stop"

    def __str__(self) -> str:
        return str(self.value)
