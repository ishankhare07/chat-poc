from .base import *
from jose import jwt

class LoginHandler(BaseHandler):
    def post(self):
        email = self.json.get('email')
        password = self.json.get('password')

        user = session.query(User).filter_by(email=email).first()
        if user.password == password:
            self.write(json.dumps(dict(
                    status="success",
                    token=jwt.encode({"email": user.email, "id": user.id}, 'secret')
                )))
        else:
            self.write(json.dumps(dict(
                status="error",
                message="password incorrect"
                )))

