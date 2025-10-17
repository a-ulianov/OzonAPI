"""
Асинхронный интерфейс для взаимодействия с API маркетплейса Ozon.
"""

__version__ = "0.2.0"
__author__ = "Alexander Ulianov"
__repository__ = "https://github.com/a-ulianov/OzonAPI"
__docs__ = "https://github.com/a-ulianov/OzonAPI#readme"
__issues__ = "https://github.com/a-ulianov/OzonAPI/issues"

__all__ = ["SellerAPI", "SellerAPIConfig", ]

from .seller import SellerAPI, SellerAPIConfig