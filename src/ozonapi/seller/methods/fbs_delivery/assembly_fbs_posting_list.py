from ...core import APIManager
from ...schemas.fbs_delivery import (
    AssemblyFbsPostingListRequest,
    AssemblyFbsPostingListResponse,
)


class AssemblyFbsPostingListMixin(APIManager):
    """Реализует метод /v1/assembly/fbs/posting/list"""

    async def assembly_fbs_posting_list(
            self: "AssemblyFbsPostingListMixin",
            request: AssemblyFbsPostingListRequest
    ) -> AssemblyFbsPostingListResponse:
        """Метод для получения списка отправлений.

        Notes:
            • Возвращает отправления, доступные для сборки, со списком товаров.
            • Использует курсорную пагинацию: передавайте `cursor` из предыдущего ответа.
            • Направление сортировки `sort_dir` (`ASC`/`DESC`) обязательно.
            • В фильтре необходимо передать `cutoff_from` и `cutoff_to`; фильтровать
              рекомендуется по ним (передача `delivery_method_id` может вызывать
              ошибку на стороне Ozon).

        References:
            https://docs.ozon.ru/api/seller/#operation/AssemblyAPI_AssemblyFbsPostingList

        Args:
            request: Запрос на получение списка отправлений по схеме `AssemblyFbsPostingListRequest`

        Returns:
            Список отправлений по схеме `AssemblyFbsPostingListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.assembly_fbs_posting_list(
                    AssemblyFbsPostingListRequest(
                        filter=AssemblyFbsPostingListFilter(),
                        limit=100,
                        sort_dir="ASC"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="assembly/fbs/posting/list",
            payload=request.model_dump()
        )
        return AssemblyFbsPostingListResponse(**response)
