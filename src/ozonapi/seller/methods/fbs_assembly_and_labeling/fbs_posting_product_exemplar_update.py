from ...core import APIManager
from ...schemas.fbs_assembly_and_labeling import (
    FBSPostingProductExemplarUpdateRequest,
    FBSPostingProductExemplarUpdateResponse
)


class FBSPostingProductExemplarUpdateMixin(APIManager):
    """Реализует метод /v1/fbs/posting/product/exemplar/update"""

    async def fbs_posting_product_exemplar_update(
            self: "FBSPostingProductExemplarUpdateMixin",
            request: FBSPostingProductExemplarUpdateRequest
    ) -> FBSPostingProductExemplarUpdateResponse:
        """Метод для сохранения обновлённых данных по экземплярам для отправлений в статусе «Ожидает отгрузки».

        Notes:
            • Используйте этот метод после передачи информации по экземплярам методом
              `fbs_posting_product_exemplar_set()` для сохранения обновлённых данных.
            • Метод применяется только для отправлений в статусе «Ожидает отгрузки».
            • После вызова этого метода обновлённые данные экземпляров сохраняются в системе
              и становятся актуальными для дальнейшей обработки отправления.
            • Для получения статусов проверки экземпляров используйте метод `fbs_posting_product_exemplar_status()`.
            • Для первоначальной передачи данных об экземплярах используйте метод `fbs_posting_product_exemplar_set()`.
            • Для предварительной проверки корректности данных используйте метод `fbs_posting_product_exemplar_validate()`.

        References:
            https://docs.ozon.com/api/seller/?#operation/PostingAPI_FbsPostingProductExemplarUpdate

        Args:
            request: Запрос на обновление данных экземпляров по схеме `FBSPostingProductExemplarUpdateRequest`

        Returns:
            Ответ API с подтверждением операции по схеме `FBSPostingProductExemplarUpdateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbs_posting_product_exemplar_update(
                    FBSPostingProductExemplarUpdateRequest(
                        posting_number="43658312-0011-1"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbs/posting/product/exemplar/update",
            payload=request.model_dump()
        )
        return FBSPostingProductExemplarUpdateResponse(**response)