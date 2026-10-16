from enum import StrEnum


class PostApiAuthLoginResponse200Type1Type(StrEnum):
    TWO_FACTOR_REQUIRED = "two_factor_required"

    def __str__(self) -> str:
        return str(self.value)
