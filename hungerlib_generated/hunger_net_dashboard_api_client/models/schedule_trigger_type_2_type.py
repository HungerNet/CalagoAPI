from enum import StrEnum


class ScheduleTriggerType2Type(StrEnum):
    SERVER_STATE = "server_state"

    def __str__(self) -> str:
        return str(self.value)
