from rest.models import Base
from rest.models.users import *
from rest.models.enquiries import *
from rest.models.replies import Reply
from sqlalchemy import create_engine

db_connection_url = "postgresql://ishan@localhost/postgres"
engine = create_engine(db_connection_url)

Base.metadata.create_all(engine)


