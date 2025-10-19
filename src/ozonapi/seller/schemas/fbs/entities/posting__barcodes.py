from pydantic import BaseModel, Field


class PostingFBSBarcodes(BaseModel):
    """Штрихкоды отправления.

    Attributes:
        lower_barcode: Нижний штрихкод на маркировке отправления
        upper_barcode: Верхний штрихкод на маркировке отправления
    """
    lower_barcode: str = Field(
        ..., description="Нижний штрихкод на маркировке отправления."
    )
    upper_barcode: str = Field(
        ..., description="Верхний штрихкод на маркировке отправления."
    )