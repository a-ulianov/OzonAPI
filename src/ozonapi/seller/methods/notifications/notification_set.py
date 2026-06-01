from ...core import APIManager
from ...schemas.notifications import (
    NotificationSetRequest,
    NotificationSetResponse,
)


class NotificationSetMixin(APIManager):
    """Реализует метод /v1/notification/set"""

    async def notification_set(
            self: "NotificationSetMixin",
            request: NotificationSetRequest
    ) -> NotificationSetResponse:
        """Подключает URL-адрес для получения пуш-уведомлений.

        Notes:
            • Список доступных типов уведомлений возвращает метод
              `notification_push_type_list()`.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/SetNotification

        Args:
            request: Запрос на подключение URL по схеме `NotificationSetRequest`

        Returns:
            Пустой ответ по схеме `NotificationSetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.notification_set(
                    NotificationSetRequest(
                        url="https://example.com/ozon",
                        types=["TYPE_NEW_POSTING"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="notification/set",
            payload=request.model_dump()
        )
        return NotificationSetResponse(**response)
