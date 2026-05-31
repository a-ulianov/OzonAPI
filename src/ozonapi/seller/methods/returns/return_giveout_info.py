from ...core import APIManager
from ...schemas.returns import ReturnGiveoutInfoRequest, ReturnGiveoutInfoResponse


class ReturnGiveoutInfoMixin(APIManager):
    """Реализует метод /v1/return/giveout/info"""

    async def return_giveout_info(
            self: "ReturnGiveoutInfoMixin",
            request: ReturnGiveoutInfoRequest
    ) -> ReturnGiveoutInfoResponse:
        """Метод для получения информации о возвратной отгрузке.

        Notes:
            • Возвращает статус отгрузки, артикулы товаров и склад.

        References:
            https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutInfo

        Args:
            request: Запрос на получение информации об отгрузке по схеме `ReturnGiveoutInfoRequest`

        Returns:
            Информация о возвратной отгрузке по схеме `ReturnGiveoutInfoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.return_giveout_info(
                    ReturnGiveoutInfoRequest(
                        giveout_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="return/giveout/info",
            payload=request.model_dump()
        )
        return ReturnGiveoutInfoResponse(**response)
