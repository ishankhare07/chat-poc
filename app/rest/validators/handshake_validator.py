from marshmallow import Schema, fields, validates, ValidationError

class HandshakeValidator(Schema):
    user_id = fields.Integer(required=True)
    jwt     = fields.String(required=True)

    @validates('user_id')
    def validate_user_id(self, data):
        """
            we also need to verify if the user_id exists
            and match with the jwt
        """

    @validates('jwt')
    def validates_jwt(self, data):
        """
            everything related to jwt self validation, expiry etc. goes here
            we can also handle the verified constraint of GlobalStore here
        """
        pass
