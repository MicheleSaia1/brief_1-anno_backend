from sqlalchemy import Column,Integer,String,Table,ForeignKey
from persistence.db_configuration import Base


class Custom(Base):
    __tablename__="Custom"

    id_custom=Column(Integer,primary_key=True,autoincrement=True)

