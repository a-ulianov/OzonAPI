from ...core import APIManager
from ...schemas.notifications import (
    NotificationEnableRequest,
    NotificationEnableResponse,
)


class NotificationEnableMixin(APIManager):
    """Реализует метод /v1/notification/enable"""

    async def notification_enable(
            self: "NotificationEnableMixin",
            request: NotificationEnableRequest
    ) -> NotificationEnableResponse:
        """Включает или выключает уведомления на подключённый URL-адрес.

        Notes:
            • Идентификатор подключённого URL `id` возвращает метод `notification_list()`.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/EnableNotification

        Args:
            request: Запрос на включение/выключение по схеме `NotificationEnableRequest`

        Returns:
            Пустой ответ по схеме `NotificationEnableResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.notification_enable(
                    NotificationEnableRequest(id=123, enabled=True)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="notification/enable",
            payload=request.model_dump()
        )
        return NotificationEnableResponse(**response)
