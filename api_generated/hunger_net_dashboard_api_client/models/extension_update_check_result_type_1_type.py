from enum import StrEnum


class ExtensionUpdateCheckResultType1Type(StrEnum):
    UPDATE_AVAILABLE = "update_available"

    def __str__(self) -> str:
        return str(self.value)
