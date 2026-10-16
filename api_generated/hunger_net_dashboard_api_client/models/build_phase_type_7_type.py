from enum import StrEnum


class BuildPhaseType7Type(StrEnum):
    INSTALLING = "installing"

    def __str__(self) -> str:
        return str(self.value)
