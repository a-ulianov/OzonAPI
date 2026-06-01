from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesDeleteStatusRequest,
    CargoesDeleteStatusResponse,
)


class CargoesDeleteStatusMixin(APIManager):
    """Реализует метод /v1/cargoes/delete/status"""

    async def cargoes_delete_status(
            self: "CargoesDeleteStatusMixin",
            request: CargoesDeleteStatusRequest
    ) -> CargoesDeleteStatusResponse:
        """Возвращает статус удаления грузомест из заявки на поставку FBO.

        Notes:
            • Используйте `operation_id`, полученный методом `cargoes_delete()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CargoesAPI_CargoesDeleteStatus

        Args:
            request: Запрос статуса удаления по схеме `CargoesDeleteStatusRequest`

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
            api_version="v1",
            endpoint="cargoes/delete/status",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesDeleteStatusResponse(**response)
