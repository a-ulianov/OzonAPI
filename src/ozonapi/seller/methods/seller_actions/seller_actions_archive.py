from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsArchiveRequest,
    SellerActionsArchiveResponse,
)


class SellerActionsArchiveMixin(APIManager):
    """Реализует метод /v1/seller-actions/archive"""

    async def seller_actions_archive(
            self: "SellerActionsArchiveMixin",
            request: SellerActionsArchiveRequest,
    ) -> SellerActionsArchiveResponse:
        """Переносит акцию продавца в архив.

        Notes:
            • Архивная акция больше не отображается в активном списке.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsArchive

        Args:
            request: Идентификатор акции по схеме `SellerActionsArchiveRequest`

        Returns:
            Пустой ответ по схеме `SellerActionsArchiveResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.seller_actions_archive(
                    SellerActionsArchiveRequest(action_id=123456)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/archive",
            payload=request.model_dump(),
        )
        return SellerActionsArchiveResponse(**response)
