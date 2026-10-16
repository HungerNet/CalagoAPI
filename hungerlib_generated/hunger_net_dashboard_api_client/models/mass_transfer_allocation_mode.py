from enum import StrEnum


class MassTransferAllocationMode(StrEnum):
    EGG_CONFIG_DEPLOYMENT = "egg_config_deployment"
    EGG_CONFIG_SELF_ASSIGN_RANGE = "egg_config_self_assign_range"
    NONE = "none"
    PRESERVE_PORTS = "preserve_ports"
    RANDOM_ALL = "random_all"
    RANDOM_PRIMARY = "random_primary"

    def __str__(self) -> str:
        return str(self.value)
