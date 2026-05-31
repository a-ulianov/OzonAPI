from ...core import APIManager
from ...schemas.fbs_delivery import (
    PostingFBSActGetPDFRequest,
    PostingFBSActGetPDFResponse,
)


class PostingFBSActGetPDFMixin(APIManager):
    """Реализует метод /v2/posting/fbs/act/get-pdf"""

    async def posting_fbs_act_get_pdf(
            self: "PostingFBSActGetPDFMixin",
            request: PostingFBSActGetPDFRequest
    ) -> PostingFBSActGetPDFResponse:
        """Метод для получения PDF c документами по отгрузке.

        Notes:
            • Возвращает PDF-файл; его содержимое доступно в поле `content` в виде байтов.
            • Документы формируются методом `posting_fbs_act_create()`; готовность —
              `posting_fbs_act_check_status()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSGetAct

        Args:
            request: Запрос на получение PDF по схеме `PostingFBSActGetPDFRequest`

        Returns:
            PDF-файл с документами по схеме `PostingFBSActGetPDFResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_act_get_pdf(
                    PostingFBSActGetPDFRequest(
                        id=12345
                    )
                )
                with open("act.pdf", "wb") as f:
                    f.write(result.content)
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/get-pdf",
            payload=request.model_dump(),
            response_format="binary"
        )
        return PostingFBSActGetPDFResponse(**response)
