from enum import Enum


class PutApiTelemetryPluginsByIdBodyEnvironment(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    STAGING = "staging"

    def __str__(self) -> str:
        return str(self.value)
