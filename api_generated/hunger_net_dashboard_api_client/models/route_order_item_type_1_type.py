from enum import StrEnum


class RouteOrderItemType1Type(StrEnum):
    DIVIDER = "divider"

    def __str__(self) -> str:
        return str(self.value)
