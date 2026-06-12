from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesDeleteStatusV1Request,
    CargoesDeleteStatusV1Response,
)


class CargoesDeleteStatusV1Mixin(APIManager):
    """Реализует метод /v1/cargoes/delete/status"""

    async def cargoes_delete_status_v1(
            self: "CargoesDeleteStatusV1Mixin",
            request: CargoesDeleteStatusV1Request
    ) -> CargoesDeleteStatusV1Response:
        """Возвращает статус удаления грузомест из заявки на поставку FBO (v1).

        Notes:
            • Устаревшая версия. Используйте канонический
              `cargoes_delete_status()` (v2).
            • Используйте `operation_id`, полученный методом
              `cargoes_delete_v1()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CargoesAPI_CargoesDeleteStatus

        Args:
            request: Запрос статуса удаления по схеме
                `CargoesDeleteStatusV1Request`

        Returns:
            Статус удаления грузомест по схеме `CargoesDeleteStatusV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_delete_status_v1(
                    CargoesDeleteStatusV1Request(operation_id="op-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/delete/status",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesDeleteStatusV1Response(**response)
