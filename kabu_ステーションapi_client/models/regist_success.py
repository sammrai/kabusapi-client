from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.regist_success_regist_list_item import RegistSuccessRegistListItem


T = TypeVar("T", bound="RegistSuccess")


@_attrs_define
class RegistSuccess:
    """
    Attributes:
        regist_list (list[RegistSuccessRegistListItem] | Unset): 現在登録されている銘柄のリスト
    """

    regist_list: list[RegistSuccessRegistListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regist_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.regist_list, Unset):
            regist_list = []
            for regist_list_item_data in self.regist_list:
                regist_list_item = regist_list_item_data.to_dict()
                regist_list.append(regist_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regist_list is not UNSET:
            field_dict["RegistList"] = regist_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.regist_success_regist_list_item import RegistSuccessRegistListItem

        d = dict(src_dict)
        _regist_list = d.pop("RegistList", UNSET)
        regist_list: list[RegistSuccessRegistListItem] | Unset = UNSET
        if _regist_list is not UNSET:
            regist_list = []
            for regist_list_item_data in _regist_list:
                regist_list_item = RegistSuccessRegistListItem.from_dict(regist_list_item_data)

                regist_list.append(regist_list_item)

        regist_success = cls(
            regist_list=regist_list,
        )

        regist_success.additional_properties = d
        return regist_success

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
