from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, func
from sqlalchemy.orm import relationship

from app.core.db import Base


class FavoriteProducts(Base):
    __tablename__ = 'favorite_products'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'),
                        nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), nullable=False)

    user = relationship("Users", back_populates="favorite_products")
    product = relationship("Products", back_populates="favorited_by")
