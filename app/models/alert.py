from sqlalchemy import Column, Integer, String, Float, ForeignKey

from sqlalchemy.orm import relationship
from app.database import Base


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    interaction_id = Column(Integer, ForeignKey('interactions.id'))
    element = Column(String)
    metric_value = Column(Float)
    alert_type = Column(String)

    interaction = relationship("Interaction", back_populates="alerts")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
