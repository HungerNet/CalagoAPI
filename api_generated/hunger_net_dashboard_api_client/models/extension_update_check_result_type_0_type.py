from enum import StrEnum


class ExtensionUpdateCheckResultType0Type(StrEnum):
    NO_UPDATE = "no_update"

    def __str__(self) -> str:
        return str(self.value)
