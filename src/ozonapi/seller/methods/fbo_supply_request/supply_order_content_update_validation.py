from ...core import APIManager
from ...schemas.fbo_supply_request import (
    SupplyOrderContentUpdateValidationRequest,
    SupplyOrderContentUpdateValidationResponse,
)


class SupplyOrderContentUpdateValidationMixin(APIManager):
    """Реализует метод /v1/supply-order/content/update/validation"""

    async def supply_order_content_update_validation(
            self: "SupplyOrderContentUpdateValidationMixin",
            request: SupplyOrderContentUpdateValidationRequest
    ) -> SupplyOrderContentUpdateValidationResponse:
        """Проверяет новый товарный состав заявки на поставку FBO.

        Notes:
            • Возвращает одобренные и отклонённые товары с причинами отклонения
              и ограничениями, а также сводные счётчики по составу.

        References:
            https://docs.ozon.ru/api/seller/#operation/SupplyOrderContentUpdateValidation

        Args:
            request: Запрос проверки состава по схеме
                `SupplyOrderContentUpdateValidationRequest`

        Returns:
            Результат проверки по схеме `SupplyOrderContentUpdateValidationResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_content_update_validation(
                    SupplyOrderContentUpdateValidationRequest(
                        new_bundle_id="b1", supply_id=2
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="supply-order/content/update/validation",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderContentUpdateValidationResponse(**response)
