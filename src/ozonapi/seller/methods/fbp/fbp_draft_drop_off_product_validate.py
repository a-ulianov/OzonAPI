from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDropOffProductValidateRequest,
    FbpDraftDropOffProductValidateResponse,
)


class FbpDraftDropOffProductValidateMixin(APIManager):
    """Реализует метод /v1/fbp/draft/drop-off/product/validate"""

    async def fbp_draft_drop_off_product_validate(
            self: "FbpDraftDropOffProductValidateMixin",
            request: FbpDraftDropOffProductValidateRequest,
    ) -> FbpDraftDropOffProductValidateResponse:
        """Проверяет список товаров, которые склад партнёра может принять.

        Notes:
            • Возвращает принятые и отклонённые товары; при успехе формируется набор
              (`bundle_generated`, `bundle_id`).

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDropOffProductValidate

        Args:
            request: Список товаров по схеме `FbpDraftDropOffProductValidateRequest`

        Returns:
            Результат проверки по схеме `FbpDraftDropOffProductValidateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_drop_off_product_validate(
                    FbpDraftDropOffProductValidateRequest(
                        skus=[FbpProductValidateSkuItem(sku=123456, count=2)],
                        warehouse_id=123,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/product/validate",
            payload=request.model_dump(),
        )
        return FbpDraftDropOffProductValidateResponse(**response)
