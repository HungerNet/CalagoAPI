from enum import StrEnum


class AllocationSelectorType2Type(StrEnum):
    FILTER = "filter"

    def __str__(self) -> str:
        return str(self.value)
