from enum import Enum


class PostApiPaymentsCreateCheckoutLinkType(str, Enum):
    ONE_TIME = "one-time"
    SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
