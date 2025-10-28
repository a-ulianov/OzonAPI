import datetime

import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSGetByBarcodeResponse


class TestPostingFBSGetByBarcode:
    """Тесты для метода posting_fbs_get_by_barcode."""

    @pytest.mark.asyncio
    async def test_posting_fbs_get_by_barcode(self, api, mock_api_request):
        """Тестирует метод posting_fbs_get_by_barcode."""
        mock_response_data = {
            "result": {
                "barcodes": {
                    "upper_barcode": "%101%10293145035",
                    "lower_barcode": "201864523528000"
                },
                "cancel_reason_id": 0,
                "created_at": "2025-01-29T08:58:07Z",
                "in_process_at": "2025-01-29T08:59:40Z",
                "order_id": 47558522075,
                "order_number": "2130415463-0013",
                "posting_number": "2130415463-0013-1",
                "products": [
                    {
                        "sku": 498274975,
                        "name": "Стульчик для кормления ребенка",
                        "quantity": 1,
                        "offer_id": "6460551001",
                        "price": "2300.0000"
                    }
                ],
                "shipment_date": "2025-01-29T18:00:00Z",
                "status": "delivered"
            }
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_get_by_barcode import PostingFBSGetByBarcodeRequest

        request = PostingFBSGetByBarcodeRequest(
            barcode="20325804886000"
        )

        response = await api.posting_fbs_get_by_barcode(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/get-by-barcode",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSGetByBarcodeResponse)
        assert response.posting_number == "2130415463-0013-1"
        assert response.order_id == 47558522075
        assert response.order_number == "2130415463-0013"
        assert response.status == "delivered"
        assert response.cancel_reason_id == 0
        assert response.barcodes.upper_barcode == "%101%10293145035"
        assert response.barcodes.lower_barcode == "201864523528000"
        assert len(response.products) == 1

        product = response.products[0]
        assert product.sku == 498274975
        assert product.name == "Стульчик для кормления ребенка"
        assert product.quantity == 1
        assert product.offer_id == "6460551001"
        assert product.price == 2300.00

        assert response.created_at.replace(tzinfo=None) == datetime.datetime(2025, 1, 29, 8, 58, 7)
        assert response.in_process_at.replace(tzinfo=None) == datetime.datetime(2025, 1, 29, 8, 59, 40)
        assert response.shipment_date.replace(tzinfo=None) == datetime.datetime(2025, 1, 29, 18, 0, 0)
