from enum import StrEnum


class ArchiveFormat(StrEnum):
    SEVEN_ZIP = "seven_zip"
    TAR = "tar"
    TAR_BZ2 = "tar_bz2"
    TAR_GZ = "tar_gz"
    TAR_LZ4 = "tar_lz4"
    TAR_LZIP = "tar_lzip"
    TAR_XZ = "tar_xz"
    TAR_ZSTD = "tar_zstd"
    ZIP = "zip"

    def __str__(self) -> str:
        return str(self.value)
