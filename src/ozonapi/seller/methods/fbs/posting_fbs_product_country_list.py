from async_lru import alru_cache

from ...core import APIManager
from ...core.exceptions import APINotFoundError
from ...schemas.fbs import PostingFBSProductCountryListRequest, PostingFBSProductCountryListResponse


class PostingFBSProductCountryListMixin(APIManager):
    """Реализует метод v2/posting/fbs/product/country/list"""

    @alru_cache(ttl=86400)
    async def posting_fbs_product_country_list(
            self: "PostingFBSProductCountryListMixin",
            request: PostingFBSProductCountryListRequest = PostingFBSProductCountryListRequest.model_construct()
    ) -> PostingFBSProductCountryListResponse:
        """Метод для получения списка доступных стран-изготовителей и их ISO кодов.

        Notes:
            • Метод возвращает полный список стран-изготовителей, доступных для указания в карточках товаров.
            • Для фильтрации результатов можно использовать параметр `name_search` - поисковая строка по названию страны.
            • Если параметр `name_search` не указан или пустой, возвращается полный список всех доступных стран.
            • Поиск осуществляется по частичному совпадению с названием страны на русском языке.
            • Регистр букв в поисковой строке не имеет значения.
            • ISO код страны возвращается в формате двухбуквенного кода (Alpha-2) согласно стандарту ISO 3166-1.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/PostingAPI_ListCountryProductFbsPostingV2

        Args:
            request: Запрос на получение списка стран-изготовителей по схеме `PostingFBSProductCountryListRequest`

        Returns:
            Список доступных стран-изготовителей с их ISO кодами по схеме `PostingFBSProductCountryListResponse`

        Examples:
            Базовое применение (получение полного списка стран):
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.posting_fbs_product_country_list(
                        PostingFBSProductCountryListRequest()
                    )

            Пример с фильтрацией по названию страны (частичное совпадение):
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.posting_fbs_product_country_list(
                        PostingFBSProductCountryListRequest(
                            name_search="тУрЦ"
                        )
                    )
        """
        try:
            response = await self._request(
                method="post",
                api_version="v2",
                endpoint="posting/fbs/product/country/list",
                payload=request.model_dump()
            )
        except APINotFoundError:
            return PostingFBSProductCountryListResponse.model_construct()
        return PostingFBSProductCountryListResponse(**response)
