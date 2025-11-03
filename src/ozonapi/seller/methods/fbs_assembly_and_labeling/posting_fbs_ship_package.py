from ...core import APIManager
from ...schemas.fbs_assembly_and_labeling import (
    PostingFBSShipPackageRequest,
    PostingFBSShipPackageResponse
)


class PostingFBSShipPackageMixin(APIManager):
    """Реализует метод /v4/posting/fbs/ship/package"""

    async def posting_fbs_ship_package(
            self: "PostingFBSShipPackageMixin",
            request: PostingFBSShipPackageRequest
    ) -> PostingFBSShipPackageResponse:
        """Метод для частичной сборки отправления FBS.

        Notes:
            • Метод выполняет частичную сборку отправления, позволяя разделить первичное отправление на несколько частей.
            • Если в запросе передать только часть товаров из отправления, метод разделит первичное отправление на две части:
              - В первичном несобранном отправлении останутся товары, которые не были переданы в запросе.
              - Будет создано новое отправление с переданными в запросе товарами.
            • По умолчанию статус созданных отправлений устанавливается в `awaiting_packaging` — ожидает сборки.
            • Статус изначального отправления изменится только после изменения статуса отправлений, на которые он разделился.
            • Ответ с кодом 200 не гарантирует успешную сборку отправления. Для проверки статуса используйте метод `posting_fbs_get()`.
            • Если в ответе метода `posting_fbs_get()` указан `result.substatus = PostingSubstatus.SHIP_FAILED`,
              повторите сборку отправления.
            • Для работы с экземплярами товаров используйте поле `exemplars_ids` для передачи идентификаторов экземпляров.
            • Всегда передавайте полный набор данных по товарам, которые должны быть включены в новое отправление.

        References:
            https://docs.ozon.com/api/seller/?#operation/PostingAPI_ShipFbsPostingV4

        Args:
            request: Запрос на частичную сборку отправления по схеме `PostingFBSShipPackageRequest`

        Returns:
            Ответ с номерами сформированных отправлений по схеме `PostingFBSShipPackageResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_ship_package(
                    PostingFBSShipPackageRequest(
                        posting_number="89491381-0072-1",
                        products=[
                            PostingFBSShipPackageProduct(
                                product_id="185479045",
                                quantity=1,
                                exemplars_ids=["12345"]
                            ),
                            PostingFBSShipPackageProduct(
                                product_id="185479046",
                                quantity=1,
                                exemplars_ids=["12347"]
                            )
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v4",
            endpoint="posting/fbs/ship/package",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBSShipPackageResponse(**response)