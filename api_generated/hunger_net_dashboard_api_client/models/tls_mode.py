from enum import StrEnum


class TlsMode(StrEnum):
    IMPLICIT_TLS = "implicit_tls"
    NONE = "none"
    START_TLS = "start_tls"

    def __str__(self) -> str:
        return str(self.value)
