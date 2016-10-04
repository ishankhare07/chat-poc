__all__ = ['Enquiry']

from . import *

class Enquiry(Base):
    __tablename__ = 'enquiries'

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    replies = relationship("Reply", backref="enquiries")

    def __repr__(self):
        return '<Enquiry: {0}, by: {1}>'.format(self.id, self.user_id)

    def jsonify(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "content": self.content
        }