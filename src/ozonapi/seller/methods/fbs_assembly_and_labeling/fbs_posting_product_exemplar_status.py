from ...core import APIManager
from ...schemas.fbs_assembly_and_labeling import (
    FBSPostingProductExemplarStatusRequest,
    FBSPostingProductExemplarStatusResponse
)


class FBSPostingProductExemplarStatusMixin(APIManager):
    """Реализует метод /v5/fbs/posting/product/exemplar/status"""

    async def fbs_posting_product_exemplar_status(
            self: "FBSPostingProductExemplarStatusMixin",
            request: FBSPostingProductExemplarStatusRequest
    ) -> FBSPostingProductExemplarStatusResponse:
        """Метод для получения статусов добавления экземпляров, переданных в методе `/v6/fbs/posting/product/exemplar/set`.

        Notes:
            • Метод возвращает статусы проверки экземпляров и данные по этим экземплярам.
            • Для отправлений после сборки статус указывает на возможность редактирования данных по экземплярам.
            • Изменяйте данные по экземплярам для отправлений в статусе «Ожидает отгрузки» с помощью методов:
              - `fbs_posting_product_exemplar_set()`
              - `fbs_posting_product_exemplar_update()`

        References:
            https://docs.ozon.ru/api/seller/?#operation/PostingAPI_FbsPostingProductExemplarStatusV5

        Args:
            request: Запрос на получение статусов экземпляров по схеме `FBSPostingProductExemplarStatusRequest`

        Returns:
            Статусы проверки экземпляров и данные по ним по схеме `FBSPostingProductExemplarStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbs_posting_product_exemplar_status(
                    FBSPostingProductExemplarStatusRequest(
                        posting_number="43658312-0011-1"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v5",
            endpoint="fbs/posting/product/exemplar/status",
            payload=request.model_dump()
        )
        return FBSPostingProductExemplarStatusResponse(**response)