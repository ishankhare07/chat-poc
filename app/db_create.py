from models import Base
from models.users import *
from models.enquiries import *
from models.replies import Reply
from sqlalchemy import create_engine

db_connection_url = "postgresql://ishan@localhost/postgres"
engine = create_engine(db_connection_url)

Base.metadata.create_all(engine)


