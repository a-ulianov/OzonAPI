"""Общие сущности состояния отмены поставки FBP."""
from typing import Optional

from pydantic import BaseModel, Field


class FbpCancellationError(BaseModel):
    """Ошибка отмены поставки FBP.

    Attributes:
        error_code: Код ошибки отмены (`CODE_UNSPECIFIED`, `NO_RESPONSE_FROM_3PF`,
            `ACCEPTANCE_ALREADY_STARTED`)
        message: Текст ошибки
    """

    error_code: Optional[str] = Field(
        None,
        description="Код ошибки отмены. Известные значения: `CODE_UNSPECIFIED`, "
                    "`NO_RESPONSE_FROM_3PF`, `ACCEPTANCE_ALREADY_STARTED` "
                    "(набор открытый — тип `str`)."
    )
    message: Optional[str] = Field(
        None, description="Текст ошибки отмены."
    )


class FbpCancellationState(BaseModel):
    """Состояние отмены поставки FBP.

    Attributes:
        cancellation_error: Ошибка отмены
        cancellation_status: Статус отмены (`STATUS_UNSPECIFIED`, `CONFIRMATION`,
            `CANCELED`, `NOT_CANCELED`)
    """

    cancellation_error: Optional[FbpCancellationError] = Field(
        None, description="Ошибка отмены поставки."
    )
    cancellation_status: Optional[str] = Field(
        None,
        description="Статус отмены. Известные значения: `STATUS_UNSPECIFIED`, "
                    "`CONFIRMATION`, `CANCELED`, `NOT_CANCELED` "
                    "(набор открытый — тип `str`)."
    )
