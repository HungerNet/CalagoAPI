from enum import StrEnum


class CaptchaProviderType5Type(StrEnum):
    CAP = "cap"

    def __str__(self) -> str:
        return str(self.value)
