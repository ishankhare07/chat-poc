from marshmallow import Schema, fields, validates, ValidationError, post_load
from .base import session, Reply


class AcknowledgementValidator(Schema):
    type = fields.Str(required=True)
    id = fields.Integer(required=True)
    category = fields.Str(required=True)
    local_msg_id = fields.Integer()
    enquiry_id = fields.Integer()
    to_user = fields.Integer()

    @validates('type')
    def validate_type(self, data):
        if not data == "acknowledgement":
            raise ValidationError("Acknowledgement payload must be of type acknowledgement")

    @validates('id')
    def validates_message_id(self, data):
        """
            Also check if this message exists
        """
        if data < 1:
            raise ValidationError("id must me positive")

    @validates('local_msg_id')
    def validates_local_msg_id(self, data):
        if data < 1:
            raise ValidationError("local message id must be positive")

    @validates('category')
    def validates_category(self, data):
        if data not in ["received", 'server-received']:
            raise ValidationError("Invalid acknowledgement category")

    @post_load
    def make_reply(self, data):
        print('in post_load')
        if data['category'] == 'received':
            msg = session.query(Reply).filter_by(id=data['id']).first()
            msg.received = True
            try:
                session.add(msg)
                session.commit()
            except:
                session.rollback()
                session.add(msg)
                session.commit()
            return {
                'type': data['type'],
                'id': data['id'],
                'category': data['category'],
                'to_user': data['to_user']
                }
        elif data['category'] == 'read':
            reply = session.query(Reply).filter_by(id=data['id']).first()
            reply.read = True
            return reply
        else:
            # server received ack
            print('parsing ack')
            reply = session.query(Reply).filter_by(id=data['id']).first()
            reply.category = 'server-received'
            return reply
