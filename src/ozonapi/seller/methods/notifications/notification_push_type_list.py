from ...core import APIManager
from ...schemas.notifications import NotificationPushTypeListResponse


class NotificationPushTypeListMixin(APIManager):
    """Реализует метод /v1/notification/push-type/list"""

    async def notification_push_type_list(
            self: "NotificationPushTypeListMixin"
    ) -> NotificationPushTypeListResponse:
        """Возвращает доступные типы пуш-уведомлений.

        Notes:
            • Метод не принимает параметров.
            • Для каждого типа возвращается описание и подключённый URL-адрес
              `seller_endpoint`, если он настроен.

        References:
            https://docs.ozon.ru/api/seller/#operation/GetNotificationPushTypeList

        Returns:
            Список типов пуш-уведомлений по схеме `NotificationPushTypeListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.notification_push_type_list()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="notification/push-type/list",
            payload={}
        )
        return NotificationPushTypeListResponse(**response)
