from tornado.web import RequestHandler
from .models.users import *
from .models.enquiries import *
from .models.replies import *
from . import session
import json

class BaseHandler(RequestHandler):
    def prepare(self):
        self.json = json.loads(self.request.body.decode('utf-8'))
