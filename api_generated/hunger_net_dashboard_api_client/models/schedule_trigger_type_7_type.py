from enum import StrEnum


class ScheduleTriggerType7Type(StrEnum):
    CONSOLE_LINE = "console_line"

    def __str__(self) -> str:
        return str(self.value)
