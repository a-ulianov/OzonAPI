__all__ = ["SellerApiKeyAPI", ]

from .roles import RolesMixin


class SellerApiKeyAPI(
    RolesMixin,
):
    """Реализует методы раздела «Информация по API-ключу».

    References:
        https://docs.ozon.ru/api/seller/#tag/APIkey
    """
    pass
