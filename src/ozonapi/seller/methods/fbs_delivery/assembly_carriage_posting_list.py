from ...core import APIManager
from ...schemas.fbs_delivery import (
    AssemblyCarriagePostingListRequest,
    AssemblyCarriagePostingListResponse,
)


class AssemblyCarriagePostingListMixin(APIManager):
    """Реализует метод /v1/assembly/carriage/posting/list"""

    async def assembly_carriage_posting_list(
            self: "AssemblyCarriagePostingListMixin",
            request: AssemblyCarriagePostingListRequest
    ) -> AssemblyCarriagePostingListResponse:
        """Метод для получения списка отправлений в отгрузке.

        Notes:
            • Возвращает отправления отгрузки со списком товаров и кодами листов подбора.
            • Использует курсорную пагинацию: передавайте `cursor` из предыдущего ответа.
            • В фильтре необходимо передать `cutoff_from` и `cutoff_to`
              (иначе API вернёт ошибку валидации).

        References:
            https://docs.ozon.ru/api/seller/#operation/AssemblyAPI_AssemblyCarriagePostingList

        Args:
            request: Запрос на получение списка отправлений по схеме `AssemblyCarriagePostingListRequest`

        Returns:
            Список отправлений в отгрузке по схеме `AssemblyCarriagePostingListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.assembly_carriage_posting_list(
                    AssemblyCarriagePostingListRequest(
                        filter=AssemblyCarriagePostingListFilter(carriage_id=12345),
                        limit=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="assembly/carriage/posting/list",
            payload=request.model_dump()
        )
        return AssemblyCarriagePostingListResponse(**response)
