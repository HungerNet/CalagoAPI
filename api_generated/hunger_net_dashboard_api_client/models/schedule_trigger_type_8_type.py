from enum import StrEnum


class ScheduleTriggerType8Type(StrEnum):
    CRASH = "crash"

    def __str__(self) -> str:
        return str(self.value)
