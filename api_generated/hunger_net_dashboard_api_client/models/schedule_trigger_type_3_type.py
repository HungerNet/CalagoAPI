from enum import StrEnum


class ScheduleTriggerType3Type(StrEnum):
    BACKUP_STATUS = "backup_status"

    def __str__(self) -> str:
        return str(self.value)
