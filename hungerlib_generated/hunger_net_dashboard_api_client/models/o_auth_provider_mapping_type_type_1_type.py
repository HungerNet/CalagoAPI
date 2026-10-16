from enum import StrEnum


class OAuthProviderMappingTypeType1Type(StrEnum):
    SERVER_SUBUSER = "server_subuser"

    def __str__(self) -> str:
        return str(self.value)
