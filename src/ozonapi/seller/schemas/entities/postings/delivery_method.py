from pydantic import BaseModel, Field


class PostingDeliveryMethod(BaseModel):
    """Метод доставки."""
    id: int = Field(
        ..., description="Идентификатор метода доставки."
    )
    name: str = Field(
        ..., description="Название метода доставки."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )
