from ...core import APIManager
from ...schemas.fbs import PostingFBSProductCountrySetRequest, PostingFBSProductCountrySetResponse


class PostingFBSProductCountrySetMixin(APIManager):
    """Реализует метод /v2/posting/fbs/product/country/set"""

    async def posting_fbs_product_country_set(
            self: "PostingFBSProductCountrySetMixin",
            request: PostingFBSProductCountrySetRequest
    ) -> PostingFBSProductCountrySetResponse:
        """Метод для добавления информации о стране-изготовителе товара в отправлении FBS.

        Notes:
            • Метод используется для добавления атрибута «Страна-изготовитель» к товару в отправлении, если он не был указан ранее.
            • Страна-изготовитель указывается в формате двухбуквенного кода стандарта ISO 3166-1 (Alpha-2).
            • Список доступных стран-изготовителей и их ISO кодов можно получить с помощью метода posting_fbs_product_country_list().
            • После успешного выполнения метода система возвращает признак необходимости передачи номера ГТД (грузовой таможенной декларации).
            • Если is_gtd_needed = true, необходимо передать номер ГТД для указанного продукта и отправления.
            • Метод может быть применен только к отправлениям, где страна-изготовитель еще не указана.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PostingAPI_SetCountryProductFbsPostingV2

        Args:
            request: Запрос на добавление информации о стране-изготовителе товара по схеме `PostingFBSProductCountrySetRequest`

        Returns:
            Результат выполнения операции с информацией о необходимости ГТД по схеме `PostingFBSProductCountrySetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_product_country_set(
                    PostingFBSProductCountrySetRequest(
                        posting_number="57195475-0050-3",
                        product_id=180550365,
                        country_iso_code="NO"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/product/country/set",
            payload=request.model_dump()
        )
        return PostingFBSProductCountrySetResponse(**response)
