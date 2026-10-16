from enum import StrEnum


class BuildPhaseType3Type(StrEnum):
    RESYNC = "resync"

    def __str__(self) -> str:
        return str(self.value)
