import pytest

from src.ozonapi.seller.schemas.fbs_delivery import CarriageEttnStatusRequest, CarriageEttnStatusResponse


class TestCarriageEttnStatus:
    """Тесты для метода carriage_ettn_status."""

    @pytest.mark.asyncio
    async def test_carriage_ettn_status(self, api, mock_api_request):
        """Тестирует метод carriage_ettn_status."""

        mock_response_data = {"status": "checked", "errors": []}
        mock_api_request.return_value = mock_response_data

        request = CarriageEttnStatusRequest(carriage_id=12345)

        response = await api.carriage_ettn_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/ettn/status",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageEttnStatusResponse)
        assert response.status == "checked"
