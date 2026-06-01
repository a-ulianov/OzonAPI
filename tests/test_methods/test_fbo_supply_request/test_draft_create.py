import pytest

from src.ozonapi.seller.common.enumerations.fbo_supply_request import SupplyCreateType
from src.ozonapi.seller.schemas.fbo_supply_request import (
    DraftCreateItem,
    DraftCreateRequest,
    DraftCreateResponse,
)


class TestDraftCreate:
    """Тесты для метода draft_create."""

    @pytest.mark.asyncio
    async def test_draft_create(self, api, mock_api_request):
        """Тестирует метод draft_create."""

        mock_api_request.return_value = {"operation_id": "op-123"}

        request = DraftCreateRequest(
            items=[DraftCreateItem(sku=123, quantity=10)],
            type=SupplyCreateType.DIRECT,
        )

        response = await api.draft_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="draft/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DraftCreateResponse)
        assert response.operation_id == "op-123"
