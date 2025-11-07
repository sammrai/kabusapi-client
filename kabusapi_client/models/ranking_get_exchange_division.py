from enum import Enum


class RankingGetExchangeDivision(str, Enum):
    ALL = "ALL"
    FK = "FK"
    M = "M"
    S = "S"
    T = "T"
    TG = "TG"
    TP = "TP"
    TS = "TS"

    def __str__(self) -> str:
        return str(self.value)
