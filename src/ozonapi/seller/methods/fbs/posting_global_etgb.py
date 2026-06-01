from ...core import APIManager
from ...schemas.fbs import PostingGlobalEtgbRequest, PostingGlobalEtgbResponse


class PostingGlobalEtgbMixin(APIManager):
    """Реализует метод /v1/posting/global/etgb"""

    async def posting_global_etgb(
            self: "PostingGlobalEtgbMixin",
            request: PostingGlobalEtgbRequest
    ) -> PostingGlobalEtgbResponse:
        """Возвращает таможенные декларации ETGB для трансграничных отправлений.

        Notes:
            • По каждому отправлению возвращается номер, дата и ссылка на декларацию.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetEtgb

        Args:
            request: Запрос деклараций по схеме `PostingGlobalEtgbRequest`

        Returns:
            Декларации ETGB по схеме `PostingGlobalEtgbResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_global_etgb(
                    PostingGlobalEtgbRequest(
                        date=PostingGlobalEtgbDate(
                            from_="2026-05-01T00:00:00Z", to_="2026-06-01T00:00:00Z"
                        )
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/global/etgb",
            payload=request.model_dump(by_alias=True)
        )
        return PostingGlobalEtgbResponse(**response)
