from enum import StrEnum


class SupervisorStateType4Type(StrEnum):
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
