from enum import StrEnum


class ScheduleBackupSelectorType1Mode(StrEnum):
    OLDEST = "oldest"

    def __str__(self) -> str:
        return str(self.value)
