from enum import StrEnum


class ExportedNestEggConfigFilesAdditionalPropertyParser(StrEnum):
    FILE = "file"
    INI = "ini"
    JSON = "json"
    PROPERTIES = "properties"
    TOML = "toml"
    XML = "xml"
    YAML = "yaml"

    def __str__(self) -> str:
        return str(self.value)
