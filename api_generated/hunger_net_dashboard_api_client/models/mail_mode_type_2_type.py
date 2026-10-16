from enum import StrEnum


class MailModeType2Type(StrEnum):
    SENDMAIL = "sendmail"

    def __str__(self) -> str:
        return str(self.value)
