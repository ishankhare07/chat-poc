from sqlalchemy import BINARY, Column, DateTime, Enum, Integer, String, Table, Text, text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .existing_models import Base


class EnquiryDatum(Base):
    __tablename__ = 'enquiry_data'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, nullable=False)
    buyer_id = Column(Integer, nullable=False)
    name = Column(String(30), nullable=False)
    last_name = Column(String(220), nullable=False)
    contact = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False)
    product_name = Column(String(30), nullable=False)
    product_type = Column(String(30), nullable=False)
    mini_quantity = Column(Integer, nullable=False)
    unit = Column(String(10), nullable=False)
    date = Column(String(15), nullable=False)
    msg = Column(Text, nullable=False)
    file_name = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)
    date_time = Column(String(255), nullable=False)
    customer_type = Column(String(220), nullable=False)
    location = Column(String(220), nullable=False)
    price = Column(String(220), nullable=False)
    quality = Column(String(50), nullable=False)
    enquirer_type = Column(String(50), nullable=False)
    frequency = Column(String(50), nullable=False)
    additional_comments = Column(String(255), nullable=False)
    variety = Column(String(50), nullable=False)
    packing = Column(String(50), nullable=False)
    payment = Column(String(50), nullable=False)
    enquiry_url = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    replies = relationship("Reply", backref="enquiry_data")
