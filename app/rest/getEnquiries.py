from .base import *

class EnquiriesHandler(BaseHandler):
    def get(self, id):
        enquiries = session.query(Enquiry).filter_by(user_id=id).all()
        return json.dumps([enquiry.serialize() for enquiry in enquiries])
