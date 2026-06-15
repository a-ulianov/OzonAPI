import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesDeleteRequest,
    CargoesDeleteResponse,
)


class TestCargoesDelete:
    """Тесты для метода cargoes_delete (v2)."""

    @pytest.mark.asyncio
    async def test_cargoes_delete(self, api, mock_api_request):
        """Тестирует метод cargoes_delete."""

        mock_api_request.return_value = {
            "operation_id": "op-del-1",
            "errors": {
                "cargo_error_reasons": [],
                "supply_error_reasons": [],
                "transport_cargo_error_reasons": [],
            },
        }

        request = CargoesDeleteRequest(
            supply_id=123,
            cargo_ids=["1", "2"],
            transport_cargo_deletion_type="UNBIND_CONTAINED_CARGOES",
        )

        response = await api.cargoes_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="cargoes/delete",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesDeleteResponse)
        assert response.operation_id == "op-del-1"
