from enum import StrEnum


class TwitterCard(StrEnum):
    SUMMARY = "summary"
    SUMMARY_LARGE_IMAGE = "summary_large_image"

    def __str__(self) -> str:
        return str(self.value)
