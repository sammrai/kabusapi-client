from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSoftLimitResponse")


@_attrs_define
class ApiSoftLimitResponse:
    """
    Example:
        {'Stock': 200, 'Margin': 200, 'Future': 10, 'FutureMini': 100, 'FutureMicro': 1000, 'Option': 20, 'MiniOption':
            200, 'KabuSVersion': '5.13.1.0'}

    Attributes:
        stock (float | Unset): 現物のワンショット上限<br>※単位は万円
        margin (float | Unset): 信用のワンショット上限<br>※単位は万円
        future (float | Unset): 先物のワンショット上限<br>※単位は枚
        future_mini (float | Unset): ミニ先物のワンショット上限<br>※単位は枚
        future_micro (float | Unset): マイクロ先物のワンショット上限<br>※単位は枚
        option (float | Unset): オプションのワンショット上限<br>※単位は枚
        mini_option (float | Unset): ミニオプションのワンショット上限<br>※単位は枚
        kabu_s_version (str | Unset): kabuステーションのバージョン
    """

    stock: float | Unset = UNSET
    margin: float | Unset = UNSET
    future: float | Unset = UNSET
    future_mini: float | Unset = UNSET
    future_micro: float | Unset = UNSET
    option: float | Unset = UNSET
    mini_option: float | Unset = UNSET
    kabu_s_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stock = self.stock

        margin = self.margin

        future = self.future

        future_mini = self.future_mini

        future_micro = self.future_micro

        option = self.option

        mini_option = self.mini_option

        kabu_s_version = self.kabu_s_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stock is not UNSET:
            field_dict["Stock"] = stock
        if margin is not UNSET:
            field_dict["Margin"] = margin
        if future is not UNSET:
            field_dict["Future"] = future
        if future_mini is not UNSET:
            field_dict["FutureMini"] = future_mini
        if future_micro is not UNSET:
            field_dict["FutureMicro"] = future_micro
        if option is not UNSET:
            field_dict["Option"] = option
        if mini_option is not UNSET:
            field_dict["MiniOption"] = mini_option
        if kabu_s_version is not UNSET:
            field_dict["KabuSVersion"] = kabu_s_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stock = d.pop("Stock", UNSET)

        margin = d.pop("Margin", UNSET)

        future = d.pop("Future", UNSET)

        future_mini = d.pop("FutureMini", UNSET)

        future_micro = d.pop("FutureMicro", UNSET)

        option = d.pop("Option", UNSET)

        mini_option = d.pop("MiniOption", UNSET)

        kabu_s_version = d.pop("KabuSVersion", UNSET)

        api_soft_limit_response = cls(
            stock=stock,
            margin=margin,
            future=future,
            future_mini=future_mini,
            future_micro=future_micro,
            option=option,
            mini_option=mini_option,
            kabu_s_version=kabu_s_version,
        )

        api_soft_limit_response.additional_properties = d
        return api_soft_limit_response

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
