from enum import StrEnum


class ScheduleTriggerType4Type(StrEnum):
    DATABASE_BACKUP_STATUS = "database_backup_status"

    def __str__(self) -> str:
        return str(self.value)
