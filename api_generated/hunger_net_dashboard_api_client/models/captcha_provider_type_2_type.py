from enum import StrEnum


class CaptchaProviderType2Type(StrEnum):
    RECAPTCHA = "recaptcha"

    def __str__(self) -> str:
        return str(self.value)
