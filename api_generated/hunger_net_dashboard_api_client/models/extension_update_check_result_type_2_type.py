from enum import StrEnum


class ExtensionUpdateCheckResultType2Type(StrEnum):
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
