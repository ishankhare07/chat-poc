from .models.existing_models import EnquiryDatum, User, Reply
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
import json

Session = sessionmaker()
engine = create_engine(os.environ.get('DB_CONNECTION_URL'))

Session.configure(bind=engine)

session = Session()
