from tornado.web import Application, StaticFileHandler
from tornado.ioloop import IOLoop
from rest.signup import SignupHandler
from rest.login import LoginHandler
import os

if not os.environ.get('DB_CONNECTION_URL'):
    print("please provide db url", "exiting now...", sep='\n')
    exit()

def make_app():
    return Application([
        (r'/api/signup', SignupHandler),
        (r'/api/login', LoginHandler),
        (r'/(.*)', StaticFileHandler,
            dict(path=os.path.join(os.getcwd(), "static"))),
 
    ])

def run():
    app = make_app()
    app.listen(8888)
    print('server listening on http://localhost:8888')
    IOLoop.current().start()

if __name__ == "__main__":
    run()

