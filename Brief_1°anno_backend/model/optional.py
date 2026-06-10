from sqlalchemy import Column,Integer,String,Table,ForeignKey,Float,Boolean,Date
from persistence.db_configuration import Base
from sqlalchemy.orm import relationship
from car import car_optional


class Optional(Base):
    __tablename__ = "optional"
 
    id_optional = Column(Integer, primary_key=True, autoincrement=True)
    brand_optional = Column(String(50), nullable=False)
    production_year = Column(Date, nullable=True)
    price = Column(Float, nullable=False)
 
    
 
    compatible_car_components = relationship(
        'Car',
        secondary=car_optional,
        back_populates='optional'
    )
 
    def __repr__(self):
        return f"Optional(id={self.id_optional}, brand={self.brand_optional})"
 
    def __str__(self):
        return f"{self.brand_optional} - €{self.price}"
 