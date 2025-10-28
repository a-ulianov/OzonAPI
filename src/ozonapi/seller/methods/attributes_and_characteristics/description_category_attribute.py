from ...core import APIManager
from ...schemas.attributes_and_characteristics import DescriptionCategoryAttributeRequest, \
    DescriptionCategoryAttributeResponse


class DescriptionCategoryAttributeMixin(APIManager):
    """Реализует метод /v1/description-category/attribute"""

    async def description_category_attribute(
        self: "DescriptionCategoryAttributeMixin",
        request: DescriptionCategoryAttributeRequest,
    ) -> DescriptionCategoryAttributeResponse:
        """Получение характеристик для указанных категории и типа товара.
        Если у `dictionary_id` значение `0`, у атрибута нет вложенных справочников. Если значение другое, то справочники есть.
        Запросите их методом `description_category_attribute_values()`.

        Notes:
            • `attribute_id` - Идентификатор характеристики, можно получить с помощью метода `description_category_attribute()`
            • `description_category_id` - Идентификатор категории, можно получить с помощью метода `description_category_tree()`
            • `type_id` - Идентификатор типа товара, можно получить с помощью метода `description_category_tree()`

        References:
            https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetAttributes

        Args:
            request: Запрос к серверу gо схеме `DescriptionCategoryAttributeRequest`

        Returns:
            Характеристики для указанных категории и типа товара по схеме `DescriptionCategoryAttributeResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                description_category_attribute = await api.description_category_attribute(
                    DescriptionCategoryAttributeRequest(
                        description_category_id=200000933,
                        type_id=93080,
                        language=Language.DEFAULT,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="description-category/attribute",
            payload=request.model_dump(),
        )
        return DescriptionCategoryAttributeResponse(**response)
