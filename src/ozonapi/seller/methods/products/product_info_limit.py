from ...core import APIManager
from ...schemas.products import ProductInfoLimitResponse


class ProductInfoLimitMixin(APIManager):
    """Реализует метод /v4/product/info/limit"""

    async def product_info_limit(
            self: "ProductInfoLimitMixin"
    ) -> ProductInfoLimitResponse:
        """Получает информацию о лимитах на ассортимент, создание и обновление товаров.

        Notes:
            • Метод возвращает информацию о трёх типах лимитов:
                - Лимит на ассортимент (total) — сколько всего товаров можно создать в личном кабинете.
                - Суточный лимит на создание товаров (daily_create) — сколько товаров можно создать в сутки.
                - Суточный лимит на обновление товаров (daily_update) — сколько товаров можно обновить в сутки.
            • Если значение лимита равно `-1`, это означает, что лимит не ограничен.
            • При достижении лимита на ассортимент вы не сможете создавать новые товары.
            • Суточные лимиты сбрасываются в указанное в `reset_at` время по UTC.
            • Лимиты зависят от типа аккаунта продавца и могут изменяться.
            • Рекомендуется проверять лимиты перед массовыми операциями с товарами.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/ProductAPI_GetUploadQuota

        Returns:
            Информация о лимитах на ассортимент, создание и обновление товаров по схеме `ProductInfoLimitResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_info_limit()
        """
        response = await self._request(
            method="post",
            api_version="v4",
            endpoint="product/info/limit",
            payload={},
        )
        return ProductInfoLimitResponse(**response)