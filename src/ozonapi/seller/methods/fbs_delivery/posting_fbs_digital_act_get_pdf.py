from ...core import APIManager
from ...schemas.fbs_delivery import (
    PostingFBSDigitalActGetPDFRequest,
    PostingFBSDigitalActGetPDFResponse,
)


class PostingFBSDigitalActGetPDFMixin(APIManager):
    """Реализует метод /v2/posting/fbs/digital/act/get-pdf"""

    async def posting_fbs_digital_act_get_pdf(
            self: "PostingFBSDigitalActGetPDFMixin",
            request: PostingFBSDigitalActGetPDFRequest
    ) -> PostingFBSDigitalActGetPDFResponse:
        """Метод для получения листа отгрузки по перевозке.

        Notes:
            • Возвращает PDF-файл; его содержимое доступно в поле `content` в виде байтов.
            • Тип документа выбирается параметром `doc_type` (лист отгрузки, акт о
              расхождениях, акт об излишках, транспортная накладная).

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetDigitalAct

        Args:
            request: Запрос на получение PDF по схеме `PostingFBSDigitalActGetPDFRequest`

        Returns:
            PDF-файл листа отгрузки по схеме `PostingFBSDigitalActGetPDFResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_digital_act_get_pdf(
                    PostingFBSDigitalActGetPDFRequest(
                        id=12345,
                        doc_type="act_of_acceptance"
                    )
                )
                with open("waybill.pdf", "wb") as f:
                    f.write(result.content)
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/digital/act/get-pdf",
            payload=request.model_dump(),
            response_format="binary"
        )
        return PostingFBSDigitalActGetPDFResponse(**response)
