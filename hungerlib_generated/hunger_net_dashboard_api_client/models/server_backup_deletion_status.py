from enum import StrEnum


class ServerBackupDeletionStatus(StrEnum):
    DELETING = "deleting"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
