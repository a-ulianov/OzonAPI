from ...core import APIManager
from ...schemas.digital import (
    PostingDigitalCodesUploadRequest,
    PostingDigitalCodesUploadResponse,
)


class PostingDigitalCodesUploadMixin(APIManager):
    """Реализует метод /v1/posting/digital/codes/upload"""

    async def posting_digital_codes_upload(
            self: "PostingDigitalCodesUploadMixin",
            request: PostingDigitalCodesUploadRequest
    ) -> PostingDigitalCodesUploadResponse:
        """Загружает коды цифровых товаров для отправления.

        Notes:
            • Количество кодов в `exemplar_keys` должно совпадать с `exemplar_qty`.
            • Коды, которые передать нельзя, учитываются в `not_available_exemplar_qty`.
            • В ответе по каждому SKU возвращается количество принятых/отклонённых
              кодов и список ошибок `failed_exemplars`.

        References:
            https://docs.ozon.ru/api/seller/#operation/UploadPostingCodes

        Args:
            request: Запрос на загрузку кодов по схеме `PostingDigitalCodesUploadRequest`

        Returns:
            Результат загрузки кодов по схеме `PostingDigitalCodesUploadResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_digital_codes_upload(
                    PostingDigitalCodesUploadRequest(
                        posting_number="0001-1",
                        exemplars_by_sku=[{
                            "sku": 123456,
                            "exemplar_qty": 1,
                            "not_available_exemplar_qty": 0,
                            "exemplar_keys": ["CODE-1"]
                        }]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/digital/codes/upload",
            payload=request.model_dump()
        )
        return PostingDigitalCodesUploadResponse(**response)
