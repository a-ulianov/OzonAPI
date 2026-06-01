from ...core import APIManager
from ...schemas.api_key import RolesResponse


class RolesMixin(APIManager):
    """Реализует метод /v1/roles"""

    async def roles(
            self: "RolesMixin",
    ) -> RolesResponse:
        """Метод для получения списка ролей и методов, доступных по API-ключу.

        Notes:
            • Метод не требует передачи параметров в теле запроса.
            • Возвращает дату истечения срока действия API-ключа и список ролей.
            • Каждая роль содержит название и список адресов доступных методов API.
            • Позволяет проверить, к каким методам у текущего API-ключа есть доступ.

        References:
            https://docs.ozon.ru/api/seller/?#operation/AccessAPI_RolesByToken

        Returns:
            Ответ со списком ролей и методов по схеме `RolesResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.roles()

            # Дата истечения срока действия ключа
            expires_at = result.expires_at

            # Перебор ролей и доступных методов
            for role in result.roles:
                role_name = role.name
                available_methods = role.methods
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="roles",
            payload={},
        )
        return RolesResponse(**response)
