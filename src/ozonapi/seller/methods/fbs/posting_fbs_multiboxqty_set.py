from ...core import APIManager
from ...schemas.fbs import PostingFBSMultiBoxQtySetRequest, PostingFBSMultiBoxQtySetResponse


class PostingFBSMultiBoxQtySetMixin(APIManager):
    """Реализует метод /v3/posting/multiboxqty/set"""

    async def posting_fbs_multiboxqty_set(
            self: "PostingFBSMultiBoxQtySetMixin",
            request: PostingFBSMultiBoxQtySetRequest
    ) -> PostingFBSMultiBoxQtySetResponse:
        """Метод для передачи количества коробок для отправлений, в которых есть многокоробочные товары.

        Notes:
            • Метод используется при работе по схеме rFBS Агрегатор — с доставкой партнёрами Ozon.
            • Используется только для многокоробочных отправлений, где товары упакованы в несколько коробок.
            • Количество коробок должно быть целым положительным числом.
            • После успешного выполнения метода система учитывает указанное количество коробок при дальнейшей обработке отправления.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/PostingAPI_PostingMultiBoxQtySetV3

        Args:
            request: Запрос на указание количества коробок для многокоробочного отправления по схеме `PostingFBSMultiBoxQtySetRequest`

        Returns:
            Результат выполнения операции по схеме `PostingFBSMultiBoxQtySetResponse`

        Examples:
            Пример с проверкой результата:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.posting_multiboxqty_set(
                        PostingFBSMultiBoxQtySetRequest(
                            posting_number="57195475-0050-3",
                            multi_box_qty=3
                        )
                    )

                    if result.result.result:
                        print("Количество коробок успешно передано")
                    else:
                        print("Произошла ошибка при указании количества коробок")
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="posting/multi-box-qty/set",
            payload=request.model_dump()
        )
        return PostingFBSMultiBoxQtySetResponse(**response)
