from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WalletCashSuccess")


@_attrs_define
class WalletCashSuccess:
    """
    Attributes:
        stock_account_wallet (float | Unset): 現物買付可能額<br> ※auマネーコネクトが有効の場合、auじぶん銀行の残高を含めた合計可能額を表示する<br>
            ※auマネーコネクトが無効の場合、三菱UFJ eスマート証券の可能額のみを表示する
        au_kc_stock_account_wallet (float | Unset): うち、三菱UFJ eスマート証券可能額
        au_jbn_stock_account_wallet (float | Unset): うち、auじぶん銀行残高<br>※auマネーコネクトが無効の場合、「0」を表示する
    """

    stock_account_wallet: float | Unset = UNSET
    au_kc_stock_account_wallet: float | Unset = UNSET
    au_jbn_stock_account_wallet: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stock_account_wallet = self.stock_account_wallet

        au_kc_stock_account_wallet = self.au_kc_stock_account_wallet

        au_jbn_stock_account_wallet = self.au_jbn_stock_account_wallet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stock_account_wallet is not UNSET:
            field_dict["StockAccountWallet"] = stock_account_wallet
        if au_kc_stock_account_wallet is not UNSET:
            field_dict["AuKCStockAccountWallet"] = au_kc_stock_account_wallet
        if au_jbn_stock_account_wallet is not UNSET:
            field_dict["AuJbnStockAccountWallet"] = au_jbn_stock_account_wallet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stock_account_wallet = d.pop("StockAccountWallet", UNSET)

        au_kc_stock_account_wallet = d.pop("AuKCStockAccountWallet", UNSET)

        au_jbn_stock_account_wallet = d.pop("AuJbnStockAccountWallet", UNSET)

        wallet_cash_success = cls(
            stock_account_wallet=stock_account_wallet,
            au_kc_stock_account_wallet=au_kc_stock_account_wallet,
            au_jbn_stock_account_wallet=au_jbn_stock_account_wallet,
        )

        wallet_cash_success.additional_properties = d
        return wallet_cash_success

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
