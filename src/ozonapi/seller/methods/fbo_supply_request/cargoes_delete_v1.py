from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesDeleteV1Request,
    CargoesDeleteV1Response,
)


class CargoesDeleteV1Mixin(APIManager):
    """Реализует метод /v1/cargoes/delete"""

    async def cargoes_delete_v1(
            self: "CargoesDeleteV1Mixin",
            request: CargoesDeleteV1Request
    ) -> CargoesDeleteV1Response:
        """Запускает удаление грузомест из заявки на поставку FBO (v1).

        Notes:
            • Устаревшая версия. Используйте канонический `cargoes_delete()`
              (v2), поддерживающий удаление транспортных грузомест.
            • Асинхронная операция; статус — через `cargoes_delete_status_v1()`
              по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CargoesAPI_CargoesDelete

        Args:
            request: Запрос удаления грузомест по схеме `CargoesDeleteV1Request`

        Returns:
            Идентификатор операции по схеме `CargoesDeleteV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_delete_v1(
                    CargoesDeleteV1Request(supply_id=123, cargo_ids=["1"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/delete",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesDeleteV1Response(**response)
