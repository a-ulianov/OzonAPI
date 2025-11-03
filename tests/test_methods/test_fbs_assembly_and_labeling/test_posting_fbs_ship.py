import pytest

from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import PostingFBSShipResponse


class TestPostingFBSShip:
    """Тесты для метода posting_fbs_ship."""

    @pytest.mark.asyncio
    async def test_posting_fbs_ship(self, api, mock_api_request):
        """Тестирует метод posting_fbs_ship."""

        mock_response_data = {
            "additional_data": [
                {
                    "posting_number": "89491381-0072-1",
                    "products": [
                        {
                            "currency_code": "RUB",
                            "mandatory_mark": ["123"],
                            "name": "Тестовый товар",
                            "offer_id": "17125",
                            "price": 2000.0,
                            "quantity": 2,
                            "sku": 185479045
                        }
                    ]
                }
            ],
            "result": ["89491381-0072-1"]
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import (
            PostingFBSShipRequest,
            PostingFBSShipProducts,
            PostingFBSShipProduct
        )

        request = PostingFBSShipRequest(
            posting_number="89491381-0072-1",
            packages=[
                PostingFBSShipProducts(
                    products=[
                        PostingFBSShipProduct(
                            product_id=185479045,
                            quantity=2
                        )
                    ]
                )
            ]
        )

        response = await api.posting_fbs_ship(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v4",
            endpoint="posting/fbs/ship",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSShipResponse)
        assert response.result == ["89491381-0072-1"]
        assert len(response.additional_data) == 1

        additional_data = response.additional_data[0]
        assert additional_data.posting_number == "89491381-0072-1"
        assert len(additional_data.products) == 1

        product = additional_data.products[0]
        assert product.currency_code == "RUB"
        assert product.mandatory_mark == ["123"]
        assert product.name == "Тестовый товар"
        assert product.offer_id == "17125"
        assert product.price == 2000.0
        assert product.quantity == 2
        assert product.sku == 185479045