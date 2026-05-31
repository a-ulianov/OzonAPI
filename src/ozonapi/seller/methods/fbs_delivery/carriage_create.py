from ...core import APIManager
from ...schemas.fbs_delivery import CarriageCreateRequest, CarriageCreateResponse


class CarriageCreateMixin(APIManager):
    """Реализует метод /v1/carriage/create"""

    async def carriage_create(
            self: "CarriageCreateMixin",
            request: CarriageCreateRequest
    ) -> CarriageCreateResponse:
        """Метод для создания отгрузки (перевозки) по методу доставки FBS.

        Notes:
            • Создаёт отгрузку для указанного метода доставки на дату отгрузки.
            • По умолчанию дата отгрузки — текущая дата.
            • Для отгрузки с прослеживаемыми товарами укажите `all_blr_traceable = true`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageCreate

        Args:
            request: Запрос на создание отгрузки по схеме `CarriageCreateRequest`

        Returns:
            Результат создания отгрузки по схеме `CarriageCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_create(
                    CarriageCreateRequest(
                        delivery_method_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/create",
            payload=request.model_dump()
        )
        return CarriageCreateResponse(**response)
