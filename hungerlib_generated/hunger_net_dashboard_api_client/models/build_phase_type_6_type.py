from enum import StrEnum


class BuildPhaseType6Type(StrEnum):
    VERIFYING = "verifying"

    def __str__(self) -> str:
        return str(self.value)
