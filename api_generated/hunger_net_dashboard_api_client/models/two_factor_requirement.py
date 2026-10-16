from enum import StrEnum


class TwoFactorRequirement(StrEnum):
    ADMINS = "admins"
    ALL_USERS = "all_users"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
