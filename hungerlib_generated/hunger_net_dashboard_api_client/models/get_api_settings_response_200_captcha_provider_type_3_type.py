from enum import StrEnum


class GetApiSettingsResponse200CaptchaProviderType3Type(StrEnum):
    HCAPTCHA = "hcaptcha"

    def __str__(self) -> str:
        return str(self.value)
