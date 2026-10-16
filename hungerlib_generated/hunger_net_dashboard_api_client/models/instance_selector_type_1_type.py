from enum import StrEnum


class InstanceSelectorType1Type(StrEnum):
    OUTDATED = "outdated"

    def __str__(self) -> str:
        return str(self.value)
