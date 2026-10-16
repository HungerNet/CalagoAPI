from enum import StrEnum


class EggRepositoryCredentialsType1Type(StrEnum):
    PASSWORD = "password"

    def __str__(self) -> str:
        return str(self.value)
