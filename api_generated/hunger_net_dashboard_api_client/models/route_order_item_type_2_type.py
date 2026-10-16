from enum import StrEnum


class RouteOrderItemType2Type(StrEnum):
    REDIRECT = "redirect"

    def __str__(self) -> str:
        return str(self.value)
