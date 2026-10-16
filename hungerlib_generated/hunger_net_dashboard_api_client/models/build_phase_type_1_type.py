from enum import StrEnum


class BuildPhaseType1Type(StrEnum):
    CLEARING = "clearing"

    def __str__(self) -> str:
        return str(self.value)
