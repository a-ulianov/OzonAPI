from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesCreateInfoRequest,
    CargoesCreateInfoResponse,
)


class CargoesCreateInfoMixin(APIManager):
    """Реализует метод /v2/cargoes/create/info"""

    async def cargoes_create_info(
            self: "CargoesCreateInfoMixin",
            request: CargoesCreateInfoRequest
    ) -> CargoesCreateInfoResponse:
        """Возвращает информацию по установке грузомест в заявке на поставку FBO.

        Notes:
            • Используйте `operation_id`, полученный методом `cargoes_create()`.
            • При успехе в `result.cargoes` возвращаются идентификаторы установленных
              грузомест; при ошибке — `errors`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CargoesCreateInfoV2

        Args:
            request: Запрос информации по схеме `CargoesCreateInfoRequest`

        Returns:
            Результат установки грузомест по схеме `CargoesCreateInfoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_create_info(
                    CargoesCreateInfoRequest(operation_id="op-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="cargoes/create/info",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesCreateInfoResponse(**response)
