__all__ = ['Reply']

from . import *

class Reply(Base):
    __tablename__ = 'replies'

    id = Column(Integer, primary_key=True)
    message = Column(String, nullable=False)
    enquiry_id = Column(Integer, ForeignKey('enquiries.id'))
    from_user = Column(Integer, ForeignKey('users.id'))
    to_user = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return '<Reply: {0}, msg: {1}>'.format(self.id, self.message)
