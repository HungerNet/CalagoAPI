from enum import StrEnum


class ServerBackupRetentionState(StrEnum):
    EXPIRED = "expired"
    FAILED = "failed"
    INDEFINITE = "indefinite"
    LOCKED = "locked"
    RETAINED = "retained"

    def __str__(self) -> str:
        return str(self.value)
