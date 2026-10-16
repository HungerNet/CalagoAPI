from enum import StrEnum


class AuthenticationType(StrEnum):
    PASSWORD = "password"
    PUBLIC_KEY = "public_key"

    def __str__(self) -> str:
        return str(self.value)
