from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegulationsResponseRegulationsInfoItem")


@_attrs_define
class RegulationsResponseRegulationsInfoItem:
    """
    Attributes:
        exchange (int | Unset): 規制市場
            <table>
              <thead>
                <tr>
                  <th>定義値</th>
                  <th>内容</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>0</td>
                  <td>全対象</td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>東証</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>名証</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>福証</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>札証</td>
                </tr>
                <tr>
                  <td>9</td>
                  <td>SOR</td>
                </tr>
                <tr>
                  <td>10</td>
                  <td>CXJ</td>
                </tr>
                <tr>
                  <td>21</td>
                  <td>JNX</td>
                </tr>
              </tbody>
            </table>
        product (int | Unset): 規制取引区分<br>
            ※空売り規制の場合、「4：新規」
            <table>
              <thead>
                <tr>
                  <th>定義値</th>
                  <th>内容</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>0</td>
                  <td>全対象</td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>現物</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>信用新規（制度）</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>信用新規（一般）</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>新規</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>信用返済（制度）</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>信用返済（一般）</td>
                </tr>
                <tr>
                  <td>7</td>
                  <td>返済</td>
                </tr>
                <tr>
                  <td>8</td>
                  <td>品受</td>
                </tr>
                <tr>
                  <td>9</td>
                  <td>品渡</td>
                </tr>
              </tbody>
            </table>
        side (str | Unset): 規制売買<br>
            ※空売り規制の場合、「1：売」
            <table>
              <thead>
                <tr>
                  <th>定義値</th>
                  <th>内容</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>0</td>
                  <td>全対象</td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>売</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>買</td>
                </tr>
              </tbody>
            </table>
        reason (str | Unset): 理由<br>※空売り規制の場合、「空売り規制」
        limit_start_day (str | Unset): 制限開始日<br>yyyy/MM/dd HH:mm形式  <br>※空売り規制の場合、null
        limit_end_day (str | Unset): 制限終了日<br>yyyy/MM/dd HH:mm形式  <br>※空売り規制の場合、null
        level (int | Unset): コンプライアンスレベル<br>
            ※空売り規制の場合、null
            <table>
              <thead>
                <tr>
                  <th>定義値</th>
                  <th>内容</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>０</td>
                  <td>規制無し</td>
                </tr>
                <tr>
                  <td>１</td>
                  <td>ワーニング</td>
                </tr>
                <tr>
                  <td>２</td>
                  <td>エラー</td>
                </tr>
              </tbody>
            </table>
    """

    exchange: int | Unset = UNSET
    product: int | Unset = UNSET
    side: str | Unset = UNSET
    reason: str | Unset = UNSET
    limit_start_day: str | Unset = UNSET
    limit_end_day: str | Unset = UNSET
    level: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange = self.exchange

        product = self.product

        side = self.side

        reason = self.reason

        limit_start_day = self.limit_start_day

        limit_end_day = self.limit_end_day

        level = self.level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange is not UNSET:
            field_dict["Exchange"] = exchange
        if product is not UNSET:
            field_dict["Product"] = product
        if side is not UNSET:
            field_dict["Side"] = side
        if reason is not UNSET:
            field_dict["Reason"] = reason
        if limit_start_day is not UNSET:
            field_dict["LimitStartDay"] = limit_start_day
        if limit_end_day is not UNSET:
            field_dict["LimitEndDay"] = limit_end_day
        if level is not UNSET:
            field_dict["Level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange = d.pop("Exchange", UNSET)

        product = d.pop("Product", UNSET)

        side = d.pop("Side", UNSET)

        reason = d.pop("Reason", UNSET)

        limit_start_day = d.pop("LimitStartDay", UNSET)

        limit_end_day = d.pop("LimitEndDay", UNSET)

        level = d.pop("Level", UNSET)

        regulations_response_regulations_info_item = cls(
            exchange=exchange,
            product=product,
            side=side,
            reason=reason,
            limit_start_day=limit_start_day,
            limit_end_day=limit_end_day,
            level=level,
        )

        regulations_response_regulations_info_item.additional_properties = d
        return regulations_response_regulations_info_item

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
