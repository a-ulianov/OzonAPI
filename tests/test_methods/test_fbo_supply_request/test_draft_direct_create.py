import pytest

from src.ozonapi.seller.common.enumerations.fbo_supply_request import SupplyDeleteSkuMode
from src.ozonapi.seller.schemas.fbo_supply_request import (
    DraftDirectCreateRequest,
    DraftTypedClusterInfo,
    DraftTypedCreateResponse,
    DraftTypedItem,
)


class TestDraftDirectCreate:
    """Тесты для метода draft_direct_create."""

    @pytest.mark.asyncio
    async def test_draft_direct_create(self, api, mock_api_request):
        """Тестирует метод draft_direct_create."""

        mock_api_request.return_value = {
            "draft_id": 888,
            "errors": [
                {
                    "error_message": "VALIDATION_ERROR",
                    "error_reasons": ["UNSPECIFIED"],
                    "items_validation": [
                        {
                            "macrolocal_cluster_id": 1,
                            "rejected_items": [
                                {"reasons": ["ITEM_UNAVAILABLE"], "sku": 999}
                            ],
                        }
                    ],
                    "macrolocal_cluster_ids": ["1"],
                    "message": "ошибка",
                    "skus": ["999"],
                }
            ],
        }

        request = DraftDirectCreateRequest(
            cluster_info=DraftTypedClusterInfo(
                items=[DraftTypedItem(sku=123, quantity=10)],
                macrolocal_cluster_id=1,
            ),
            deletion_sku_mode=SupplyDeleteSkuMode.PARTIAL,
        )

        response = await api.draft_direct_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="draft/direct/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DraftTypedCreateResponse)
        assert response.draft_id == 888
        assert response.errors[0].items_validation[0].rejected_items[0].sku == 999
