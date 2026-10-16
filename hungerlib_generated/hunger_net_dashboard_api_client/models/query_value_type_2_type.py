from enum import StrEnum


class QueryValueType2Type(StrEnum):
    BINARY = "binary"

    def __str__(self) -> str:
        return str(self.value)
