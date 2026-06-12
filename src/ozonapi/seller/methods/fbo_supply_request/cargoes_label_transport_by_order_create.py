from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesLabelTransportByOrderCreateRequest,
    CargoesLabelTransportByOrderCreateResponse,
)


class CargoesLabelTransportByOrderCreateMixin(APIManager):
    """Реализует метод /v1/cargoes/label/transport-by-order/create"""

    async def cargoes_label_transport_by_order_create(
            self: "CargoesLabelTransportByOrderCreateMixin",
            request: CargoesLabelTransportByOrderCreateRequest
    ) -> CargoesLabelTransportByOrderCreateResponse:
        """Запускает генерацию этикеток транспортных грузомест по поставке.

        Notes:
            • Асинхронная операция; статус и ссылку на файл — через
              `cargoes_label_transport_by_order_status()` по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос генерации этикеток по схеме
                `CargoesLabelTransportByOrderCreateRequest`

        Returns:
            Идентификатор операции по схеме
            `CargoesLabelTransportByOrderCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_label_transport_by_order_create(
                    CargoesLabelTransportByOrderCreateRequest(order_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/label/transport-by-order/create",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesLabelTransportByOrderCreateResponse(**response)
