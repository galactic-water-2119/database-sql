from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://username:password@localhost:5432/db_name', pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)

Base = declarative_base()
