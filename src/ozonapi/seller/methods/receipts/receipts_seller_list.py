from ...core import APIManager
from ...schemas.receipts import (
    ReceiptsSellerListRequest,
    ReceiptsSellerListResponse,
)


class ReceiptsSellerListMixin(APIManager):
    """Реализует метод /v1/receipts/seller/list"""

    async def receipts_seller_list(
            self: "ReceiptsSellerListMixin",
            request: ReceiptsSellerListRequest = ReceiptsSellerListRequest()
    ) -> ReceiptsSellerListResponse:
        """Возвращает список чеков продавца с постраничной навигацией.

        Notes:
            • Постраничная навигация задаётся полями `page` и `page_size`;
              признак наличия следующей страницы — `has_next`.
            • Можно отфильтровать чеки по номерам отправлений `posting_numbers`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReceiptsSellerList

        Args:
            request: Запрос списка чеков по схеме `ReceiptsSellerListRequest`

        Returns:
            Список чеков продавца по схеме `ReceiptsSellerListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.receipts_seller_list(
                    ReceiptsSellerListRequest(page=1, page_size=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="receipts/seller/list",
            payload=request.model_dump()
        )
        return ReceiptsSellerListResponse(**response)
