from datetime import datetime
# from typing import TYPE_CHECKING
from sqlalchemy import Boolean, Column, DateTime, Integer, String
# from sqlalchemy.orm import relationship
from app.database.base_class import Base

# if TYPE_CHECKING:
#     from .item import Item  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    # items = relationship("Item", back_populates="owner")


# class BaseTimestamps:
#     id: Any
#     __name__: str
#     created_at: datetime = datetime.now()
#     updated_at: datetime = datetime.now()

#     @declared_attr # type: ignore
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()
    
#     class Config:
#         validate_assignment = True

#     @root_validator
#     def number_validator(cls, values):
#         if values["updated_at"]:
#             values["updated_at"] = datetime.now()
#         else:
#             values["updated_at"] = values["created_at"]
#         return values
