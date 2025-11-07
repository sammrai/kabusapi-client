from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WalletOptionSuccess")


@_attrs_define
class WalletOptionSuccess:
    """
    Attributes:
        option_buy_trade_limit (float | Unset): 買新規建玉可能額
        option_sell_trade_limit (float | Unset): 売新規建玉可能額
        margin_requirement (float | Unset): 必要証拠金額<br>※銘柄指定の場合のみ。<br>※銘柄が指定されなかった場合、空を返す。
    """

    option_buy_trade_limit: float | Unset = UNSET
    option_sell_trade_limit: float | Unset = UNSET
    margin_requirement: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option_buy_trade_limit = self.option_buy_trade_limit

        option_sell_trade_limit = self.option_sell_trade_limit

        margin_requirement = self.margin_requirement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if option_buy_trade_limit is not UNSET:
            field_dict["OptionBuyTradeLimit"] = option_buy_trade_limit
        if option_sell_trade_limit is not UNSET:
            field_dict["OptionSellTradeLimit"] = option_sell_trade_limit
        if margin_requirement is not UNSET:
            field_dict["MarginRequirement"] = margin_requirement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option_buy_trade_limit = d.pop("OptionBuyTradeLimit", UNSET)

        option_sell_trade_limit = d.pop("OptionSellTradeLimit", UNSET)

        margin_requirement = d.pop("MarginRequirement", UNSET)

        wallet_option_success = cls(
            option_buy_trade_limit=option_buy_trade_limit,
            option_sell_trade_limit=option_sell_trade_limit,
            margin_requirement=margin_requirement,
        )

        wallet_option_success.additional_properties = d
        return wallet_option_success

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
