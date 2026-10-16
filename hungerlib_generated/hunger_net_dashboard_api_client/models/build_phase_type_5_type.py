from enum import StrEnum


class BuildPhaseType5Type(StrEnum):
    BUILDING = "building"

    def __str__(self) -> str:
        return str(self.value)
