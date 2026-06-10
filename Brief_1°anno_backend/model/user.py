from sqlalchemy import Column,Integer,String,Table,ForeignKey
from persistence.db_configuration import Base


class User(Base):
    __tablename__ = "user"  
 
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(200), nullable=False)  
    role = Column(String(20), nullable=False, default="user")
 
    def to_dict(self):
       
        return {
            "id": self.id_user,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "role": self.role,
        }
 
   
    def __repr__(self):
        return f"User(id={self.id_user}, email={self.email})"
 
    def __str__(self):
        return f"{self.name} ({self.username})"


    
    



    


    


 




