from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

Session = sessionmaker()
engine = create_engine(os.environ.get('DB_CONNECTION_URL'))

Session.configure(bind=engine)

session = Session()
