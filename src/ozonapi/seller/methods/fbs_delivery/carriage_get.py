from ...core import APIManager
from ...schemas.fbs_delivery import CarriageGetRequest, CarriageGetResponse


class CarriageGetMixin(APIManager):
    """Реализует метод /v1/carriage/get"""

    async def carriage_get(
            self: "CarriageGetMixin",
            request: CarriageGetRequest
    ) -> CarriageGetResponse:
        """Метод для получения информации о перевозке.

        Notes:
            • Возвращает подробную информацию о перевозке: статус, склад, метод доставки,
              грузовые места, доступные действия и возможность отмены.
            • Идентификатор перевозки можно получить методом `carriage_create()`
              или из списка отгрузок `carriage_delivery_list()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageGet

        Args:
            request: Запрос на получение информации о перевозке по схеме `CarriageGetRequest`

        Returns:
            Информация о перевозке по схеме `CarriageGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_get(
                    CarriageGetRequest(
                        carriage_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/get",
            payload=request.model_dump()
        )
        return CarriageGetResponse(**response)
