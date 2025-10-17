from ..core import APIManager
from ..schemas.attributes_and_characteristics import (
    DescriptionCategoryAttributeResponse,
    DescriptionCategoryTreeResponse,
    DescriptionCategoryTreeRequest,
    DescriptionCategoryAttributeRequest,
    DescriptionCategoryAttributeValuesRequest,
    DescriptionCategoryAttributeValuesResponse,
    DescriptionCategoryAttributeValuesSearchRequest,
    DescriptionCategoryAttributeValuesSearchResponse
)


class SellerCategoryAPI(APIManager):
    """Реализует методы раздела Атрибуты и характеристики Ozon.

    References:
        https://docs.ozon.ru/api/seller/?__rr=1#tag/CategoryAPI
    """

    async def description_category_tree(
        self: "SellerCategoryAPI",
        request: DescriptionCategoryTreeRequest = DescriptionCategoryTreeRequest.model_construct(),
    ) -> DescriptionCategoryTreeResponse:
        """Возвращает категории и типы для товаров в виде дерева.
        Создание товаров доступно только в категориях последнего уровня, сравните именно их с категориями на своей площадке.
        Категории не создаются по запросу пользователя.

        Notes:
            Внимательно выбирайте категорию для товара: для разных категорий применяется разный размер комиссии.

        References:
            https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetTree

        Args:
            request: Запрос к серверу по схеме `DescriptionCategoryTreeRequest`

        Returns:
            Категории и типы для товаров в виде дерева по схеме `DescriptionCategoryTreeResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                description_category_tree = await api.description_category_tree()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="description-category/tree",
            json=request.model_dump()
        )
        return DescriptionCategoryTreeResponse(**response)

    async def description_category_attribute(
        self: "SellerCategoryAPI",
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
            json=request.model_dump(),
        )
        return DescriptionCategoryAttributeResponse(**response)

    async def description_category_attribute_values(
        self: "SellerCategoryAPI",
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
            json=request.model_dump(),
        )
        return DescriptionCategoryAttributeValuesResponse(**response)


    async def description_category_attribute_values_search(
        self: "SellerCategoryAPI",
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
            json=request.model_dump(),
        )
        return DescriptionCategoryAttributeValuesSearchResponse(**response)