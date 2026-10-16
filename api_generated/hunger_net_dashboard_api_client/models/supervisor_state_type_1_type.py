from enum import StrEnum


class SupervisorStateType1Type(StrEnum):
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
