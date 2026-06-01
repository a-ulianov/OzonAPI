from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesRulesGetRequest,
    CargoesRulesGetResponse,
)


class CargoesRulesGetMixin(APIManager):
    """Реализует метод /v1/cargoes/rules/get"""

    async def cargoes_rules_get(
            self: "CargoesRulesGetMixin",
            request: CargoesRulesGetRequest
    ) -> CargoesRulesGetResponse:
        """Возвращает чек-лист по установке грузомест для заявок на поставку FBO.

        Notes:
            • По каждой поставке возвращаются правила установки грузомест с флагом
              `satisfied` — выполнено ли правило.

        References:
            https://docs.ozon.ru/api/seller/#operation/CargoesAPI_CargoesRulesGet

        Args:
            request: Запрос чек-листа по схеме `CargoesRulesGetRequest`

        Returns:
            Чек-листы по поставкам по схеме `CargoesRulesGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_rules_get(
                    CargoesRulesGetRequest(supply_ids=["123"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/rules/get",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesRulesGetResponse(**response)
