from sqlalchemy import Column,Integer,String,Table,ForeignKey,Float
from persistence.db_configuration import Base
from sqlalchemy.orm import relationship
 #tabella join


car_accessories = Table(
    'car_accessories', Base.metadata,
    Column('car_id', Integer, ForeignKey('car.car_id'), primary_key=True),
    Column('accessory_id', Integer, ForeignKey('accessories.id_accessories'), primary_key=True),
)
 
car_optional = Table(
    'car_optional', Base.metadata,
    Column('car_id', Integer, ForeignKey('car.car_id'), primary_key=True),
    Column('optional_id', Integer, ForeignKey('optional.id_optional'), primary_key=True),
)
 
car_engine = Table(
    'car_engine', Base.metadata,
    Column('car_id', Integer, ForeignKey('car.car_id'), primary_key=True),
    Column('engine_id', Integer, ForeignKey('engine.id_engine'), primary_key=True),
)
 
 
class Car(Base):
    __tablename__ = "car"
 
    car_id = Column(Integer, primary_key=True, autoincrement=True)
    car_brand = Column(String(50), nullable=False)
    car_model = Column(String(50), nullable=False)
    car_start_price = Column(Float, nullable=False)
 
   
    accessories = relationship('Accessories', secondary=car_accessories, back_populates='compatible_car_components')
    optional = relationship('Optional', secondary=car_optional, back_populates='compatible_car_components')
    engine = relationship('Engine', secondary=car_engine, back_populates='compatible_car_components')
 
    def __repr__(self):
        return f"Car(id={self.car_id}, brand={self.car_brand}, model={self.car_model})"
 
    def __str__(self):
        return f"{self.car_brand} {self.car_model} - €{self.car_start_price}"