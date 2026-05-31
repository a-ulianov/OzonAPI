from ...core import APIManager
from ...schemas.questions import (
    QuestionChangeStatusRequest,
    QuestionChangeStatusResponse,
)


class QuestionChangeStatusMixin(APIManager):
    """Реализует метод /v1/question/change-status"""

    async def question_change_status(
            self: "QuestionChangeStatusMixin",
            request: QuestionChangeStatusRequest
    ) -> QuestionChangeStatusResponse:
        """Метод для изменения статуса вопросов.

        Notes:
            • Переводит указанные вопросы в статус `NEW`, `VIEWED` или `PROCESSED`.
            • Доступен продавцам с подпиской Premium Plus (раздел Вопросы-ответы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Question_ChangeStatus

        Args:
            request: Запрос на изменение статуса по схеме `QuestionChangeStatusRequest`

        Returns:
            Результат изменения статуса по схеме `QuestionChangeStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.question_change_status(
                    QuestionChangeStatusRequest(
                        question_ids=["q-1"],
                        status="PROCESSED"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="question/change-status",
            payload=request.model_dump()
        )
        return QuestionChangeStatusResponse(**response)
