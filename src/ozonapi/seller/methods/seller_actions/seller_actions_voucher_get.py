from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsVoucherGetRequest,
    SellerActionsVoucherGetResponse,
)


class SellerActionsVoucherGetMixin(APIManager):
    """Реализует метод /v1/seller-actions/voucher/get"""

    async def seller_actions_voucher_get(
            self: "SellerActionsVoucherGetMixin",
            request: SellerActionsVoucherGetRequest,
    ) -> SellerActionsVoucherGetResponse:
        """Получает файл с промокодами акции «Скидка по промокоду» в формате CSV.

        Notes:
            • В ответе возвращается ссылка `file` на CSV-файл с промокодами.
            • Метод применим только к акциям с механикой «Скидка по промокоду».

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsVoucherGet

        Args:
            request: Идентификатор акции по схеме `SellerActionsVoucherGetRequest`

        Returns:
            Ссылка на CSV-файл с промокодами по схеме `SellerActionsVoucherGetResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.seller_actions_voucher_get(
                    SellerActionsVoucherGetRequest(action_id=123456)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/voucher/get",
            payload=request.model_dump(),
        )
        return SellerActionsVoucherGetResponse(**response)
