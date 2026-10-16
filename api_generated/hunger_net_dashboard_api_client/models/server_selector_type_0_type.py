from enum import StrEnum


class ServerSelectorType0Type(StrEnum):
    UUIDS = "uuids"

    def __str__(self) -> str:
        return str(self.value)
