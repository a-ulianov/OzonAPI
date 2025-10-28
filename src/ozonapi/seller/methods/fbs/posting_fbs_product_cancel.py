from ...core import APIManager
from ...schemas.fbs import PostingFBSProductCancelRequest, PostingFBSProductCancelResponse


class PostingFBSProductCancelMixin(APIManager):
    """Реализует метод /v2/posting/fbs/product/cancel"""

    async def posting_fbs_product_cancel(
            self: "PostingFBSProductCancelMixin",
            request: PostingFBSProductCancelRequest
    ) -> PostingFBSProductCancelResponse:
        """Метод для отмены отправки некоторых товаров в отправлении.

        Notes:
            • Используйте метод, если вы не можете отправить часть продуктов из отправления.
            • Чтобы получить идентификаторы причин отмены `cancel_reason_id` при работе по схемам FBS или rFBS,
              используйте метод `posting_fbs_cancel_reason_list()`.
            • Условно-доставленные отправления отменить нельзя.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_CancelFbsPostingProduct

        Args:
            request: Запрос на отмену отправки товаров в отправлении по схеме `PostingFBSProductCancelRequest`

        Returns:
            Результат отмены с номером отправления по схеме `PostingFBSProductCancelResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_product_cancel(
                    PostingFBSProductCancelRequest(
                        cancel_reason_id=352,
                        cancel_reason_message="Product is out of stock",
                        items=[
                            PostingFBSProductCancelItem(
                                quantity=5,
                                sku=150587396
                            )
                        ],
                        posting_number="33920113-1231-1"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/product/cancel",
            payload=request.model_dump()
        )
        return PostingFBSProductCancelResponse(**response)