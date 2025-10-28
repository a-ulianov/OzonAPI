from ...core import APIManager
from ...schemas.attributes_and_characteristics import DescriptionCategoryTreeRequest, DescriptionCategoryTreeResponse


class DescriptionCategoryTreeMixin(APIManager):
    """Реализует метод /v1/description-category/tree"""

    async def description_category_tree(
        self: "DescriptionCategoryTreeMixin",
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
            payload=request.model_dump()
        )
        return DescriptionCategoryTreeResponse(**response)
