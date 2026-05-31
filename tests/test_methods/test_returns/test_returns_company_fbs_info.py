import pytest

from src.ozonapi.seller.schemas.returns import (
    ReturnsCompanyFbsInfoRequest,
    ReturnsCompanyFbsInfoResponse,
)
from src.ozonapi.seller.schemas.returns.v1__returns_company_fbs_info import (
    ReturnsCompanyFbsInfoPagination,
)


class TestReturnsCompanyFbsInfo:
    """Тесты для метода returns_company_fbs_info."""

    @pytest.mark.asyncio
    async def test_returns_company_fbs_info(self, api, mock_api_request):
        """Тестирует метод returns_company_fbs_info."""

        mock_response_data = {
            "has_next": False,
            "drop_off_points": [
                {
                    "id": 1,
                    "name": "ПВЗ",
                    "address": "ул. Пушкина",
                    "box_count": 2,
                    "returns_count": 5,
                    "pass_info": {"count": 1, "is_required": True},
                    "warehouses_ids": ["555"]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = ReturnsCompanyFbsInfoRequest(
            pagination=ReturnsCompanyFbsInfoPagination(limit=100)
        )

        response = await api.returns_company_fbs_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="returns/company/fbs/info",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnsCompanyFbsInfoResponse)
        assert response.drop_off_points[0].returns_count == 5
        assert response.drop_off_points[0].pass_info.is_required is True
