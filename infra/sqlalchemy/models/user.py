from infra.sqlalchemy.config.database import Base
from sqlalchemy                       import String, Integer, Column

class users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
