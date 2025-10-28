from ...core import APIManager
from ...schemas.attributes_and_characteristics import DescriptionCategoryAttributeValuesRequest, \
    DescriptionCategoryAttributeValuesResponse


class DescriptionCategoryAttributeValuesMixin(APIManager):
    """Реализует метод /v1/description-category/attribute/values"""

    async def description_category_attribute_values(
        self: "DescriptionCategoryAttributeValuesMixin",
        request: DescriptionCategoryAttributeValuesRequest,
    ) -> DescriptionCategoryAttributeValuesResponse:
        """Возвращает справочник значений характеристики.
        Узнать, есть ли вложенный справочник, можно через метод `description_category_attribute()`.

        Notes:
            • `attribute_id` - Идентификатор характеристики, можно получить с помощью метода `description_category_attribute()`
            • `description_category_id` - Идентификатор категории, можно получить с помощью метода `description_category_tree()`
            • `type_id` - Идентификатор типа товара, можно получить с помощью метода `description_category_tree()`
            • Для пагинации используйте значение `last_value_id`

        References:
            https://docs.ozon.ru/api/seller/?__rr=2&abt_att=1#operation/DescriptionCategoryAPI_GetAttributeValues

        Args:
            request: Запрос к серверу по схеме `DescriptionCategoryAttributeValuesRequest`

        Returns:
            Cправочник значений характеристики по схеме `DescriptionCategoryAttributeValuesResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                description_category_attribute_values = await api.description_category_attribute_values(
                    DescriptionCategoryAttributeValuesRequest(
                        attribute_id=85,
                        description_category_id=17054869,
                        language=Language.DEFAULT,
                        last_value_id=0,
                        limit=100,
                        type_id=97311
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="description-category/attribute/values",
            payload=request.model_dump(),
        )
        return DescriptionCategoryAttributeValuesResponse(**response)
