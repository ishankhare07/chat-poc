__all__ = ['User']

from . import *

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    user_type = Column(String)       # paid/un-paid
    enquiries = relationship("Enquiry")
    
    def __repr__(self):
        return '<User: {0}, type: {1}>'.format(self.id, self.type)




