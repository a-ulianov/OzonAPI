"""https://docs.ozon.ru/api/seller/#operation/AccessAPI_RolesByToken"""
from typing import Optional

from pydantic import BaseModel, Field


class Role(BaseModel):
    """Роль и доступные ей методы API.

    Attributes:
        name: Название роли
        methods: Список адресов методов, доступных роли
    """

    name: Optional[str] = Field(
        None, description="Название роли."
    )
    methods: list[str] = Field(
        default_factory=list,
        description="Список адресов методов API, доступных роли."
    )


class RolesResponse(BaseModel):
    """Схема ответа со списком ролей и методов, доступных по API-ключу.

    Attributes:
        expires_at: Дата и время истечения срока действия API-ключа
        roles: Список ролей с доступными методами
    """

    expires_at: Optional[str] = Field(
        None,
        description="Дата и время истечения срока действия API-ключа в формате RFC3339."
    )
    roles: list[Role] = Field(
        default_factory=list,
        description="Список ролей с доступными им методами API."
    )
