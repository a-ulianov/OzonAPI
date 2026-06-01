from ...core import APIManager
from ...schemas.rfbs_delivery import (
    PostingCutoffSetRequest,
    PostingCutoffSetResponse,
)


class PostingCutoffSetMixin(APIManager):
    """Реализует метод /v1/posting/cutoff/set"""

    async def posting_cutoff_set(
            self: "PostingCutoffSetMixin",
            request: PostingCutoffSetRequest
    ) -> PostingCutoffSetResponse:
        """Уточняет дату отгрузки отправления rFBS.

        Notes:
            • Задаёт новую дату отгрузки `new_cutoff_date` для отправления.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_SetPostingCutoff

        Args:
            request: Запрос уточнения по схеме `PostingCutoffSetRequest`

        Returns:
            Результат уточнения по схеме `PostingCutoffSetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_cutoff_set(
                    PostingCutoffSetRequest(
                        posting_number="123-456-1",
                        new_cutoff_date="2026-06-02T00:00:00Z",
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/cutoff/set",
            payload=request.model_dump(by_alias=True)
        )
        return PostingCutoffSetResponse(**response)
