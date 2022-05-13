from sqlalchemy.ext.declarative         import declarative_base
from infra.sqlalchemy.config.connection import DBConnection

Base = declarative_base()
db   = DBConnection.Instance().db
