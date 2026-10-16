from enum import StrEnum


class ScheduleResourceMetric(StrEnum):
    CPU = "cpu"
    DISK = "disk"
    MEMORY = "memory"

    def __str__(self) -> str:
        return str(self.value)
