from enum import StrEnum


class ScheduleTriggerType6Type(StrEnum):
    RESOURCE_USAGE = "resource_usage"

    def __str__(self) -> str:
        return str(self.value)
