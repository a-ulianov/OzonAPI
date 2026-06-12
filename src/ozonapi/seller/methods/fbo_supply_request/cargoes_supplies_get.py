from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesSuppliesGetRequest,
    CargoesSuppliesGetResponse,
)


class CargoesSuppliesGetMixin(APIManager):
    """Реализует метод /v1/cargoes/supplies/get"""

    async def cargoes_supplies_get(
            self: "CargoesSuppliesGetMixin",
            request: CargoesSuppliesGetRequest
    ) -> CargoesSuppliesGetResponse:
        """Возвращает информацию о грузоместах в поставках FBO.

        Notes:
            • Для каждой поставки возвращаются как грузоместа без транспортных
              грузомест, так и транспортные грузоместа с их содержимым.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос информации о грузоместах по схеме
                `CargoesSuppliesGetRequest`

        Returns:
            Грузоместа по поставкам по схеме `CargoesSuppliesGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_supplies_get(
                    CargoesSuppliesGetRequest(supply_ids=["123"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/supplies/get",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesSuppliesGetResponse(**response)
