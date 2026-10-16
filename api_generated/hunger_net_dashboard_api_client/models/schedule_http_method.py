from enum import StrEnum


class ScheduleHttpMethod(StrEnum):
    DELETE = "delete"
    GET = "get"
    HEAD = "head"
    PATCH = "patch"
    POST = "post"
    PUT = "put"

    def __str__(self) -> str:
        return str(self.value)
