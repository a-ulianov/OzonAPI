from ...core import APIManager
from ...schemas.fbs_assembly_and_labeling import (
    FBSPostingProductExemplarValidateRequest,
    FBSPostingProductExemplarValidateResponse
)


class FBSPostingProductExemplarValidateMixin(APIManager):
    """Реализует метод /v5/fbs/posting/product/exemplar/validate"""

    async def fbs_posting_product_exemplar_validate(
            self: "FBSPostingProductExemplarValidateMixin",
            request: FBSPostingProductExemplarValidateRequest
    ) -> FBSPostingProductExemplarValidateResponse:
        """Метод для проверки кодов на соответствие требованиям системы «Честный ЗНАК».

        Notes:
            • Метод проверяет коды маркировки на соответствие требованиям системы «Честный ЗНАК»
              по количеству и составу символов, а также других маркировок.
            • Проверяются следующие типы маркировок:
              - mandatory_mark — обязательная маркировка «Честный ЗНАК»;
              - jw_uin — уникальный идентификационный номер (УИН) ювелирного изделия;
              - imei — IMEI мобильного устройства.
            • Если у вас нет номера грузовой таможенной декларации (ГТД), вы можете его не указывать.
            • Метод возвращает детальную информацию о результатах валидации для каждого экземпляра
              и каждой маркировки, включая список ошибок.
            • Для каждого товара, экземпляра и маркировки указывается результат проверки (valid = true/false).
            • Используйте этот метод для предварительной проверки данных перед отправкой через
              метод `fbs_posting_product_exemplar_set()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingProductExemplarValidateV5

        Args:
            request: Запрос на валидацию кодов маркировки по схеме `FBSPostingProductExemplarValidateRequest`

        Returns:
            Ответ с результатами валидации по схеме `FBSPostingProductExemplarValidateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbs_posting_product_exemplar_validate(
                    FBSPostingProductExemplarValidateRequest(
                        posting_number="43658312-0011-1",
                        products=[
                            FBSPostingProductExemplarValidateProduct(
                                product_id=123456789,
                                exemplars=[
                                    FBSPostingProductExemplarBase(
                                        gtd="10714440/110922/0012345/1",
                                        marks=[
                                            ProductExemplarMark(
                                                mark="010460406349100021N4O0B5A8B1",
                                                mark_type=MarkType.MANDATORY_MARK
                                            )
                                        ],
                                        rnpt="RNPT123456789",
                                        weight=1.5
                                    )
                                ]
                            )
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v5",
            endpoint="fbs/posting/product/exemplar/validate",
            payload=request.model_dump()
        )
        return FBSPostingProductExemplarValidateResponse(**response)