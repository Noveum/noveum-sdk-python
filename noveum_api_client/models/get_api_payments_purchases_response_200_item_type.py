from enum import Enum


class GetApiPaymentsPurchasesResponse200ItemType(str, Enum):
    ONE_TIME = "ONE_TIME"
    SUBSCRIPTION = "SUBSCRIPTION"

    def __str__(self) -> str:
        return str(self.value)
