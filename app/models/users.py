from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey, \
    func
from app.core.db import Base


class Users(Base):
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), nullable=False)
    password_hash = Column(Text, nullable=False)
    status = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    favorite_product_id = Column(ForeignKey('products.id'))
