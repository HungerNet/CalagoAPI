from enum import StrEnum


class CaptchaProviderType0Type(StrEnum):
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
