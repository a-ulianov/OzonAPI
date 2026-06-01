import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesGetRequest,
    CargoesGetResponse,
)


class TestCargoesGet:
    """Тесты для метода cargoes_get."""

    @pytest.mark.asyncio
    async def test_cargoes_get(self, api, mock_api_request):
        """Тестирует метод cargoes_get."""

        mock_api_request.return_value = {
            "supply": [
                {
                    "bundle_id": "b1",
                    "supply_id": 123,
                    "cargoes": [
                        {
                            "cargo_id": 1,
                            "content_type": "SKU",
                            "placement_zone_type": "COLD",
                            "type": "BOX",
                            "tracking_info": {
                                "date": "2026-06-01T00:00:00Z",
                                "status": "ACCEPTED",
                                "type": "ARRIVAL",
                            },
                        }
                    ],
                }
            ]
        }

        request = CargoesGetRequest(supply_ids=["123"])

        response = await api.cargoes_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/get",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesGetResponse)
        assert response.supply[0].supply_id == 123
        assert response.supply[0].cargoes[0].cargo_id == 1
