from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsChangeActivityRequest,
    SellerActionsChangeActivityResponse,
)


class SellerActionsChangeActivityMixin(APIManager):
    """Реализует метод /v1/seller-actions/change-activity"""

    async def seller_actions_change_activity(
            self: "SellerActionsChangeActivityMixin",
            request: SellerActionsChangeActivityRequest,
    ) -> SellerActionsChangeActivityResponse:
        """Включает или выключает акцию продавца.

        Notes:
            • Параметр `is_turn_on=True` включает акцию, `False` — выключает.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsChangeActivity

        Args:
            request: Идентификатор акции и флаг активности по схеме
                `SellerActionsChangeActivityRequest`

        Returns:
            Пустой ответ по схеме `SellerActionsChangeActivityResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.seller_actions_change_activity(
                    SellerActionsChangeActivityRequest(action_id=123456, is_turn_on=True)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/change-activity",
            payload=request.model_dump(),
        )
        return SellerActionsChangeActivityResponse(**response)
