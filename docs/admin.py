from sqlalchemy import Column,Integer,String,Table,ForeignKey
from persistence.db_configuration import Base




class Admin(Base):
    __tablename__="admin"

    id_admin= Column(Integer,ForeignKey('people.id'),primary_key=True)



    __mapper_args__= {
         'polymorphic_identity':'admin'
    }


    

    def __str__(self):
        return f"[admin]:id{self.id_admin}  "




    