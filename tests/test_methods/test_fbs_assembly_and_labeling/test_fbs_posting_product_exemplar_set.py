import pytest

from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import FBSPostingProductExemplarSetResponse


class TestFBSPostingProductExemplarSet:
    """Тесты для метода fbs_posting_product_exemplar_set."""

    @pytest.mark.asyncio
    async def test_fbs_posting_product_exemplar_set(self, api, mock_api_request):
        """Тестирует метод fbs_posting_product_exemplar_set."""

        mock_response_data = {
            "code": None,
            "details": [],
            "message": None
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import FBSPostingProductExemplarSetRequest

        request_data = {
            "posting_number": "43658312-0011-1",
            "multi_box_qty": 1,
            "products": [
                {
                    "product_id": 123456789,
                    "exemplars": [
                        {
                            "exemplar_id": 1,
                            "gtd": "10714440/110922/0012345/1",
                            "is_gtd_absent": False,
                            "is_rnpt_absent": True,
                            "marks": [
                                {
                                    "mark": "010460406349100021N4O0B5A8B1",
                                    "mark_type": "mandatory_mark"
                                }
                            ],
                            "rnpt": None,
                            "weight": 1.5
                        }
                    ]
                }
            ]
        }

        request = FBSPostingProductExemplarSetRequest(**request_data)

        response = await api.fbs_posting_product_exemplar_set(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v6",
            endpoint="fbs/posting/product/exemplar/set",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FBSPostingProductExemplarSetResponse)
        assert response.code is None
        assert response.message is None
        assert response.details == []