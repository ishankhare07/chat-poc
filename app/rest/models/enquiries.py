__all__ = ['Enquiry']

from . import *

class Enquiry(Base):
    __tablename__ = 'enquiries'

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    replies = relationship("Reply")

    def __repr__(self):
        return '<Enquiry: {0}, by: <some user_id>>'.format(self.id)


