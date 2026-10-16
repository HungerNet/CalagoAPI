from enum import StrEnum


class FilterOperator(StrEnum):
    CONTAINS = "contains"
    ENDS_WITH = "ends_with"
    EQ = "eq"
    GT = "gt"
    GTE = "gte"
    IS_NULL = "is_null"
    LT = "lt"
    LTE = "lte"
    NE = "ne"
    NOT_NULL = "not_null"
    STARTS_WITH = "starts_with"

    def __str__(self) -> str:
        return str(self.value)
