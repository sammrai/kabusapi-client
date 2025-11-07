from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderSuccess")


@_attrs_define
class OrderSuccess:
    """
    Attributes:
        result (int | Unset): 結果コード<br>0が成功。それ以外はエラーコード。
        order_id (str | Unset): 受付注文番号 Example: 20200529A01N06848002.
    """

    result: int | Unset = UNSET
    order_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result = self.result

        order_id = self.order_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["Result"] = result
        if order_id is not UNSET:
            field_dict["OrderId"] = order_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        result = d.pop("Result", UNSET)

        order_id = d.pop("OrderId", UNSET)

        order_success = cls(
            result=result,
            order_id=order_id,
        )

        order_success.additional_properties = d
        return order_success

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
