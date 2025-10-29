from ...core import APIManager
from ...schemas.fbs_assembly_and_labeling import FBSPostingProductExemplarSetRequest, \
    FBSPostingProductExemplarSetResponse


class FBSPostingProductExemplarSetMixin(APIManager):
    """Реализует метод /v6/fbs/posting/product/exemplar/set"""

    async def fbs_posting_product_exemplar_set(
            self,
            request: FBSPostingProductExemplarSetRequest,
    ) -> FBSPostingProductExemplarSetResponse:
        """Реализует проверку и сохранение информации об экземплярах.

        Notes:
            Описание метода:
                Асинхронный метод для:
                - проверки наличия экземпляров в обороте в системе «Честный ЗНАК»;
                - сохранения данных экземпляров.

                Важные особенности:
                - Код ответа 200 не гарантирует, что данные об экземплярах приняты.
                  Он указывает, что создана задача для добавления информации.
                - Для получения результатов проверок используйте метод `fbs_posting_product_exemplar_status()`.
                - Для получения данных о созданных экземплярах используйте метод
                  `fbs_posting_product_exemplar_create_or_get()`.
                - Если у вас несколько одинаковых товаров в отправлении, укажите один `product_id`
                  и массив `exemplars` для каждого товара из отправления.
                - Всегда передавайте полный набор данных по экземплярам и продуктам.

        References:
            https://docs.ozon.com/api/seller/?__rr=1#operation/PostingAPI_FbsPostingProductExemplarSetV6

        Args:
            request: Объект запроса с данными экземпляров по схеме `FBSPostingProductExemplarSetRequest`.

        Returns:
            Ответ API с информацией о результате операции по схеме `FBSPostingProductExemplarSetResponse`.

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbs_posting_product_exemplar_set(
                    FBSPostingProductExemplarSetRequest(
                        posting_number="43658312-0011-1",
                        multi_box_qty=1,
                        products=[
                            FBSPostingProductExemplarSetProduct(
                                product_id=123456789,
                                exemplars=[
                                    FBSPostingProductExemplarSetExemplar(
                                        exemplar_id=1,
                                        gtd="10714440/110922/0012345/1",
                                        is_gtd_absent=False,
                                        is_rnpt_absent=True,
                                        marks=[
                                            FBSPostingProductExemplarSetExemplarMark(
                                                mark="010460406349100021N4O0B5A8B1",
                                                mark_type=MarkType.MANDATORY_MARK,
                                            )
                                        ],
                                        rnpt=None,
                                        weight=1.5,
                                    )
                                ],
                            )
                        ],
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v6",
            endpoint="fbs/posting/product/exemplar/set",
            payload=request.model_dump(by_alias=True)
        )

        return FBSPostingProductExemplarSetResponse(**response)

