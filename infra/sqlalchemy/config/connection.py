from sqlalchemy                import create_engine
from sqlalchemy.orm            import sessionmaker
from infra.providers.singleton import Singleton

@Singleton
class DBConnection(object):

    def __init__(self):

        engine       = create_engine()
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.__db    = SessionLocal()
    
    @property
    def db(self):
        return self.__db
    
    def __str__(self):
        return 'Database connection object'