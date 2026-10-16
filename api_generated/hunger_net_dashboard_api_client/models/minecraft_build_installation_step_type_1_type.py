from enum import StrEnum


class MinecraftBuildInstallationStepType1Type(StrEnum):
    UNZIP = "unzip"

    def __str__(self) -> str:
        return str(self.value)
