from enum import StrEnum


class ServerBackupKind(StrEnum):
    DATABASE_INSTANCE = "database_instance"
    SERVER = "server"

    def __str__(self) -> str:
        return str(self.value)
