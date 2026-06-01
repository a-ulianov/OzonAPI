import pytest

from src.ozonapi.seller.common.enumerations.orders import (
    OrderDeliverySchema,
    OrderDeliveryType,
)
from src.ozonapi.seller.schemas.orders import (
    OrderCreateDateRange,
    OrderCreateDeliveryMethod,
    OrderCreateItem,
    OrderCreateRequest,
    OrderCreateResponse,
    OrderCreateSplit,
)


class TestOrderCreate:
    """Тесты для метода order_create."""

    @pytest.mark.asyncio
    async def test_order_create(self, api, mock_api_request):
        """Тестирует метод order_create."""

        mock_api_request.return_value = {
            "order_number": "789-012",
            "postings": ["789-012-1"],
        }

        request = OrderCreateRequest(
            delivery_schema=OrderDeliverySchema.FBS,
            splits=[
                OrderCreateSplit(
                    warehouse_id=1,
                    delivery_method=OrderCreateDeliveryMethod(
                        delivery_type=OrderDeliveryType.COURIER,
                        logistic_date_range=OrderCreateDateRange(
                            from_="2026-06-01T00:00:00Z",
                            to_="2026-06-02T00:00:00Z",
                        ),
                    ),
                    items=[OrderCreateItem(sku=10, quantity=1)],
                )
            ],
        )

        response = await api.order_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="order/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, OrderCreateResponse)
        assert response.order_number == "789-012"
        # alias "from"/"to" emitted in payload
        payload = request.model_dump(by_alias=True)
        date_range = payload["splits"][0]["delivery_method"]["logistic_date_range"]
        assert "from" in date_range and "to" in date_range
