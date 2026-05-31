import pytest

from src.ozonapi.seller.schemas.fbs_containers import (
    CarriageContainerCreateRequest,
    CarriageContainerCreateResponse,
)


class TestCarriageContainerCreate:
    """Тесты для метода carriage_container_create."""

    @pytest.mark.asyncio
    async def test_carriage_container_create(self, api, mock_api_request):
        """Тестирует метод carriage_container_create."""

        mock_response_data = {"container_ids": ["111", "222"]}
        mock_api_request.return_value = mock_response_data

        request = CarriageContainerCreateRequest(
            cargo_type="box", containers_count=2, sort_type="sort", warehouse_id=12345
        )

        response = await api.carriage_container_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/container/create",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageContainerCreateResponse)
        assert response.container_ids == ["111", "222"]
