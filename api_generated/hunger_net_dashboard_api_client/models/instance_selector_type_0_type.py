from enum import StrEnum


class InstanceSelectorType0Type(StrEnum):
    UUIDS = "uuids"

    def __str__(self) -> str:
        return str(self.value)
