from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesLabelCreateRequest,
    CargoesLabelCreateResponse,
)


class CargoesLabelCreateMixin(APIManager):
    """Реализует метод /v1/cargoes-label/create"""

    async def cargoes_label_create(
            self: "CargoesLabelCreateMixin",
            request: CargoesLabelCreateRequest
    ) -> CargoesLabelCreateResponse:
        """Запускает генерацию этикеток для грузомест поставки.

        Notes:
            • Асинхронная операция; идентификатор этикетки — через `cargoes_label_get()`
              по `operation_id`, PDF — через `cargoes_label_file()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/SupplyDraftAPI_CargoesLabelCreate

        Args:
            request: Запрос генерации этикеток по схеме `CargoesLabelCreateRequest`

        Returns:
            Идентификатор операции по схеме `CargoesLabelCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_label_create(
                    CargoesLabelCreateRequest(
                        supply_id=123, cargoes=[CargoesLabelCreateCargo(cargo_id=1)]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes-label/create",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesLabelCreateResponse(**response)
