from enum import StrEnum


class DatabaseAgentType(StrEnum):
    MARIADB = "mariadb"
    MONGODB = "mongodb"
    POSTGRES = "postgres"
    REDIS = "redis"

    def __str__(self) -> str:
        return str(self.value)
