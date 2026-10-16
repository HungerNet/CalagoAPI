from enum import StrEnum


class CompressionType(StrEnum):
    BZ2 = "bz2"
    GZ = "gz"
    LZ4 = "lz4"
    LZIP = "lzip"
    NONE = "none"
    XZ = "xz"
    ZSTD = "zstd"

    def __str__(self) -> str:
        return str(self.value)
