from enum import StrEnum


class BuildPhaseType4Type(StrEnum):
    STAGING_TRANSLATIONS = "staging_translations"

    def __str__(self) -> str:
        return str(self.value)
