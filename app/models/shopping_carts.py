from sqlalchemy import Column, String, DateTime, ForeignKey, func, Integer
from app.core.db import Base


class ShoppingCarts(Base):
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), nullable=False)




