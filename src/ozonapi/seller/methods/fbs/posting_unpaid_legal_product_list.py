from ...core import APIManager
from ...schemas.fbs import (
    PostingUnpaidLegalProductListRequest,
    PostingUnpaidLegalProductListResponse,
)


class PostingUnpaidLegalProductListMixin(APIManager):
    """Реализует метод /v1/posting/unpaid-legal/product/list"""

    async def posting_unpaid_legal_product_list(
            self: "PostingUnpaidLegalProductListMixin",
            request: PostingUnpaidLegalProductListRequest = PostingUnpaidLegalProductListRequest()
    ) -> PostingUnpaidLegalProductListResponse:
        """Возвращает список неоплаченных товаров, заказанных юридическими лицами.

        Notes:
            • Курсорная пагинация: передайте полученный `cursor` в следующий запрос.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_UnpaidLegalProductList

        Args:
            request: Запрос по схеме `PostingUnpaidLegalProductListRequest` (cursor, limit)

        Returns:
            Список неоплаченных товаров по схеме `PostingUnpaidLegalProductListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_unpaid_legal_product_list(
                    PostingUnpaidLegalProductListRequest(limit=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/unpaid-legal/product/list",
            payload=request.model_dump(by_alias=True)
        )
        return PostingUnpaidLegalProductListResponse(**response)
