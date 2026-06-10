from sqlalchemy import Column,Integer,String,Table,ForeignKey,Float,Date,Boolean
from persistence.db_configuration import Base
from sqlalchemy.orm import relationship
from car import car_accessories

class Accessories(Base):
    __tablename__ = "accessories"
 
    
    id_accessories = Column(Integer, primary_key=True, autoincrement=True)
    accessories_brand = Column(String(50), nullable=False)
    year_production = Column(Date, nullable=True)
    price = Column(Float, nullable=False)  
 
    
    compatible_car_components = relationship(
        'Car',
        secondary=car_accessories,
        back_populates='accessories'
    )
 
    
    def __repr__(self):
        return f"Accessories(id={self.id_accessories}, brand={self.accessories_brand})"
 
    def __str__(self):
        return f"{self.accessories_brand} - €{self.price}"