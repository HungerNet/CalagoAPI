from enum import StrEnum


class ActivityIpHiding(StrEnum):
    ADMINS = "admins"
    ALL_USERS = "all_users"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
