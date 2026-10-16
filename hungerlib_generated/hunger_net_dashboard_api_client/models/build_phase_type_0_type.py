from enum import StrEnum


class BuildPhaseType0Type(StrEnum):
    PREPARING = "preparing"

    def __str__(self) -> str:
        return str(self.value)
