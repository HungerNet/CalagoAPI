from enum import StrEnum


class ServerBackupStatus(StrEnum):
    FAILED = "failed"
    FINISHED = "finished"
    STARTING = "starting"

    def __str__(self) -> str:
        return str(self.value)
