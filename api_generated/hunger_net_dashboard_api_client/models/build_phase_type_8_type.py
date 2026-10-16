from enum import StrEnum


class BuildPhaseType8Type(StrEnum):
    RESTARTING = "restarting"

    def __str__(self) -> str:
        return str(self.value)
