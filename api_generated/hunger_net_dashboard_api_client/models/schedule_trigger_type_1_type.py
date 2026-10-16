from enum import StrEnum


class ScheduleTriggerType1Type(StrEnum):
    POWER_ACTION = "power_action"

    def __str__(self) -> str:
        return str(self.value)
