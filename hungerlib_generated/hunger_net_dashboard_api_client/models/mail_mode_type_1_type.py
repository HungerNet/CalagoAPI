from enum import StrEnum


class MailModeType1Type(StrEnum):
    SMTP = "smtp"

    def __str__(self) -> str:
        return str(self.value)
