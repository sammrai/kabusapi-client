from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BoardSuccessSell5")


@_attrs_define
class BoardSuccessSell5:
    """売気配数量5本目

    Attributes:
        price (float | Unset): 値段<br>※株式・先物・オプション銘柄の場合のみ
        qty (float | Unset): 数量<br>※株式・先物・オプション銘柄の場合のみ
    """

    price: float | Unset = UNSET
    qty: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        qty = self.qty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price is not UNSET:
            field_dict["Price"] = price
        if qty is not UNSET:
            field_dict["Qty"] = qty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("Price", UNSET)

        qty = d.pop("Qty", UNSET)

        board_success_sell_5 = cls(
            price=price,
            qty=qty,
        )

        board_success_sell_5.additional_properties = d
        return board_success_sell_5

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
