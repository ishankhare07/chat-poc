from .base import *

class SignupHandler(BaseHandler):
    def post(self):
        email = self.json.get('email')
        password = self.json.get('password')

        user = User(email=email, password=password, user_type="unpaid")

        if session.query(User).filter_by(email=email).all():
            # email exists
            print("email already exists")
            self.write(json.dumps(dict(
                message="Email already exists",
                status="error"
                )))
        else:
            session.add(user)
            session.commit()
            print("successfully created user")
            self.write(json.dumps(dict(
                message="Successfully created user",
                status="Success"
                )))
