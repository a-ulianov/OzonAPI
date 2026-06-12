from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesTransportCreateRequest,
    CargoesTransportCreateResponse,
)


class CargoesTransportCreateMixin(APIManager):
    """Реализует метод /v1/cargoes/transport/create"""

    async def cargoes_transport_create(
            self: "CargoesTransportCreateMixin",
            request: CargoesTransportCreateRequest
    ) -> CargoesTransportCreateResponse:
        """Создаёт транспортные грузоместа в поставке FBO.

        Notes:
            • Асинхронная операция; статус — через
              `cargoes_transport_create_status()` по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос создания транспортных грузомест по схеме
                `CargoesTransportCreateRequest`

        Returns:
            Идентификатор операции по схеме `CargoesTransportCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_transport_create(
                    CargoesTransportCreateRequest(
                        supply_id=123,
                        transport_cargoes=[
                            CargoesTransportCreateItem(count=1, type="PALLET")
                        ],
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/transport/create",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesTransportCreateResponse(**response)
