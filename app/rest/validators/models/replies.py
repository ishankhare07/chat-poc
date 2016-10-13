from sqlalchemy import BINARY, Column, DateTime, Enum, Integer, String, Table, Text, text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .existing_models import Base

class Reply(Base):
    __tablename__ = 'replies'

    id = Column(Integer, primary_key=True)
    message = Column(Text, nullable=False)
    enquiry_id = Column(Integer, ForeignKey('enquiry_data.id'))
    from_user = Column(Integer, ForeignKey('user.user_id'))
    to_user = Column(Integer, ForeignKey('user.user_id'))
    local_msg_id = Column(Integer)
    read = Column(Boolean, default=False, nullable=False)
    received = Column(Boolean, default=False, nullable=False)
    type = Column(Text, nullable=False)

    category = None

    def __repr__(self):
        return '<Reply: {0},from: {2}, to: {3}, msg: {1}>'.format(self.id, self.message, self.from_user, self.to_user)


