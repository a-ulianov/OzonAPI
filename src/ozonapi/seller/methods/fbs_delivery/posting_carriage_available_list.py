from ...core import APIManager
from ...schemas.fbs_delivery import (
    PostingCarriageAvailableListRequest,
    PostingCarriageAvailableListResponse,
)


class PostingCarriageAvailableListMixin(APIManager):
    """Реализует метод /v1/posting/carriage-available/list"""

    async def posting_carriage_available_list(
            self: "PostingCarriageAvailableListMixin",
            request: PostingCarriageAvailableListRequest
    ) -> PostingCarriageAvailableListResponse:
        """Метод для получения списка доступных перевозок.

        Notes:
            • Возвращает перевозки, доступные для указанного метода доставки и даты отгрузки.
            • По умолчанию дата отгрузки — текущая дата.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetCarriageAvailableList

        Args:
            request: Запрос на получение списка доступных перевозок по схеме `PostingCarriageAvailableListRequest`

        Returns:
            Список доступных перевозок по схеме `PostingCarriageAvailableListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_carriage_available_list(
                    PostingCarriageAvailableListRequest(
                        delivery_method_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/carriage-available/list",
            payload=request.model_dump()
        )
        return PostingCarriageAvailableListResponse(**response)
