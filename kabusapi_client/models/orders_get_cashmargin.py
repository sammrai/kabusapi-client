from enum import StrEnum


class OrdersGetCashmargin(StrEnum):
    VALUE_0 = "2"
    VALUE_1 = "3"

    def __str__(self) -> str:
        return str(self.value)
