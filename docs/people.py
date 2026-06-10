from sqlalchemy import Column,Integer,String,Table,ForeignKey
from persistence.db_configuration import Base
from sqlalchemy.orm import Relationship

people_user=Table(
    'people_user',
    Base.metadata,
    Column('people_id',Integer,ForeignKey('people.id'),primary_key=True),
    Column('user_id',Integer,ForeignKey('user.id'), primary_key=True )

)

people_admin=Table(
    'people_admin',
    Base.metadata,
    Column('people_id',Integer,ForeignKey('people.id'),primary_key=True),
    Column('admin_id',Integer,ForeignKey('admin.id'), primary_key=True )

)








class People(Base):
    
    __tablename__="people"

    id_people=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(20),nullable=False)
    role= Column(String(20),nullable=False)
    username=Column(String(20),nullable=False)
    email=Column(String(20),nullable=False)
    password = Column(String(200), nullable=False)


    def to_dict(self):
        return {
            "id": self.id_people,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            
            }
    

    id_user=Column(Integer,ForeignKey('user_id'))
    
    user=Relationship('User')

    id_admin=Column(Integer,ForeignKey('id_admin'))

    admin=Relationship('Admin')

    











    __mapper_args__= {
            'polymorphic_identity':'people',# Default classe su cui definisci, valore per la classe 
            'polymorphic_on':role #Colonna che dice il tipo (admin-user)
    }



def __repr__(self):
    return f"People: ID :{self.id_people}, name {self.name}, username {self.username}, email {self.email} ,"

def __str__(self):
    return f"{self.id_people}{self.name}-{self.username}-{self.mail}"


def __equal__(self):
    pass