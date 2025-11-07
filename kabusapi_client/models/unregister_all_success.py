from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unregister_all_success_regist_list import UnregisterAllSuccessRegistList


T = TypeVar("T", bound="UnregisterAllSuccess")


@_attrs_define
class UnregisterAllSuccess:
    """
    Attributes:
        regist_list (UnregisterAllSuccessRegistList | Unset):
            現在登録されている銘柄のリスト<br>※銘柄登録解除が正常に行われれば、空リストを返します。<br>　登録解除でエラー等が発生した場合、現在登録されている銘柄のリストを返します
    """

    regist_list: UnregisterAllSuccessRegistList | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regist_list: dict[str, Any] | Unset = UNSET
        if not isinstance(self.regist_list, Unset):
            regist_list = self.regist_list.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regist_list is not UNSET:
            field_dict["RegistList"] = regist_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unregister_all_success_regist_list import UnregisterAllSuccessRegistList

        d = dict(src_dict)
        _regist_list = d.pop("RegistList", UNSET)
        regist_list: UnregisterAllSuccessRegistList | Unset
        if isinstance(_regist_list, Unset):
            regist_list = UNSET
        else:
            regist_list = UnregisterAllSuccessRegistList.from_dict(_regist_list)

        unregister_all_success = cls(
            regist_list=regist_list,
        )

        unregister_all_success.additional_properties = d
        return unregister_all_success

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
