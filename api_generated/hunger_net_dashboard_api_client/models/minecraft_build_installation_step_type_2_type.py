from enum import StrEnum


class MinecraftBuildInstallationStepType2Type(StrEnum):
    REMOVE = "remove"

    def __str__(self) -> str:
        return str(self.value)
