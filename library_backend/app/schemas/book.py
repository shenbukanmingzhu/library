from pydantic import BaseModel, field_validator
import re

class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str
    stock: int
    category_id: int = None

    @field_validator('isbn')
    def isbn_valid(cls, v):
        if not re.match(r'^\d{10}(\d{3})?$', v):
            raise ValueError('ISBN必须是10位或13位数字')
        return v

    @field_validator('stock')
    def stock_non_negative(cls, v):
        if v < 0:
            raise ValueError('库存不能为负数')
        return v