from ...core import APIManager
from ...schemas.fbs_delivery import (
    PostingFBSActCreateRequest,
    PostingFBSActCreateResponse,
)


class PostingFBSActCreateMixin(APIManager):
    """Реализует метод /v2/posting/fbs/act/create"""

    async def posting_fbs_act_create(
            self: "PostingFBSActCreateMixin",
            request: PostingFBSActCreateRequest
    ) -> PostingFBSActCreateResponse:
        """Метод для подтверждения отгрузки и создания документов.

        Notes:
            • Запускает асинхронное формирование штрихкода и документов отгрузки.
            • Возвращает идентификатор задания; статус проверяйте методом
              `posting_fbs_act_check_status()`.
            • Если вы подключены к схеме с грузовыми местами, передайте `containers_count`.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSActCreate

        Args:
            request: Запрос на создание документов по схеме `PostingFBSActCreateRequest`

        Returns:
            Результат создания задания по схеме `PostingFBSActCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_act_create(
                    PostingFBSActCreateRequest(
                        delivery_method_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/create",
            payload=request.model_dump()
        )
        return PostingFBSActCreateResponse(**response)
