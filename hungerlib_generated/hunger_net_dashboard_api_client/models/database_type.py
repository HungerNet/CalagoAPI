from enum import StrEnum


class DatabaseType(StrEnum):
    MONGODB = "mongodb"
    MYSQL = "mysql"
    POSTGRES = "postgres"

    def __str__(self) -> str:
        return str(self.value)
