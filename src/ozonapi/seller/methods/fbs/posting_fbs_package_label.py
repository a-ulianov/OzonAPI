from ...core import APIManager
from ...schemas.fbs import PostingFBSPackageLabelRequest, PostingFBSPackageLabelResponse


class PostingFBSPackageLabelMixin(APIManager):
    """Реализует метод /v2/posting/fbs/package-label"""

    async def posting_fbs_package_label(
            self: "PostingFBSPackageLabelMixin",
            request: PostingFBSPackageLabelRequest
    ) -> PostingFBSPackageLabelResponse:
        """Метод для генерации PDF-файла с этикетками для указанных отправлений.

        Notes:
            • Метод применим только для отправлений в статусе «Ожидает отгрузки» — `awaiting_deliver`.
            • В одном запросе можно передать не больше `20` идентификаторов отправлений.
            • Если хотя бы для одного отправления возникнет ошибка, этикетки не будут подготовлены для всех отправлений в запросе.
            • Рекомендуется запрашивать этикетки через 45–60 секунд после сборки заказа.
            • Ошибка `The next postings aren't ready` означает, что этикетки ещё не готовы — повторите запрос позднее.
            • Для работы по схемам rFBS или rFBS Express изучите процесс печати этикетки в Базе знаний продавца (https://seller-edu.ozon.ru/rfbs/scheme-of-work).

        References:
            https://docs.ozon.ru/api/seller/?#operation/PostingAPI_PostingFBSPackageLabel

        Args:
            request: Запрос на получение PDF-файла с этикетками по схеме `PostingFBSPackageLabelRequest`

        Returns:
            PDF-файл с этикетками в бинарном виде по схеме `PostingFBSPackageLabelResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_package_label(
                    PostingFBSPackageLabelRequest(
                        posting_number=["48173252-0034-4", ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/package-label",
            payload=request.model_dump()
        )
        return PostingFBSPackageLabelResponse(**response)