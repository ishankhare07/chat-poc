from marshmallow import Schema, fields, validates, ValidationError

class HandshakeValidator(Schema):
    user_id = fields.Integer(required=True)

    @validates('user_id')
    def validate_user_id(self, data):
        """
            we also need to verify if the user_id exists
            and match with the jwt
        """
        if not isinstance(data, int):
            data = int(data)
