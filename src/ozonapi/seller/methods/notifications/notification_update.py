from ...core import APIManager
from ...schemas.notifications import (
    NotificationUpdateRequest,
    NotificationUpdateResponse,
)


class NotificationUpdateMixin(APIManager):
    """Реализует метод /v1/notification/update"""

    async def notification_update(
            self: "NotificationUpdateMixin",
            request: NotificationUpdateRequest
    ) -> NotificationUpdateResponse:
        """Изменяет подключённый URL-адрес для уведомлений и набор типов.

        Notes:
            • Идентификатор подключённого URL `id` возвращает метод `notification_list()`.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/UpdateNotification

        Args:
            request: Запрос на изменение URL по схеме `NotificationUpdateRequest`

        Returns:
            Пустой ответ по схеме `NotificationUpdateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.notification_update(
                    NotificationUpdateRequest(
                        id=123,
                        url="https://example.com/ozon",
                        types=["TYPE_NEW_POSTING"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="notification/update",
            payload=request.model_dump()
        )
        return NotificationUpdateResponse(**response)
