import pytest

from src.ozonapi.seller.schemas.fbs_containers import (
    CarriageContainerDocumentGetRequest,
    CarriageContainerDocumentGetResponse,
)


class TestCarriageContainerDocumentGet:
    """Тесты для метода carriage_container_document_get."""

    @pytest.mark.asyncio
    async def test_carriage_container_document_get(self, api, mock_api_request):
        """Тестирует метод carriage_container_document_get."""

        mock_response_data = {
            "content_type": "application/pdf",
            "file_content": "JVBERi0xLjQK...",
            "file_name": "carriage.pdf"
        }
        mock_api_request.return_value = mock_response_data

        request = CarriageContainerDocumentGetRequest(container_ids=["12345"])

        response = await api.carriage_container_document_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/container/document/get",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageContainerDocumentGetResponse)
        assert response.file_name == "carriage.pdf"
        assert response.file_content == "JVBERi0xLjQK..."
