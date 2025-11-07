from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WalletMarginSuccess")


@_attrs_define
class WalletMarginSuccess:
    """
    Attributes:
        margin_account_wallet (float | Unset): 信用新規可能額
        depositkeep_rate (float | Unset): 保証金維持率<br>※銘柄指定の場合のみ<br>※銘柄が指定されなかった場合、0.0を返す。
        consignment_deposit_rate (float | Unset): 委託保証金率<br>※銘柄指定の場合のみ。<br>※銘柄が指定されなかった場合、Noneを返す。
        cash_of_consignment_deposit_rate (float | Unset): 現金委託保証金率<br>※銘柄指定の場合のみ。<br>※銘柄が指定されなかった場合、Noneを返す。
    """

    margin_account_wallet: float | Unset = UNSET
    depositkeep_rate: float | Unset = UNSET
    consignment_deposit_rate: float | Unset = UNSET
    cash_of_consignment_deposit_rate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        margin_account_wallet = self.margin_account_wallet

        depositkeep_rate = self.depositkeep_rate

        consignment_deposit_rate = self.consignment_deposit_rate

        cash_of_consignment_deposit_rate = self.cash_of_consignment_deposit_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if margin_account_wallet is not UNSET:
            field_dict["MarginAccountWallet"] = margin_account_wallet
        if depositkeep_rate is not UNSET:
            field_dict["DepositkeepRate"] = depositkeep_rate
        if consignment_deposit_rate is not UNSET:
            field_dict["ConsignmentDepositRate"] = consignment_deposit_rate
        if cash_of_consignment_deposit_rate is not UNSET:
            field_dict["CashOfConsignmentDepositRate"] = cash_of_consignment_deposit_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        margin_account_wallet = d.pop("MarginAccountWallet", UNSET)

        depositkeep_rate = d.pop("DepositkeepRate", UNSET)

        consignment_deposit_rate = d.pop("ConsignmentDepositRate", UNSET)

        cash_of_consignment_deposit_rate = d.pop("CashOfConsignmentDepositRate", UNSET)

        wallet_margin_success = cls(
            margin_account_wallet=margin_account_wallet,
            depositkeep_rate=depositkeep_rate,
            consignment_deposit_rate=consignment_deposit_rate,
            cash_of_consignment_deposit_rate=cash_of_consignment_deposit_rate,
        )

        wallet_margin_success.additional_properties = d
        return wallet_margin_success

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
