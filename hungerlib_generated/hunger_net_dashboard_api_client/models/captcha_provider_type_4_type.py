from enum import StrEnum


class CaptchaProviderType4Type(StrEnum):
    FRIENDLY_CAPTCHA = "friendly_captcha"

    def __str__(self) -> str:
        return str(self.value)
