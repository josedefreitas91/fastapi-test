from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from app.database.base_class import Base


class Tokens(Base):
    access_token = Column(String, primary_key=True, nullable=False)
    expires_in = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())