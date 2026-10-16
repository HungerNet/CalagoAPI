from enum import StrEnum


class ScheduleConditionComparator(StrEnum):
    EQUAL = "equal"
    GREATER_THAN = "greater_than"
    GREATER_THAN_OR_EQUALS = "greater_than_or_equals"
    SMALLER_THAN = "smaller_than"
    SMALLER_THAN_OR_EQUALS = "smaller_than_or_equals"

    def __str__(self) -> str:
        return str(self.value)
