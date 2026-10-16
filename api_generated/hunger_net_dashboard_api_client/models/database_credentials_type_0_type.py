from enum import StrEnum


class DatabaseCredentialsType0Type(StrEnum):
    CONNECTION_STRING = "connection_string"

    def __str__(self) -> str:
        return str(self.value)
