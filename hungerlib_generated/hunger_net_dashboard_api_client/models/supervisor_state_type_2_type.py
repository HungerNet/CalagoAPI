from enum import StrEnum


class SupervisorStateType2Type(StrEnum):
    BUILDING = "building"

    def __str__(self) -> str:
        return str(self.value)
