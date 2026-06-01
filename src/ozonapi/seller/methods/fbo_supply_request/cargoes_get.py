from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesGetRequest,
    CargoesGetResponse,
)


class CargoesGetMixin(APIManager):
    """Реализует метод /v1/cargoes/get"""

    async def cargoes_get(
            self: "CargoesGetMixin",
            request: CargoesGetRequest
    ) -> CargoesGetResponse:
        """Возвращает информацию о грузоместах в заявках на поставку FBO.

        Notes:
            • Возвращает грузоместа по каждой запрошенной поставке вместе с данными
              отслеживания и типом зоны размещения.

        References:
            https://docs.ozon.ru/api/seller/#operation/CargoesGet

        Args:
            request: Запрос информации о грузоместах по схеме `CargoesGetRequest`

        Returns:
            Грузоместа поставок по схеме `CargoesGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_get(
                    CargoesGetRequest(supply_ids=["123"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/get",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesGetResponse(**response)
