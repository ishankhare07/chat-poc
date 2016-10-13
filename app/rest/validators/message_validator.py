from marshmallow import Schema, fields, validates, ValidationError, post_load
from .base import Reply

class MessageValidator(Schema):
    type = fields.Str(required=True)
    enquiry_id = fields.Integer(required=True)
    from_user = fields.Integer(required=True)
    to_user = fields.Integer(required=True)
    local_msg_id = fields.Integer(required=True)
    message = fields.Str(required=True)
    id = fields.Integer()

    @validates('type')
    def validate_type(self, data):
        if not data == "message":
            raise ValidationError("Message must have a type of message")

    @validates('enquiry_id')
    def validates_enq_id(self, data):
        # check if this enq_id exists
        pass

    @validates('from_user')
    def validates_from_user(self, data):
        '''
            check if user id exists in db
            also verify if user in JWT is same as user id
        '''
        pass

    @validates('to_user')
    def validates_to_user(self, data):
        '''
            check if user exists in db
        '''
        pass

    @validates('local_msg_id')
    def validates_local_message_id(self, data):
        if not data > 0:
            raise ValidationError("Local Message Id must be positive")

    @post_load
    def make_reply(self, data):
        return Reply(message = data['message'],
                    enquiry_id = data['enquiry_id'],
                    from_user = data['from_user'],
                    to_user = data['to_user'],
                    local_msg_id = data['local_msg_id'],
                    type = data['type']
                    )
