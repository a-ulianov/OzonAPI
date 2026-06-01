from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesDeleteRequest,
    CargoesDeleteResponse,
)


class CargoesDeleteMixin(APIManager):
    """Реализует метод /v1/cargoes/delete"""

    async def cargoes_delete(
            self: "CargoesDeleteMixin",
            request: CargoesDeleteRequest
    ) -> CargoesDeleteResponse:
        """Запускает удаление грузомест из заявки на поставку FBO.

        Notes:
            • Асинхронная операция; статус — через `cargoes_delete_status()`
              по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CargoesAPI_CargoesDelete

        Args:
            request: Запрос удаления грузомест по схеме `CargoesDeleteRequest`

        Returns:
            Идентификатор операции по схеме `CargoesDeleteResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_delete(
                    CargoesDeleteRequest(supply_id=123, cargo_ids=["1"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/delete",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesDeleteResponse(**response)
