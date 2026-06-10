from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from persistence.db_configuration import Base


class Car_Configuration(Base):
    __tablename__ = "car_configuration"
 
    id_configuration = Column(Integer, primary_key=True, autoincrement=True)
 
    
    created_at = Column(DateTime, default=datetime, nullable=False)
    total_price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    car_id = Column(Integer, ForeignKey('car.car_id'), nullable=False)
    quote_id = Column(Integer, ForeignKey('quote.id'), nullable=False)
 
    user = relationship('User')
    car = relationship('Car')
    quote = relationship('Quote', back_populates='configuration', uselist=False)
 
    def __repr__(self):
        return f"Car_Configuration(id={self.id_configuration}, car_id={self.car_id}, total={self.total_price})"
 
    def __str__(self):
        return f"Configurazione #{self.id_configuration} - {self.car.car_brand} {self.car.car_model} - €{self.total_price}"
 


