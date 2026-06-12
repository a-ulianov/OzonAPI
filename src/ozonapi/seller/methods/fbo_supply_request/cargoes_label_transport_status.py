from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesLabelTransportStatusRequest,
    CargoesLabelTransportStatusResponse,
)


class CargoesLabelTransportStatusMixin(APIManager):
    """Реализует метод /v1/cargoes/label/transport/status"""

    async def cargoes_label_transport_status(
            self: "CargoesLabelTransportStatusMixin",
            request: CargoesLabelTransportStatusRequest
    ) -> CargoesLabelTransportStatusResponse:
        """Возвращает статус генерации этикеток транспортных грузомест.

        Notes:
            • Используйте `operation_id`, полученный методом
              `cargoes_label_transport_create()`. При успехе в `result.file_url`
              возвращается ссылка на файл с этикетками.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос статуса генерации по схеме
                `CargoesLabelTransportStatusRequest`

        Returns:
            Статус и ссылку на файл по схеме
            `CargoesLabelTransportStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_label_transport_status(
                    CargoesLabelTransportStatusRequest(operation_id="op-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/label/transport/status",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesLabelTransportStatusResponse(**response)
