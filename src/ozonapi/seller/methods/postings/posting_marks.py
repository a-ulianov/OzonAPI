from ...core import APIManager
from ...schemas.postings import (
    PostingMarksRequest,
    PostingMarksResponse,
)


class PostingMarksMixin(APIManager):
    """Реализует метод /v1/posting/marks"""

    async def posting_marks(
            self: "PostingMarksMixin",
            request: PostingMarksRequest
    ) -> PostingMarksResponse:
        """Возвращает маркировки экземпляров из отправлений.

        Notes:
            • Для каждого отправления возвращаются экземпляры с полученными маркировками
              (`issued_exemplars`) и без них (`non_issued_exemplars`).
            • В `invalid_postings` попадают номера отправлений, по которым не удалось
              получить данные.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingMarks

        Args:
            request: Запрос маркировок по схеме `PostingMarksRequest`

        Returns:
            Маркировки экземпляров отправлений по схеме `PostingMarksResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_marks(
                    PostingMarksRequest(posting_numbers=["0001-1", "0002-1"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/marks",
            payload=request.model_dump()
        )
        return PostingMarksResponse(**response)
