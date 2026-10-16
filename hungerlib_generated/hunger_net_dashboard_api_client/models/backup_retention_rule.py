from enum import StrEnum


class BackupRetentionRule(StrEnum):
    COUNT = "count"
    DAILY = "daily"
    DAYS = "days"
    MONTHLY = "monthly"
    WEEKLY = "weekly"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)
