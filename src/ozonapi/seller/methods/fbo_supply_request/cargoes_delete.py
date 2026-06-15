from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesDeleteRequest,
    CargoesDeleteResponse,
)


class CargoesDeleteMixin(APIManager):
    """Реализует метод /v2/cargoes/delete"""

    async def cargoes_delete(
            self: "CargoesDeleteMixin",
            request: CargoesDeleteRequest
    ) -> CargoesDeleteResponse:
        """Запускает удаление грузомест и транспортных грузомест из поставки FBO.

        Notes:
            • Канонический метод (v2): удаляет как грузоместа, так и транспортные
              грузоместа; способ удаления задаётся `transport_cargo_deletion_type`.
              Устаревшая v1-версия доступна как `cargoes_delete_v1()`.
            • Асинхронная операция; статус — через `cargoes_delete_status()` по
              `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос удаления грузомест по схеме `CargoesDeleteRequest`

        Returns:
            Идентификатор операции по схеме `CargoesDeleteResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_delete(
                    CargoesDeleteRequest(
                        supply_id=123,
                        cargo_ids=["1"],
                        transport_cargo_deletion_type="UNBIND_CONTAINED_CARGOES",
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="cargoes/delete",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesDeleteResponse(**response)
