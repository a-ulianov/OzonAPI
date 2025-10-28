from ...core import APIManager
from ...schemas.fbs import PostingFBSRestrictionsRequest, PostingFBSRestrictionsResponse


class PostingFBSRestrictionsMixin(APIManager):
    """Реализует метод /v1/posting/fbs/restrictions"""

    async def posting_fbs_restrictions(
            self: "PostingFBSRestrictionsMixin",
            request: PostingFBSRestrictionsRequest
    ) -> PostingFBSRestrictionsResponse:
        """Метод для получения габаритных, весовых и прочих ограничений пункта приёма по номеру отправления.

        Notes:
            • Метод применим только для работы по схеме FBS.
            • Возвращает ограничения пункта приёма, связанные с указанным отправлением.
            • Ограничения включают габаритные (ширина, высота, длина), весовые (мин./макс. вес) и стоимостные (мин./макс. цена) параметры.
            • Вес указывается в граммах, габариты — в сантиметрах, стоимость — в рублях.
            • Если для какого-то параметра ограничение не установлено, значение будет None.
            • Метод помогает определить, соответствует ли отправление требованиям пункта приёма перед передачей.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PostingAPI_GetRestrictions

        Args:
            request: Запрос на получение ограничений пункта приёма по номеру отправления по схеме `PostingFBSRestrictionsRequest`

        Returns:
            Ограничения пункта приёма для указанного отправления по схеме `PostingFBSRestrictionsResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_restrictions(
                    PostingFBSRestrictionsRequest(
                        posting_number="76673629-0020-1"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/restrictions",
            payload=request.model_dump()
        )
        return PostingFBSRestrictionsResponse(**response["result"])