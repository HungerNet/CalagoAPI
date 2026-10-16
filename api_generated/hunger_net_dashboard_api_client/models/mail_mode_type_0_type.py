from enum import StrEnum


class MailModeType0Type(StrEnum):
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
