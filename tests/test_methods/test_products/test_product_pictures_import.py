import pytest

from src.ozonapi.seller.schemas.products import ProductPicturesImportResponse, ProductPicturesImportRequest


class TestProductPicturesImport:
    """Тесты для метода product_pictures_import."""

    @pytest.mark.asyncio
    async def test_product_pictures_import(self, api, mock_api_request):
        """Тестирует метод product_pictures_import."""
        mock_response_data = {
            "result": {
                "pictures": [
                    {
                        "is_360": True,
                        "is_color": False,
                        "is_primary": True,
                        "product_id": 123456789,
                        "state": "imported",
                        "url": "https://example.com/image1.jpg"
                    },
                    {
                        "is_360": False,
                        "is_color": True,
                        "is_primary": False,
                        "product_id": 123456789,
                        "state": "imported",
                        "url": "https://example.com/color.jpg"
                    }
                ]
            }
        }
        mock_api_request.return_value = mock_response_data

        request = ProductPicturesImportRequest(
            product_id=123456789,
            color_image="https://example.com/color.jpg",
            images=[
                "https://example.com/image1.jpg",
                "https://example.com/image2.jpg",
            ],
            images360=[
                "https://example.com/360_1.jpg",
            ]
        )
        response = await api.product_pictures_import(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/pictures/import",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductPicturesImportResponse)
        assert len(response.result.pictures) == 2
        assert response.result.pictures[0].product_id == 123456789
        assert response.result.pictures[0].state == "imported"
        assert response.result.pictures[0].is_primary is True
        assert response.result.pictures[1].is_color is True
