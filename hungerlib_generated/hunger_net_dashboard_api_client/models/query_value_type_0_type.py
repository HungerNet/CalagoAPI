from enum import StrEnum


class QueryValueType0Type(StrEnum):
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
