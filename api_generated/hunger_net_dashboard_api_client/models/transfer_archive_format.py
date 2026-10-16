from enum import StrEnum


class TransferArchiveFormat(StrEnum):
    ITAF = "itaf"
    ITAF_BZ2 = "itaf_bz2"
    ITAF_GZ = "itaf_gz"
    ITAF_LZ4 = "itaf_lz4"
    ITAF_LZIP = "itaf_lzip"
    ITAF_XZ = "itaf_xz"
    ITAF_ZSTD = "itaf_zstd"
    TAR = "tar"
    TAR_BZ2 = "tar_bz2"
    TAR_GZ = "tar_gz"
    TAR_LZ4 = "tar_lz4"
    TAR_LZIP = "tar_lzip"
    TAR_XZ = "tar_xz"
    TAR_ZSTD = "tar_zstd"

    def __str__(self) -> str:
        return str(self.value)
