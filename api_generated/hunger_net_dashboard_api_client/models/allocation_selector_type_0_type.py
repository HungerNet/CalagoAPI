from enum import StrEnum


class AllocationSelectorType0Type(StrEnum):
    UUIDS = "uuids"

    def __str__(self) -> str:
        return str(self.value)
