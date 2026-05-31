import pytest

from src.ozonapi.seller.schemas.fbs_containers import (
    CarriageContainerLabelGetRequest,
    CarriageContainerLabelGetResponse,
)


class TestCarriageContainerLabelGet:
    """Тесты для метода carriage_container_label_get."""

    @pytest.mark.asyncio
    async def test_carriage_container_label_get(self, api, mock_api_request):
        """Тестирует метод carriage_container_label_get."""

        mock_response_data = {
            "content": {
                "content_type": "application/pdf",
                "file_content": "JVBERi0xLjQK...",
                "file_name": "labels.pdf"
            },
            "error_containers": []
        }
        mock_api_request.return_value = mock_response_data

        request = CarriageContainerLabelGetRequest(container_ids=["12345"])

        response = await api.carriage_container_label_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/container/label/get",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageContainerLabelGetResponse)
        assert response.content.file_name == "labels.pdf"
