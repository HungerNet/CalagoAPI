from enum import StrEnum


class ScheduleTriggerType5Type(StrEnum):
    SCHEDULE_COMPLETION = "schedule_completion"

    def __str__(self) -> str:
        return str(self.value)
