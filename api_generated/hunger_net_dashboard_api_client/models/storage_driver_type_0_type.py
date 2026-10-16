from enum import StrEnum


class StorageDriverType0Type(StrEnum):
    FILESYSTEM = "filesystem"

    def __str__(self) -> str:
        return str(self.value)
