from enum import StrEnum


class ScheduleBackupSelectorType3Mode(StrEnum):
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
