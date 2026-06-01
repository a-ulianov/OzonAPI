import pytest

from src.ozonapi.seller.schemas.fbo import (
    PostingFBOListRequest,
    PostingFBOListResponse,
)


class TestPostingFBOList:
    """Тесты для метода posting_fbo_list (канонический v3)."""

    @pytest.mark.asyncio
    async def test_posting_fbo_list(self, api, mock_api_request):
        """Тестирует метод posting_fbo_list."""

        mock_api_request.return_value = {
            "cursor": "next-cursor",
            "has_next": True,
            "postings": [
                {
                    "additional_data": [{"key": "k", "value": "v"}],
                    "analytics_data": {
                        "city": "Москва",
                        "delivery_type": "courier",
                        "is_legal": False,
                        "is_premium": True,
                        "payment_type_group_name": "card",
                        "warehouse_id": 123,
                        "warehouse_name": "Основной склад",
                    },
                    "cancellation": {
                        "cancel_reason": "",
                        "cancellation_initiator": "",
                        "cancellation_type": "",
                    },
                    "created_at": "2026-05-01T10:00:00Z",
                    "external_order": {"is_external": False, "platform_name": ""},
                    "financial_data": {
                        "cluster_from": "Москва",
                        "cluster_to": "Санкт-Петербург",
                        "products": [
                            {
                                "actions": ["promo"],
                                "commission": {
                                    "amount": 10.5,
                                    "currency": "RUB",
                                    "percent": 5,
                                },
                                "old_price": 2000.0,
                                "payout": 1800.0,
                                "price": 1900.0,
                                "product_id": 555,
                                "total_discount_percent": 5.0,
                                "total_discount_value": 100.0,
                            }
                        ],
                    },
                    "legal_info": {"company_name": "ООО", "inn": "1", "kpp": "2"},
                    "order_id": 777,
                    "order_number": "ORDER-1",
                    "posting_number": "0001-1",
                    "products": [
                        {
                            "digital_codes": [],
                            "is_marketplace_buyout": False,
                            "name": "Товар",
                            "offer_id": "art-1",
                            "price": {"amount": "1900.0000", "currency": "RUB"},
                            "quantity": 1,
                            "sku": 999,
                        }
                    ],
                    "status": "delivered",
                    "substatus": "posting_delivered",
                }
            ],
        }

        request = PostingFBOListRequest(
            limit=100,
            filter={"since": "2026-05-01T00:00:00Z", "to": "2026-06-01T00:00:00Z"},
            sort_dir="ASC",
            with_={"analytics_data": True, "financial_data": True, "legal_info": True},
        )

        response = await api.posting_fbo_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="posting/fbo/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBOListResponse)
        assert response.has_next is True
        assert response.cursor == "next-cursor"
        posting = response.postings[0]
        assert posting.posting_number == "0001-1"
        assert posting.financial_data.products[0].commission.amount == 10.5
        assert posting.products[0].price.amount == "1900.0000"
        assert posting.legal_info.inn == "1"
        # `with` and `to` reserved words serialised via alias
        payload = request.model_dump(by_alias=True)
        assert "with" in payload
        assert "to" in payload["filter"]
