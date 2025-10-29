import pytest

from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import FBSPostingProductExemplarValidateResponse


class TestFBSPostingProductExemplarValidate:
    """Тесты для метода fbs_posting_product_exemplar_validate."""

    @pytest.mark.asyncio
    async def test_fbs_posting_product_exemplar_validate(self, api, mock_api_request):
        """Тестирует метод fbs_posting_product_exemplar_validate."""

        mock_response_data = {
            "products": [
                {
                    "error": None,
                    "exemplars": [
                        {
                            "errors": [],
                            "gtd": "10714440/110922/0012345/1",
                            "marks": [
                                {
                                    "errors": [],
                                    "mark": "010460406349100021N4O0B5A8B1",
                                    "mark_type": "mandatory_mark",
                                    "valid": True
                                }
                            ],
                            "rnpt": "RNPT123456789",
                            "valid": True,
                            "weight": 1.5
                        }
                    ],
                    "product_id": 123456789,
                    "valid": True
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import (
            FBSPostingProductExemplarValidateRequest,
            FBSPostingProductExemplarValidateProduct,
            ProductExemplarBase,
            ProductExemplarMark
        )

        request = FBSPostingProductExemplarValidateRequest(
            posting_number="43658312-0011-1",
            products=[
                FBSPostingProductExemplarValidateProduct(
                    product_id=123456789,
                    exemplars=[
                        ProductExemplarBase(
                            gtd="10714440/110922/0012345/1",
                            marks=[
                                ProductExemplarMark(
                                    mark="010460406349100021N4O0B5A8B1",
                                    mark_type="mandatory_mark"
                                )
                            ],
                            rnpt="RNPT123456789",
                            weight=1.5
                        )
                    ]
                )
            ]
        )

        response = await api.fbs_posting_product_exemplar_validate(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v5",
            endpoint="fbs/posting/product/exemplar/validate",
            payload=request.model_dump()
        )

        assert isinstance(response, FBSPostingProductExemplarValidateResponse)
        assert len(response.products) == 1

        product = response.products[0]
        assert product.product_id == 123456789
        assert product.valid is True
        assert product.error is None

        assert len(product.exemplars) == 1
        exemplar = product.exemplars[0]
        assert exemplar.gtd == "10714440/110922/0012345/1"
        assert exemplar.rnpt == "RNPT123456789"
        assert exemplar.weight == 1.5
        assert exemplar.valid is True
        assert exemplar.errors == []

        assert len(exemplar.marks) == 1
        mark = exemplar.marks[0]
        assert mark.mark == "010460406349100021N4O0B5A8B1"
        assert mark.mark_type == "mandatory_mark"
        assert mark.valid is True
        assert mark.errors == []

    @pytest.mark.asyncio
    async def test_fbs_posting_product_exemplar_validate_with_errors(self, api, mock_api_request):
        """Тестирует метод fbs_posting_product_exemplar_validate с ошибками валидации."""

        mock_response_data = {
            "products": [
                {
                    "error": "VALIDATION_ERROR",
                    "exemplars": [
                        {
                            "errors": ["INVALID_GTD_FORMAT"],
                            "gtd": "invalid_gtd_format",
                            "marks": [
                                {
                                    "errors": ["INVALID_MARK_LENGTH"],
                                    "mark": "010460406349100021N4O0B5A8B",
                                    "mark_type": "mandatory_mark",
                                    "valid": False
                                }
                            ],
                            "rnpt": "RNPT123456789",
                            "valid": False,
                            "weight": 1.5
                        }
                    ],
                    "product_id": 123456789,
                    "valid": False
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import (
            FBSPostingProductExemplarValidateRequest,
            FBSPostingProductExemplarValidateProduct,
            ProductExemplarBase,
            ProductExemplarMark
        )

        request = FBSPostingProductExemplarValidateRequest(
            posting_number="43658312-0011-1",
            products=[
                FBSPostingProductExemplarValidateProduct(
                    product_id=123456789,
                    exemplars=[
                        ProductExemplarBase(
                            gtd="invalid_gtd_format",
                            marks=[
                                ProductExemplarMark(
                                    mark="010460406349100021N4O0B5A8B",  # Неправильная длина
                                    mark_type="mandatory_mark"
                                )
                            ],
                            rnpt="RNPT123456789",
                            weight=1.5
                        )
                    ]
                )
            ]
        )

        response = await api.fbs_posting_product_exemplar_validate(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v5",
            endpoint="fbs/posting/product/exemplar/validate",
            payload=request.model_dump()
        )

        assert isinstance(response, FBSPostingProductExemplarValidateResponse)
        product = response.products[0]
        assert product.valid is False
        assert product.error == "VALIDATION_ERROR"

        exemplar = product.exemplars[0]
        assert exemplar.valid is False
        assert exemplar.errors == ["INVALID_GTD_FORMAT"]

        mark = exemplar.marks[0]
        assert mark.valid is False
        assert mark.errors == ["INVALID_MARK_LENGTH"]