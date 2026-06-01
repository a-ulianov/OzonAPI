from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesCreateRequest,
    CargoesCreateResponse,
)


class CargoesCreateMixin(APIManager):
    """Реализует метод /v1/cargoes/create"""

    async def cargoes_create(
            self: "CargoesCreateMixin",
            request: CargoesCreateRequest
    ) -> CargoesCreateResponse:
        """Запускает установку грузомест в заявке на поставку FBO.

        Notes:
            • Асинхронная операция; результат — через `cargoes_create_info()`
              по `operation_id`.
            • Установите `delete_current_version=true`, чтобы заменить ранее
              установленные грузоместа.

        References:
            https://docs.ozon.ru/api/seller/#operation/CargoesAPI_CargoesCreate

        Args:
            request: Запрос установки грузомест по схеме `CargoesCreateRequest`

        Returns:
            Идентификатор операции по схеме `CargoesCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_create(
                    CargoesCreateRequest(supply_id=123, cargoes=[])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/create",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesCreateResponse(**response)
