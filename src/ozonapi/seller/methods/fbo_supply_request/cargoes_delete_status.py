from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesDeleteStatusRequest,
    CargoesDeleteStatusResponse,
)


class CargoesDeleteStatusMixin(APIManager):
    """Реализует метод /v2/cargoes/delete/status"""

    async def cargoes_delete_status(
            self: "CargoesDeleteStatusMixin",
            request: CargoesDeleteStatusRequest
    ) -> CargoesDeleteStatusResponse:
        """Возвращает статус удаления грузомест и транспортных грузомест.

        Notes:
            • Канонический метод (v2). Устаревшая v1-версия доступна как
              `cargoes_delete_status_v1()`.
            • Используйте `operation_id`, полученный методом `cargoes_delete()`.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос статуса удаления по схеме
                `CargoesDeleteStatusRequest`

        Returns:
            Статус удаления грузомест по схеме `CargoesDeleteStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_delete_status(
                    CargoesDeleteStatusRequest(operation_id="op-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="cargoes/delete/status",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesDeleteStatusResponse(**response)
