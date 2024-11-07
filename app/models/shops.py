from sqlalchemy import Column, String, DateTime, ForeignKey, func
from app.core.db import Base


class Shops(Base):
    shop_name = Column(String(100), unique=True, nullable=False)
    owner_id = Column(ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        default=func.now(), nullable=False)


