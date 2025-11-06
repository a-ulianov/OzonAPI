import pytest

from src.ozonapi.seller.schemas.fbo import PostingFBOGetResponse


class TestPostingFBOGet:
    """Тесты для метода posting_fbo_get."""

    @pytest.mark.asyncio
    async def test_posting_fbo_get(self, api, mock_api_request):
        """Тестирует метод posting_fbo_get."""

        mock_response_data = {
            "result": {
                "order_id": 354679434,
                "order_number": "50520644-0012",
                "posting_number": "50520644-0012-7",
                "status": "delivered",
                "cancel_reason_id": 0,
                "created_at": "2021-09-01T00:34:56.563Z",
                "in_process_at": "2021-09-01T00:34:56.103Z",
                "legal_info": {
                    "company_name": "ООО Ромашка",
                    "inn": "1234567890",
                    "kpp": "123456789"
                },
                "products": [
                    {
                        "sku": 254665483,
                        "name": "Мочалка натуральная из люфы с деревянной ручкой",
                        "quantity": 1,
                        "offer_id": "PS1033",
                        "price": "137.00",
                        "is_marketplace_buyout": True,
                        "digital_codes": [],
                        "currency_code": "RUB"
                    }
                ],
                "analytics_data": {
                    "city": "Москва",
                    "delivery_type": "Courier",
                    "is_premium": False,
                    "payment_type_group_name": "Карты оплаты",
                    "warehouse_id": 15431806189000,
                    "warehouse_name": "ХОРУГВИНО_РФЦ",
                    "is_legal": False
                },
                "financial_data": {
                    "products": [
                        {
                            "commission_amount": 13.7,
                            "commission_percent": 10,
                            "payout": 123.3,
                            "product_id": 254665483,
                            "currency_code": "RUB",
                            "old_price": 198,
                            "price": 137,
                            "total_discount_value": 61,
                            "total_discount_percent": 30.81,
                            "actions": [
                                "Системная виртуальная скидка селлера"
                            ],
                            "quantity": 0
                        }
                    ]
                },
                "additional_data": []
            }
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbo import PostingFBOGetRequest
        from src.ozonapi.seller.schemas.entities.postings import PostingFilterWith

        request = PostingFBOGetRequest(
            posting_number="50520644-0012-7",
            translit=True,
            with_=PostingFilterWith(
                analytics_data=True,
                financial_data=True,
                legal_info=True
            )
        )

        response = await api.posting_fbo_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbo/get",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBOGetResponse)
        assert response.result is not None

        posting = response.result
        assert posting.posting_number == "50520644-0012-7"
        assert posting.order_id == 354679434
        assert posting.order_number == "50520644-0012"
        assert posting.status == "delivered"
        assert posting.cancel_reason_id == 0

        # Проверка аналитических данных
        assert posting.analytics_data is not None
        assert posting.analytics_data.warehouse_id == 15431806189000
        assert posting.analytics_data.warehouse_name == "ХОРУГВИНО_РФЦ"
        assert posting.analytics_data.delivery_type == "Courier"
        assert posting.analytics_data.is_legal is False
        assert posting.analytics_data.city == "Москва"
        assert posting.analytics_data.is_premium is False
        assert posting.analytics_data.payment_type_group_name == "Карты оплаты"

        # Проверка финансовых данных
        assert posting.financial_data is not None
        assert len(posting.financial_data.products) == 1
        financial_product = posting.financial_data.products[0]
        assert financial_product.product_id == 254665483
        assert financial_product.commission_amount == 13.7
        assert financial_product.payout == 123.3
        assert financial_product.currency_code == "RUB"
        assert financial_product.old_price == 198
        assert financial_product.price == 137
        assert financial_product.total_discount_value == 61
        assert financial_product.total_discount_percent == 30.81
        assert financial_product.quantity == 0
        assert financial_product.actions == ["Системная виртуальная скидка селлера"]

        # Проверка юридической информации
        assert posting.legal_info is not None
        assert posting.legal_info.company_name == "ООО Ромашка"
        assert posting.legal_info.inn == "1234567890"
        assert posting.legal_info.kpp == "123456789"

        # Проверка товаров
        assert len(posting.products) == 1
        product = posting.products[0]
        assert product.sku == 254665483
        assert product.offer_id == "PS1033"
        assert product.name == "Мочалка натуральная из люфы с деревянной ручкой"
        assert product.price == 137.00
        assert product.quantity == 1
        assert product.is_marketplace_buyout is True
        assert product.digital_codes == []
        assert product.currency_code == "RUB"