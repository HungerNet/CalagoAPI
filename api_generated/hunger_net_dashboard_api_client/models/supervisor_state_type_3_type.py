from enum import StrEnum


class SupervisorStateType3Type(StrEnum):
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
