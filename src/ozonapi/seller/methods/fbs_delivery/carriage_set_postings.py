from ...core import APIManager
from ...schemas.fbs_delivery import (
    CarriageSetPostingsRequest,
    CarriageSetPostingsResponse,
)


class CarriageSetPostingsMixin(APIManager):
    """Реализует метод /v1/carriage/set-postings"""

    async def carriage_set_postings(
            self: "CarriageSetPostingsMixin",
            request: CarriageSetPostingsRequest
    ) -> CarriageSetPostingsResponse:
        """Метод для изменения состава отгрузки.

        Notes:
            • Передавайте полный актуальный список отправлений отгрузки.
            • Отправления, которых нет в списке, будут исключены из отгрузки.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_SetPostings

        Args:
            request: Запрос на изменение состава отгрузки по схеме `CarriageSetPostingsRequest`

        Returns:
            Результат изменения состава отгрузки по схеме `CarriageSetPostingsResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_set_postings(
                    CarriageSetPostingsRequest(
                        carriage_id=12345,
                        posting_numbers=["33920113-1231-1"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/set-postings",
            payload=request.model_dump()
        )
        return CarriageSetPostingsResponse(**response)
