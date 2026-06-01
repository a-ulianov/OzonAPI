from ...core import APIManager
from ...schemas.notifications import (
    NotificationCheckRequest,
    NotificationCheckResponse,
)


class NotificationCheckMixin(APIManager):
    """Реализует метод /v1/notification/check"""

    async def notification_check(
            self: "NotificationCheckMixin",
            request: NotificationCheckRequest
    ) -> NotificationCheckResponse:
        """Проверяет доступность URL-адреса для пуш-уведомлений.

        Notes:
            • Ozon отправляет тестовый запрос на URL и возвращает результат проверки.
            • При недоступности URL в `errors` возвращается тип и описание ошибки.

        References:
            https://docs.ozon.ru/api/seller/#operation/CheckNotification

        Args:
            request: Запрос на проверку URL по схеме `NotificationCheckRequest`

        Returns:
            Результат проверки URL по схеме `NotificationCheckResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.notification_check(
                    NotificationCheckRequest(url="https://example.com/ozon")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="notification/check",
            payload=request.model_dump()
        )
        return NotificationCheckResponse(**response)
