from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenSuccess")


@_attrs_define
class TokenSuccess:
    """
    Attributes:
        result_code (int | Unset): 結果コード<br>0が成功。それ以外はエラーコード。
        token (str | Unset): APIトークン Example: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
    """

    result_code: int | Unset = UNSET
    token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result_code = self.result_code

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result_code is not UNSET:
            field_dict["ResultCode"] = result_code
        if token is not UNSET:
            field_dict["Token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        result_code = d.pop("ResultCode", UNSET)

        token = d.pop("Token", UNSET)

        token_success = cls(
            result_code=result_code,
            token=token,
        )

        token_success.additional_properties = d
        return token_success

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
