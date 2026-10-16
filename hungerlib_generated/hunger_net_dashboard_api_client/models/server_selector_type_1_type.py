from enum import StrEnum


class ServerSelectorType1Type(StrEnum):
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
