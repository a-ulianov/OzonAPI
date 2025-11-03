from ...core import APIManager
from ...schemas.fbs_assembly_and_labeling import PostingFBSShipRequest, PostingFBSShipResponse


class PostingFBSShipMixin(APIManager):
    """Реализует метод /v4/posting/fbs/ship"""

    async def posting_fbs_ship(
            self: "PostingFBSShipMixin",
            request: PostingFBSShipRequest
    ) -> PostingFBSShipResponse:
        """Метод для деления заказа на отправления и перевода его в статус `awaiting_deliver`.

        Notes:
            • Метод делит заказ на отправления и переводит его в статус `awaiting_deliver`.
            • Каждый элемент в `packages` может содержать несколько элементов `products` или отправлений.
            • Каждый элемент в `products` — это товар, включённый в данное отправление.
            • Разделить заказ нужно если:
              - товары не помещаются в одну упаковку;
              - товары нельзя сложить в одну упаковку.
            • Чтобы разделить заказ, передайте в массиве `packages` несколько объектов.
            • Ответ с кодом 200 не гарантирует успешную сборку заказа. Используйте метод `posting_fbs_get()`,
              чтобы проверить, что заказ собран.
            • Если в ответе метода `posting_fbs_get()` указан `result.substatus = PostingSubstatus.SHIP_FAILED`,
              повторите сборку заказа.
            • Чтобы внести информацию по экземплярам, используйте метод `fbs_posting_product_exemplar_set()`.
            • Для получения дополнительной информации об отправлениях установите `with_.additional_data = True`.

        References:
            https://docs.ozon.com/api/seller/?#operation/PostingAPI_ShipFbsPostingV4

        Args:
            request: Запрос на деление заказа на отправления по схеме `PostingFBSShipRequest`

        Returns:
            Ответ с результатом сборки отправлений по схеме `PostingFBSShipResponse`

        Examples:
            Пример без разделения заказа:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.posting_fbs_ship(
                        PostingFBSShipRequest(
                            posting_number="89491381-0072-1",
                            packages=[
                                PostingFBSShipProducts(
                                    products=[
                                        PostingFBSShipProduct(
                                            product_id=185479045,
                                            quantity=2
                                        )
                                    ]
                                )
                            ]
                        )
                    )

            Пример с разделением заказа:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.posting_fbs_ship(
                        PostingFBSShipRequest(
                            posting_number="89491381-0072-1",
                            packages=[
                                PostingFBSShipProducts(
                                    products=[
                                        PostingFBSShipProduct(
                                            product_id=185479045,
                                            quantity=1
                                        )
                                    ]
                                ),
                                PostingFBSShipProducts(
                                    products=[
                                        PostingFBSShipProduct(
                                            product_id=185479045,
                                            quantity=1
                                        )
                                    ]
                                )
                            ],
                            _with=PostingFBSShipRequestWith(additional_data=True)
                        )
                    )
        """
        response = await self._request(
            method="post",
            api_version="v4",
            endpoint="posting/fbs/ship",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBSShipResponse(**response)