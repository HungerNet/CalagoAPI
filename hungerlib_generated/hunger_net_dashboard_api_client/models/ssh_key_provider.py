from enum import StrEnum


class SshKeyProvider(StrEnum):
    GITHUB = "github"
    GITLAB = "gitlab"
    LAUNCHPAD = "launchpad"

    def __str__(self) -> str:
        return str(self.value)
