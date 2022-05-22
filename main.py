from infra.sqlalchemy.config.database import db
from infra.sqlalchemy.models.user import users

print("len", db.query(users).all())