from unicodedata import category

from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey, \
    func
from app.core.db import Base


class Products(Base):
    shop_id = Column(ForeignKey('shops.id'))
    category_id = Column(ForeignKey("categories.id"), nullable=False)
    product_name = Column(String(100), unique=True, nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, )
    created_at = Column(DateTime, default=func.now(), nullable=False)
