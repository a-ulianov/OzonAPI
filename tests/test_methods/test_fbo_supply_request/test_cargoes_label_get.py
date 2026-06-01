import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesLabelGetRequest,
    CargoesLabelGetResponse,
)


class TestCargoesLabelGet:
    """Тесты для метода cargoes_label_get."""

    @pytest.mark.asyncio
    async def test_cargoes_label_get(self, api, mock_api_request):
        """Тестирует метод cargoes_label_get."""

        mock_api_request.return_value = {
            "result": {
                "file_guid": "guid-1",
                "file_url": "https://ozon.ru/labels.pdf",
            },
            "status": "SUCCESS",
            "errors": {"error_reasons": []},
        }

        request = CargoesLabelGetRequest(operation_id="op-lbl-1")

        response = await api.cargoes_label_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes-label/get",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesLabelGetResponse)
        assert response.result.file_guid == "guid-1"
        assert response.status == "SUCCESS"
