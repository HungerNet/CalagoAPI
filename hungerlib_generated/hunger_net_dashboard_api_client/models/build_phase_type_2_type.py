from enum import StrEnum


class BuildPhaseType2Type(StrEnum):
    ADDING = "adding"

    def __str__(self) -> str:
        return str(self.value)
