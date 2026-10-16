from enum import StrEnum


class ServerConfigurationAutoStartBehavior(StrEnum):
    ALWAYS = "always"
    NEVER = "never"
    UNLESS_STOPPED = "unless_stopped"

    def __str__(self) -> str:
        return str(self.value)
