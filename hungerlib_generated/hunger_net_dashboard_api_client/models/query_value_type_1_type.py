from enum import StrEnum


class QueryValueType1Type(StrEnum):
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
