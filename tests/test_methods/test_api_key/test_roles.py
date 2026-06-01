import pytest

from src.ozonapi.seller.schemas.api_key import RolesResponse


class TestRoles:
    """Тесты для метода roles."""

    @pytest.mark.asyncio
    async def test_roles(self, api, mock_api_request):
        """Тестирует метод roles."""
        mock_response_data = {
            "expires_at": "2026-12-31T23:59:59Z",
            "roles": [
                {
                    "name": "Admin",
                    "methods": [
                        "/v1/roles",
                        "/v1/seller/info",
                    ],
                },
                {
                    "name": "ReadOnly",
                    "methods": [
                        "/v1/seller/info",
                    ],
                },
            ],
        }
        mock_api_request.return_value = mock_response_data

        response = await api.roles()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="roles",
            payload={},
        )
        assert isinstance(response, RolesResponse)
        assert response.expires_at == "2026-12-31T23:59:59Z"
        assert len(response.roles) == 2
        assert response.roles[0].name == "Admin"
        assert response.roles[0].methods == ["/v1/roles", "/v1/seller/info"]
        assert response.roles[1].name == "ReadOnly"
