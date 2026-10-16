from enum import StrEnum


class CaptchaProviderType3Type(StrEnum):
    HCAPTCHA = "hcaptcha"

    def __str__(self) -> str:
        return str(self.value)
