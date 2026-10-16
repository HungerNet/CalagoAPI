from enum import StrEnum


class GetApiSettingsResponse200CaptchaProviderType2Type(StrEnum):
    RECAPTCHA = "recaptcha"

    def __str__(self) -> str:
        return str(self.value)
