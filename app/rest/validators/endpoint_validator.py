from marshmallow import Schema, fields, validates, ValidationError

class EndpointValidator(Schema):
    user_id = fields.Integer(required=True)

    @validates('user_id')
    def validate_user_id(self, data):
        """
            check if user exists
        """
