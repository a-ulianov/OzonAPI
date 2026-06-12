from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesGetRequest,
    CargoesGetResponse,
)


class CargoesGetMixin(APIManager):
    """Реализует метод /v2/cargoes/get"""

    async def cargoes_get(
            self: "CargoesGetMixin",
            request: CargoesGetRequest
    ) -> CargoesGetResponse:
        """Возвращает информацию о грузоместах в заявках на поставку FBO.

        Notes:
            • Канонический метод (v2): дополнительно возвращает транспортные
              грузоместа, лимиты поставки и данные отслеживания. Устаревшая
              v1-версия доступна как `cargoes_get_v1()`.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос информации о грузоместах по схеме `CargoesGetRequest`

        Returns:
            Грузоместа поставок по схеме `CargoesGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_get(
                    CargoesGetRequest(
                        supplies=[
                            CargoesGetSupplyRequest(
                                supply_id=123, cargo_ids=["1"]
                            )
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="cargoes/get",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesGetResponse(**response)
