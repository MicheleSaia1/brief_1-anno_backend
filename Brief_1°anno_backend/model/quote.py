from sqlalchemy import Column,Integer,String,Table,ForeignKey,Float
from persistence.db_configuration import Base
from sqlalchemy.orm import relationship



class QuoteItem(Base):
    __tablename__ = "quote_item"  
 
    id = Column(Integer, primary_key=True, autoincrement=True)
    quote_id = Column(Integer, ForeignKey('quote.id'), nullable=False)
 
    
    component_type = Column(String(20), nullable=False)
    component_id = Column(Integer, nullable=False)
    price_snapshot = Column(Float, nullable=False)

    quote = relationship('Quote', back_populates='items')
 
    def __repr__(self):
        return f"QuoteItem(type={self.component_type}, component_id={self.component_id}, price={self.price_snapshot})"
 
 

 
class Quote(Base):
    __tablename__ = "quote"
 
    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('car.car_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id_user'), nullable=False)
 
    # RELATIONSHIP 
 
    car = relationship('Car')
    user = relationship('User')
    items = relationship('QuoteItem', back_populates='quote')
 
   
    configuration = relationship('Car_Configuration', back_populates='quote', uselist=False)
 
    #PROPERTY 
   
 
    @property
    def total(self) -> float:
        price_base = self.car.car_start_price
        extras = sum(item.price_snapshot for item in self.items)
        return price_base + extras
 
    @property
    def is_finalized(self) -> bool:
        return self.configuration is not None
 
    

    
    def __repr__(self):
        return f"Quote(id={self.id}, car_id={self.car_id}, finalized={self.is_finalized})"
 
    def __str__(self):
        stato = "Finalizzata" if self.is_finalized else "Bozza"
        return f"Preventivo #{self.id} [{stato}] - €{self.total}"
 