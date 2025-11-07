from enum import Enum


class OrdersGetCashmargin(str, Enum):
    VALUE_0 = "2"
    VALUE_1 = "3"

    def __str__(self) -> str:
        return str(self.value)
