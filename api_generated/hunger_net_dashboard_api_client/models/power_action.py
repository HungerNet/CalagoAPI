from enum import StrEnum


class PowerAction(StrEnum):
    KILL = "kill"
    RESTART = "restart"
    START = "start"
    STOP = "stop"

    def __str__(self) -> str:
        return str(self.value)
