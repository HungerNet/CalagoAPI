from enum import StrEnum


class TwoFactorMethod(StrEnum):
    EMAIL = "email"
    SECURITY_KEY = "security_key"
    TOTP = "totp"

    def __str__(self) -> str:
        return str(self.value)
