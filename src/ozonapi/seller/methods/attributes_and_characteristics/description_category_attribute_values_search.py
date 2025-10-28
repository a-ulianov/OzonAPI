from ...core import APIManager
from ...schemas.attributes_and_characteristics import DescriptionCategoryAttributeValuesSearchRequest, \
    DescriptionCategoryAttributeValuesSearchResponse


class DescriptionCategoryAttributeValuesSearchMixin(APIManager):
    """Реализует метод /v1/description-category/attribute/values/search"""

    async def description_category_attribute_values_search(
        self: "DescriptionCategoryAttributeValuesSearchMixin",
        request: DescriptionCategoryAttributeValuesSearchRequest,
    ) -> DescriptionCategoryAttributeValuesSearchResponse:
        """Возвращает справочные значения характеристики по заданному значению value в запросе.
        Узнать, есть ли вложенный справочник, можно через метод `description_category_attribute()`.

        Notes:
            • `attribute_id` - Идентификатор характеристики, можно получить с помощью метода `description_category_attribute()`
            • `description_category_id` - Идентификатор категории, можно получить с помощью метода `description_category_tree()`
            • `type_id` - Идентификатор типа товара, можно получить с помощью метода `description_category_tree()`
            • `value` - Поисковый запрос (минимум 2 символа)

        References:
            https://docs.ozon.ru/api/seller/?__rr=2&abt_att=1#operation/DescriptionCategoryAPI_SearchAttributeValues

        Args:
            request: Запрос к серверу по схеме `DescriptionCategoryAttributeValuesSearchRequest`

        Returns:
            Справочные значения характеристики по заданному значению value в запросе по схеме `DescriptionCategoryAttributeValuesSearchResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                description_category_attribute_values = await api.description_category_attribute_values_search(
                    DescriptionCategoryAttributeValuesSearchRequest(
                        attribute_id=85,
                        description_category_id=17054869,
                        limit=100,
                        type_id=97311,
                        value="Красота"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="description-category/attribute/values/search",
            payload=request.model_dump(),
        )
        return DescriptionCategoryAttributeValuesSearchResponse(**response)