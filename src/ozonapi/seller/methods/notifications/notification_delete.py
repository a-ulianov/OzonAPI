from ...core import APIManager
from ...schemas.notifications import (
    NotificationDeleteRequest,
    NotificationDeleteResponse,
)


class NotificationDeleteMixin(APIManager):
    """Реализует метод /v1/notification/delete"""

    async def notification_delete(
            self: "NotificationDeleteMixin",
            request: NotificationDeleteRequest
    ) -> NotificationDeleteResponse:
        """Удаляет подключённый URL-адрес для уведомлений.

        Notes:
            • Идентификатор подключённого URL `id` возвращает метод `notification_list()`.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/DeleteNotification

        Args:
            request: Запрос на удаление URL по схеме `NotificationDeleteRequest`

        Returns:
            Пустой ответ по схеме `NotificationDeleteResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.notification_delete(
                    NotificationDeleteRequest(id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="notification/delete",
            payload=request.model_dump()
        )
        return NotificationDeleteResponse(**response)
