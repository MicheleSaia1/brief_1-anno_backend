from sqlalchemy import Column, Integer, String, Table, ForeignKey,Date,Float
from persistence.db_configuration import Base
from sqlalchemy.orm import relationship
from car import car_engine


class Engine(Base):
    __tablename__ = "engine"
 
    id_engine = Column(Integer, primary_key=True, autoincrement=True)
    brand_engine = Column(String(50), nullable=False)
    production_year = Column(Date, nullable=True)
    displacement_cc = Column(Integer, nullable=True)   # cilindrata 
    horsepower = Column(Integer, nullable=True)        # cavalli 
 
   
    price = Column(Float, nullable=False)
 
    
    compatible_car_components = relationship(
        'Car',
        secondary=car_engine,
        back_populates='engine'
    )
 
    def __repr__(self):
        return f"Engine(id={self.id_engine}, brand={self.brand_engine}, hp={self.horsepower})"
 
    def __str__(self):
        return f"{self.brand_engine} {self.horsepower}cv - €{self.price}"
 