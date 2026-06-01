import pytest

from src.ozonapi.seller.common.enumerations.fbo_supply_request import SupplyDeliveryType
from src.ozonapi.seller.schemas.fbo_supply_request import (
    DraftMultiClusterCreateRequest,
    DraftTypedClusterInfo,
    DraftTypedCreateResponse,
    DraftTypedDeliveryInfo,
    DraftTypedItem,
)


class TestDraftMultiClusterCreate:
    """Тесты для метода draft_multi_cluster_create."""

    @pytest.mark.asyncio
    async def test_draft_multi_cluster_create(self, api, mock_api_request):
        """Тестирует метод draft_multi_cluster_create."""

        mock_api_request.return_value = {"draft_id": 999, "errors": []}

        request = DraftMultiClusterCreateRequest(
            clusters_info=[
                DraftTypedClusterInfo(
                    items=[DraftTypedItem(sku=123, quantity=10)],
                    macrolocal_cluster_id=1,
                ),
                DraftTypedClusterInfo(
                    items=[DraftTypedItem(sku=456, quantity=5)],
                    macrolocal_cluster_id=2,
                ),
            ],
            delivery_info=DraftTypedDeliveryInfo(type=SupplyDeliveryType.PICKUP),
        )

        response = await api.draft_multi_cluster_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="draft/multi-cluster/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DraftTypedCreateResponse)
        assert response.draft_id == 999
