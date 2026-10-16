from enum import StrEnum


class CompressionLevel(StrEnum):
    BEST_COMPRESSION = "best_compression"
    BEST_SPEED = "best_speed"
    GOOD_COMPRESSION = "good_compression"
    GOOD_SPEED = "good_speed"

    def __str__(self) -> str:
        return str(self.value)
