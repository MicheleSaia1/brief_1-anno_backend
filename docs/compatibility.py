from sqlalchemy import Column,Integer,String,Table,ForeignKey
from persistence.db_configuration import Base




class compatibility(Base):
    __tablename__='component_compatibility'

    