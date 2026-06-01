from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsListRequest,
    SellerActionsListResponse,
)


class SellerActionsListMixin(APIManager):
    """Реализует метод /v1/seller-actions/list"""

    async def seller_actions_list(
            self: "SellerActionsListMixin",
            request: SellerActionsListRequest,
    ) -> SellerActionsListResponse:
        """Получает список акций продавца.

        Notes:
            • Список можно фильтровать по идентификаторам, механикам, статусам и названию.
            • Пагинация выполняется через `limit` и `offset`.
            • Для каждой акции возвращаются её параметры в объекте `action_parameters`.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsList

        Args:
            request: Параметры фильтрации и пагинации по схеме `SellerActionsListRequest`

        Returns:
            Список акций продавца по схеме `SellerActionsListResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.seller_actions_list(
                    SellerActionsListRequest(status=["ACTIVE"], limit=50)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/list",
            payload=request.model_dump(),
        )
        return SellerActionsListResponse(**response)
