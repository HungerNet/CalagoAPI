from enum import StrEnum


class StorageDriverType1Type(StrEnum):
    S3 = "s3"

    def __str__(self) -> str:
        return str(self.value)
