from enum import StrEnum


class ScheduleBackupSelectorType2Mode(StrEnum):
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
