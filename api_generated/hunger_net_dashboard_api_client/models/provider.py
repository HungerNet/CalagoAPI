from enum import StrEnum


class Provider(StrEnum):
    CLOUDFLARE = "cloudflare"
    POWERDNS = "powerdns"

    def __str__(self) -> str:
        return str(self.value)
