from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://username:password@localhost:5432/db_name')
Session = sessionmaker(bind=engine)

Base = declarative_base()
