from enum import Enum


class ExchangeGetSymbol(str, Enum):
    AUDJPY = "audjpy"
    AUDUSD = "audusd"
    CADJPY = "cadjpy"
    CHFJPY = "chfjpy"
    EURJPY = "eurjpy"
    EURUSD = "eurusd"
    GBPJPY = "gbpjpy"
    GBPUSD = "gbpusd"
    NZDJPY = "nzdjpy"
    USDJPY = "usdjpy"
    ZARJPY = "zarjpy"

    def __str__(self) -> str:
        return str(self.value)
