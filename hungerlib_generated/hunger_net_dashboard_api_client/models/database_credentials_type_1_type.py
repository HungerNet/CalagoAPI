from enum import StrEnum


class DatabaseCredentialsType1Type(StrEnum):
    DETAILS = "details"

    def __str__(self) -> str:
        return str(self.value)
