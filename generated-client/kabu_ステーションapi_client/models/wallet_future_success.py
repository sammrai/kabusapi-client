from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WalletFutureSuccess")


@_attrs_define
class WalletFutureSuccess:
    """
    Attributes:
        future_trade_limit (float | Unset): 新規建玉可能額
        margin_requirement (float | Unset): 買い必要証拠金額<br>※銘柄指定の場合のみ。<br>※銘柄が指定されなかった場合、空を返す。
        margin_requirement_sell (float | Unset): 売り必要証拠金額<br>※銘柄指定の場合のみ。<br>※銘柄が指定されなかった場合、空を返す。
    """

    future_trade_limit: float | Unset = UNSET
    margin_requirement: float | Unset = UNSET
    margin_requirement_sell: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        future_trade_limit = self.future_trade_limit

        margin_requirement = self.margin_requirement

        margin_requirement_sell = self.margin_requirement_sell

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if future_trade_limit is not UNSET:
            field_dict["FutureTradeLimit"] = future_trade_limit
        if margin_requirement is not UNSET:
            field_dict["MarginRequirement"] = margin_requirement
        if margin_requirement_sell is not UNSET:
            field_dict["MarginRequirementSell"] = margin_requirement_sell

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        future_trade_limit = d.pop("FutureTradeLimit", UNSET)

        margin_requirement = d.pop("MarginRequirement", UNSET)

        margin_requirement_sell = d.pop("MarginRequirementSell", UNSET)

        wallet_future_success = cls(
            future_trade_limit=future_trade_limit,
            margin_requirement=margin_requirement,
            margin_requirement_sell=margin_requirement_sell,
        )

        wallet_future_success.additional_properties = d
        return wallet_future_success

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
