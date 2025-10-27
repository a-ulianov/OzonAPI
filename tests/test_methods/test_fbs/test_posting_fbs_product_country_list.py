import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSProductCountryListResponse


class TestPostingFBSProductCountryList:
    """Тесты для метода posting_fbs_product_country_list."""

    @pytest.mark.asyncio
    async def test_posting_fbs_product_country_list(self, api, mock_api_request):
        """Тестирует метод posting_fbs_product_country_list и его кеширование."""

        mock_response_data = {
            "result": [
                {
                    "name": "Турция",
                    "country_iso_code": "TR"
                },
                {
                    "name": "Туркменистан",
                    "country_iso_code": "TM"
                },
                {
                    "name": "Тунис",
                    "country_iso_code": "TN"
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_product_country_list import (
            PostingFBSProductCountryListRequest
        )

        request = PostingFBSProductCountryListRequest(
            name_search="тУрЦ"
        )

        # Первый вызов - должен выполнить запрос к API
        response1 = await api.posting_fbs_product_country_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/product/country/list",
            json=request.model_dump(by_alias=True)
        )

        assert isinstance(response1, PostingFBSProductCountryListResponse)
        assert len(response1.result) == 3

        first_country = response1.result[0]
        second_country = response1.result[1]
        third_country = response1.result[2]

        assert first_country.name == "Турция"
        assert first_country.country_iso_code == "TR"
        assert second_country.name == "Туркменистан"
        assert second_country.country_iso_code == "TM"
        assert third_country.name == "Тунис"
        assert third_country.country_iso_code == "TN"

        # Второй вызов с теми же параметрами - должен вернуть закешированный результат
        response2 = await api.posting_fbs_product_country_list(request)

        # Проверяем, что метод _request был вызван только один раз (кеширование работает)
        assert mock_api_request.call_count == 1

        # Проверяем, что результаты одинаковые
        assert response1 == response2
        assert len(response2.result) == 3
        assert response2.result[0].name == "Турция"
        assert response2.result[0].country_iso_code == "TR"
