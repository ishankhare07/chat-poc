from marshmallow import Schema, fields, validates, ValidationError

class HandshakeValidator(Schema):
    type = fields.Str()
    user_id = fields.Integer()

    @validates('type')
    def validate_type(self, data):
        if not data == "handshake":
            raise ValidationError("Opening connection type must be a handshake")


