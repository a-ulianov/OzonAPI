from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesLabelGetRequest,
    CargoesLabelGetResponse,
)


class CargoesLabelGetMixin(APIManager):
    """Реализует метод /v1/cargoes-label/get"""

    async def cargoes_label_get(
            self: "CargoesLabelGetMixin",
            request: CargoesLabelGetRequest
    ) -> CargoesLabelGetResponse:
        """Возвращает идентификатор и ссылку на PDF с этикетками грузомест.

        Notes:
            • При готовности возвращает `file_guid` (для `cargoes_label_file()`) и
              прямую ссылку `file_url` на PDF.

        References:
            https://docs.ozon.ru/api/seller/#operation/SupplyDraftAPI_CargoesLabelGet

        Args:
            request: Запрос идентификатора этикетки по схеме `CargoesLabelGetRequest`

        Returns:
            Идентификатор и ссылка на PDF по схеме `CargoesLabelGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_label_get(
                    CargoesLabelGetRequest(operation_id="op-123")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes-label/get",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesLabelGetResponse(**response)
