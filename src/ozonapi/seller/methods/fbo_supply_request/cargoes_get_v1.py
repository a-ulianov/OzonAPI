from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesGetV1Request,
    CargoesGetV1Response,
)


class CargoesGetV1Mixin(APIManager):
    """Реализует метод /v1/cargoes/get"""

    async def cargoes_get_v1(
            self: "CargoesGetV1Mixin",
            request: CargoesGetV1Request
    ) -> CargoesGetV1Response:
        """Возвращает информацию о грузоместах в заявках на поставку FBO (v1).

        Notes:
            • Устаревшая версия. Используйте канонический `cargoes_get()` (v2),
              возвращающий данные о транспортных грузоместах и лимитах.

        References:
            https://docs.ozon.ru/api/seller/#operation/CargoesGet

        Args:
            request: Запрос информации о грузоместах по схеме
                `CargoesGetV1Request`

        Returns:
            Грузоместа поставок по схеме `CargoesGetV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_get_v1(
                    CargoesGetV1Request(supply_ids=["123"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/get",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesGetV1Response(**response)
