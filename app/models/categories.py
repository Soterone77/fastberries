from sqlalchemy import Column, DateTime, String
from app.core.db import Base


class Categories(Base):
    category_name = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
