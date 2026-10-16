from enum import StrEnum


class CaptchaProviderType1Type(StrEnum):
    TURNSTILE = "turnstile"

    def __str__(self) -> str:
        return str(self.value)
