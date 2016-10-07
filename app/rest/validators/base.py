from .models import EnquiryDatum
from .models import Reply
from .models.existing_models import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
import json

Session = sessionmaker()
engine = create_engine(os.environ.get('DB_CONNECTION_URL'))

Session.configure(bind=engine)

session = Session()
