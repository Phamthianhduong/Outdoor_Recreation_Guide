
from .. import db
from . import AnonymousUserMixin

class User(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    email = db.Column(db.String(255))
    user_name = db.Column(db.String(255))

    def __init__(self, email="", id=""):
        self.id = id
        self.email = email

    def __repr__(self):
        return '<User {}>'.format(self.user_name)

    
    @property
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True 
        
    def get_id(self):
        return str(self.id)
    
    def is_active(self):
        # Replace this condition with your own logic to determine if the user is active
        return True