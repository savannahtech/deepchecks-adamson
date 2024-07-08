from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(String, index=True)
    output_text = Column(String, index=True)
    input_metric = Column(Float)
    output_metric = Column(Float)

    alerts = relationship("Alert", back_populates="interaction")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class InteractionCreate(BaseModel):
    input_text: str
    output_text: str
