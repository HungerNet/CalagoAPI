from enum import StrEnum


class ScheduleTriggerType0Type(StrEnum):
    CRON = "cron"

    def __str__(self) -> str:
        return str(self.value)
