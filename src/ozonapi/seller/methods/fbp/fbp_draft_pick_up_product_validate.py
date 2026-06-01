from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftPickUpProductValidateRequest,
    FbpDraftPickUpProductValidateResponse,
)


class FbpDraftPickUpProductValidateMixin(APIManager):
    """Реализует метод /v1/fbp/draft/pick-up/product/validate"""

    async def fbp_draft_pick_up_product_validate(
            self: "FbpDraftPickUpProductValidateMixin",
            request: FbpDraftPickUpProductValidateRequest,
    ) -> FbpDraftPickUpProductValidateResponse:
        """Провалидирует список товаров для pick-up поставки.

        Notes:
            • Возвращает принятые и отклонённые товары; при успехе формируется набор
              (`bundle_generated`, `bundle_id`).

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftPickUpProductValidate

        Args:
            request: Список товаров по схеме `FbpDraftPickUpProductValidateRequest`

        Returns:
            Результат проверки по схеме `FbpDraftPickUpProductValidateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_pick_up_product_validate(
                    FbpDraftPickUpProductValidateRequest(
                        skus=[FbpProductValidateSkuItem(sku=123456, count=2)],
                        warehouse_id=123,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/pick-up/product/validate",
            payload=request.model_dump(),
        )
        return FbpDraftPickUpProductValidateResponse(**response)
