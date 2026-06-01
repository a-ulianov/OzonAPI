from ...core import APIManager
from ...schemas.notifications import NotificationListResponse


class NotificationListMixin(APIManager):
    """Реализует метод /v1/notification/list"""

    async def notification_list(
            self: "NotificationListMixin"
    ) -> NotificationListResponse:
        """Возвращает информацию по подключённым URL-адресам для уведомлений.

        Notes:
            • Метод не принимает параметров.
            • Для каждого URL возвращаются подключённые типы уведомлений и признак
              активности `enable`.

        References:
            https://docs.ozon.ru/api/seller/#operation/NotificationList

        Returns:
            Список подключённых URL-адресов по схеме `NotificationListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.notification_list()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="notification/list",
            payload={}
        )
        return NotificationListResponse(**response)
