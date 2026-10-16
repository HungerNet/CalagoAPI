from enum import StrEnum


class MailModeType3Type(StrEnum):
    FILESYSTEM = "filesystem"

    def __str__(self) -> str:
        return str(self.value)
