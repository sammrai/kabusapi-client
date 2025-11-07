from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.regulations_response_regulations_info_item import RegulationsResponseRegulationsInfoItem


T = TypeVar("T", bound="RegulationsResponse")


@_attrs_define
class RegulationsResponse:
    """
    Example:
        {'Symbol': '5614', 'RegulationsInfo': [{'Exchange': 1, 'Product': 8, 'Side': '2', 'Reason':
            '品受停止（貸借申込停止銘柄（日証金規制））', 'LimitStartDay': '2020/10/01 00:00', 'LimitEndDay': '2999/12/31 00:00', 'Level': 2},
            {'Exchange': 0, 'Product': 1, 'Side': '2', 'Reason': 'その他（代用不適格銘柄）', 'LimitStartDay': '2021/01/27 00:00',
            'LimitEndDay': '2021/02/17 00:00', 'Level': 2}]}

    Attributes:
        symbol (str | Unset): 銘柄コード<br>
            ※対象商品は、株式のみ
        regulations_info (list[RegulationsResponseRegulationsInfoItem] | Unset): 規制情報
    """

    symbol: str | Unset = UNSET
    regulations_info: list[RegulationsResponseRegulationsInfoItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        regulations_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.regulations_info, Unset):
            regulations_info = []
            for regulations_info_item_data in self.regulations_info:
                regulations_info_item = regulations_info_item_data.to_dict()
                regulations_info.append(regulations_info_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["Symbol"] = symbol
        if regulations_info is not UNSET:
            field_dict["RegulationsInfo"] = regulations_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.regulations_response_regulations_info_item import RegulationsResponseRegulationsInfoItem

        d = dict(src_dict)
        symbol = d.pop("Symbol", UNSET)

        _regulations_info = d.pop("RegulationsInfo", UNSET)
        regulations_info: list[RegulationsResponseRegulationsInfoItem] | Unset = UNSET
        if _regulations_info is not UNSET:
            regulations_info = []
            for regulations_info_item_data in _regulations_info:
                regulations_info_item = RegulationsResponseRegulationsInfoItem.from_dict(regulations_info_item_data)

                regulations_info.append(regulations_info_item)

        regulations_response = cls(
            symbol=symbol,
            regulations_info=regulations_info,
        )

        regulations_response.additional_properties = d
        return regulations_response

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
