from ...core import APIManager
from ...schemas.fbs import (
    PostingFBSPackageLabelCreateV1Request,
    PostingFBSPackageLabelCreateV1Response,
)


class PostingFBSPackageLabelCreateV1Mixin(APIManager):
    """Реализует метод /v1/posting/fbs/package-label/create"""

    async def posting_fbs_package_label_create_v1(
            self: "PostingFBSPackageLabelCreateV1Mixin",
            request: PostingFBSPackageLabelCreateV1Request
    ) -> PostingFBSPackageLabelCreateV1Response:
        """Создаёт задание на формирование этикеток для отправлений (версия 1).

        Notes:
            • Устаревшая версия 1: возвращает один `task_id`. Рекомендуется
              использовать `posting_fbs_package_label_create()` (v2).
            • Готовые этикетки получайте методом `posting_fbs_package_label_get()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_CreateLabelBatch

        Args:
            request: Запрос по схеме `PostingFBSPackageLabelCreateV1Request`

        Returns:
            Идентификатор задания по схеме `PostingFBSPackageLabelCreateV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_package_label_create_v1(
                    PostingFBSPackageLabelCreateV1Request(posting_number=["123-456-1"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/package-label/create",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBSPackageLabelCreateV1Response(**response)
