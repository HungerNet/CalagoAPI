from enum import StrEnum


class EggRepositoryCredentialsType2Type(StrEnum):
    PRIVATE_KEY = "private_key"

    def __str__(self) -> str:
        return str(self.value)
