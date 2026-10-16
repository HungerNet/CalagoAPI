from enum import StrEnum


class SupervisorStateType0Type(StrEnum):
    IDLE = "idle"

    def __str__(self) -> str:
        return str(self.value)
