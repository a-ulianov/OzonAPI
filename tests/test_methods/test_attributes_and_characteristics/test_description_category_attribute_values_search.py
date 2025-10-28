import pytest

from src.ozonapi.seller.schemas.attributes_and_characteristics import DescriptionCategoryAttributeValuesSearchResponse, \
    DescriptionCategoryAttributeValuesSearchRequest


class TestDescriptionCategoryAttributeValuesSearch:
    """Тесты для метода description_category_attribute_values_search."""

    @pytest.mark.asyncio
    async def test_description_category_attribute_values_search(self, api, mock_api_request):
        """Тестирует метод description_category_attribute_values_search."""

        mock_response_data = {
            "result": [
                {
                    "id": 1,
                    "info": "Красивый цвет",
                    "picture": "https://example.com/beauty.jpg",
                    "value": "Красота"
                },
                {
                    "id": 2,
                    "info": "Очень красивый цвет",
                    "picture": "https://example.com/very-beauty.jpg",
                    "value": "Очень красивый"
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = DescriptionCategoryAttributeValuesSearchRequest(
            attribute_id=85,
            description_category_id=200000933,
            type_id=93080,
            value="Красота",
            limit=50
        )
        response = await api.description_category_attribute_values_search(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="description-category/attribute/values/search",
            payload=request.model_dump()
        )
        assert isinstance(response, DescriptionCategoryAttributeValuesSearchResponse)
        assert len(response.result) == 2
        assert response.result[0].value == "Красота"
        assert response.result[1].value == "Очень красивый"