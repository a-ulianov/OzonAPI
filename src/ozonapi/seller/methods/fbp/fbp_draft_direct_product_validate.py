from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDirectProductValidateRequest,
    FbpDraftDirectProductValidateResponse,
)


class FbpDraftDirectProductValidateMixin(APIManager):
    """Реализует метод /v1/fbp/draft/direct/product/validate"""

    async def fbp_draft_direct_product_validate(
            self: "FbpDraftDirectProductValidateMixin",
            request: FbpDraftDirectProductValidateRequest,
    ) -> FbpDraftDirectProductValidateResponse:
        """Проверяет список товаров для склада партнёра.

        Notes:
            • Возвращает принятые и отклонённые товары; при успехе формируется набор
              (`bundle_generated`, `bundle_id`) для дальнейшего создания черновика.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDirectProductValidate

        Args:
            request: Список товаров по схеме `FbpDraftDirectProductValidateRequest`

        Returns:
            Результат проверки по схеме `FbpDraftDirectProductValidateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_direct_product_validate(
                    FbpDraftDirectProductValidateRequest(
                        skus=[FbpProductValidateSkuItem(sku=123456, count=2)],
                        warehouse_id=123,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/product/validate",
            payload=request.model_dump(),
        )
        return FbpDraftDirectProductValidateResponse(**response)
