from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://tejeshagrawal:xdr5$ESZ@localhost:5432/sqlalchemy')
Session = sessionmaker(bind=engine)

Base = declarative_base()
