from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarginPremiumResponseDayTrade")


@_attrs_define
class MarginPremiumResponseDayTrade:
    """一般信用（デイトレ）

    Attributes:
        margin_premium_type (int | Unset): プレミアム料入力区分
            <table>
              <thead>
                  <tr>
                      <th>定義値</th>
                      <th>説明</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>null</td>
                      <td>一般信用（デイトレ）非対応銘柄</td>
                  </tr>
                  <tr>
                      <td>0</td>
                      <td>プレミアム料がない銘柄</td>
                  </tr>
                  <tr>
                      <td>1</td>
                      <td>プレミアム料が固定の銘柄</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>プレミアム料が入札で決定する銘柄</td>
                  </tr>
              </tbody>
            </table>
        margin_premium (float | Unset): 確定プレミアム料<br>
            ※入札銘柄の場合、入札受付中は随時更新します。受付時間外は、確定したプレミアム料を返します。<br>
            ※非入札銘柄の場合、常に固定値を返します。<br>
            ※信用取引不可の場合、nullを返します。<br>
            ※19:30~翌営業日のプレミアム料になります。
        upper_margin_premium (float | Unset): 上限プレミアム料<br>
            ※プレミアム料がない場合は、nullを返します。
        lower_margin_premium (float | Unset): 下限プレミアム料<br>
            ※プレミアム料がない場合は、nullを返します。
        tick_margin_premium (float | Unset): プレミアム料刻値<br>
            ※入札可能銘柄以外は、nullを返します。
    """

    margin_premium_type: int | Unset = UNSET
    margin_premium: float | Unset = UNSET
    upper_margin_premium: float | Unset = UNSET
    lower_margin_premium: float | Unset = UNSET
    tick_margin_premium: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        margin_premium_type = self.margin_premium_type

        margin_premium = self.margin_premium

        upper_margin_premium = self.upper_margin_premium

        lower_margin_premium = self.lower_margin_premium

        tick_margin_premium = self.tick_margin_premium

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if margin_premium_type is not UNSET:
            field_dict["MarginPremiumType"] = margin_premium_type
        if margin_premium is not UNSET:
            field_dict["MarginPremium"] = margin_premium
        if upper_margin_premium is not UNSET:
            field_dict["UpperMarginPremium"] = upper_margin_premium
        if lower_margin_premium is not UNSET:
            field_dict["LowerMarginPremium"] = lower_margin_premium
        if tick_margin_premium is not UNSET:
            field_dict["TickMarginPremium"] = tick_margin_premium

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        margin_premium_type = d.pop("MarginPremiumType", UNSET)

        margin_premium = d.pop("MarginPremium", UNSET)

        upper_margin_premium = d.pop("UpperMarginPremium", UNSET)

        lower_margin_premium = d.pop("LowerMarginPremium", UNSET)

        tick_margin_premium = d.pop("TickMarginPremium", UNSET)

        margin_premium_response_day_trade = cls(
            margin_premium_type=margin_premium_type,
            margin_premium=margin_premium,
            upper_margin_premium=upper_margin_premium,
            lower_margin_premium=lower_margin_premium,
            tick_margin_premium=tick_margin_premium,
        )

        margin_premium_response_day_trade.additional_properties = d
        return margin_premium_response_day_trade

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
