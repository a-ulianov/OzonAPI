from ...core import APIManager
from ...schemas.beta import SellerInfoResponse


class SellerInfoMixin(APIManager):
    """Реализует метод /v1/seller/info"""

    async def seller_info(
            self: "SellerInfoMixin",
    ) -> SellerInfoResponse:
        """Метод для получения информации о кабинете продавца, рейтингах и подписке.

        Notes:
            • Метод не требует передачи параметров в теле запроса.
            • Возвращает полную информацию о компании продавца, включая реквизиты и налоговую систему.
            • Предоставляет данные о рейтингах продавца с текущими и предыдущими значениями, включая статусы опасности и участия в Premium-программе.
            • Содержит информацию о подписке продавца, включая тип подписки и статус Premium-доступа.
            • Рейтинги могут иметь различные типы значений: индекс, процент, время, коэффициент, оценка или счёт.
            • Статусы рейтингов могут быть: OK (хороший), WARNING (требует внимания), CRITICAL (критичный).

        References:
            https://docs.ozon.ru/api/seller/?#operation/SellerAPI_SellerInfo

        Returns:
            Ответ с информацией о кабинете продавца по схеме `SellerInfoResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.seller_info()

            # Пример использования полученных данных:
            company_name = result.company.name
            inn = result.company.inn
            currency = result.company.currency
            tax_system = result.company.tax_system

            # Работа с рейтингами
            for rating in result.ratings:
                rating_name = rating.name
                current_value = rating.current_value.value
                current_status = rating.current_value.status

            # Проверка подписки
            if result.subscription:
                has_premium = result.subscription.is_premium
                subscription_type = result.subscription.type
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller/info",
            payload={},
        )
        return SellerInfoResponse(**response)