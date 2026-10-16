from enum import StrEnum


class AllocationSelectorType1Type(StrEnum):
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
