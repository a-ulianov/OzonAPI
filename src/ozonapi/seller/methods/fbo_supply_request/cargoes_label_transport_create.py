from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesLabelTransportCreateRequest,
    CargoesLabelTransportCreateResponse,
)


class CargoesLabelTransportCreateMixin(APIManager):
    """Реализует метод /v1/cargoes/label/transport/create"""

    async def cargoes_label_transport_create(
            self: "CargoesLabelTransportCreateMixin",
            request: CargoesLabelTransportCreateRequest
    ) -> CargoesLabelTransportCreateResponse:
        """Запускает генерацию этикеток транспортных грузомест по грузоместу.

        Notes:
            • Асинхронная операция; статус и ссылку на файл — через
              `cargoes_label_transport_status()` по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос генерации этикеток по схеме
                `CargoesLabelTransportCreateRequest`

        Returns:
            Идентификатор операции по схеме
            `CargoesLabelTransportCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_label_transport_create(
                    CargoesLabelTransportCreateRequest(
                        supply_id=123, transport_cargo_ids=["10"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/label/transport/create",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesLabelTransportCreateResponse(**response)
