from ...core import APIManager
from ...schemas.cancellations import CancelReasonListResponse


class CancelReasonListMixin(APIManager):
    """Реализует метод /v1/cancel-reason/list"""

    async def cancel_reason_list(
            self: "CancelReasonListMixin",
    ) -> CancelReasonListResponse:
        """Получает список причин отмены заказов.

        Notes:
            • Метод не принимает параметров и возвращает все доступные причины отмены.
            • Идентификаторы причин используются в методах отмены отправлений.

        References:
            https://docs.ozon.ru/api/seller/#operation/CancelReasonList

        Returns:
            Список причин отмены по схеме `CancelReasonListResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cancel_reason_list()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cancel-reason/list",
            payload={},
        )
        return CancelReasonListResponse(**response)
