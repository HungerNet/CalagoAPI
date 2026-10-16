from enum import StrEnum


class ScheduleBackupSelectorType0Mode(StrEnum):
    LATEST = "latest"

    def __str__(self) -> str:
        return str(self.value)
