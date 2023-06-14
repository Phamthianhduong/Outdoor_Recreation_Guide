from flask import (redirect, url_for, session, abort, flash)
from flask_login import LoginManager, login_fresh, login_user, current_user
from flask_bcrypt import Bcrypt
#from config import DevConfig
#from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer import oauth_authorized
from .controllers import google_blueprint



login_manager = LoginManager()

#login_manager.login_view = "auth.login"


def create_module(app, **kwargs):
    app.register_blueprint(google_blueprint)
    
    
    """login_manager.init_app(app)
    google_blueprint = make_google_blueprint(
        client_id = app.config.get("GOOGLE_CLIENT_ID"),
        client_secret = app.config.get("GOOGLE_CLIENT_SECRET"),
        scope=["email", "profile"],
        #scope=["https://www.googleapis.com/auth/userinfo.profile","https://www.googleapis.com/auth/userinfo.email",], 
        
    )
    
    
    app.register_blueprint(google_blueprint, url_prefix='/auth/login')

    from .controllers import google_blueprint
#    app.register_blueprint(google_blueprint) """ 
     
    
@login_manager.user_loader
def load_user(userId):
    from .models import User 
    return User.query.get(userId) 


"""@oauth_authorized.connect
def logged_in(blueprint, token):
    from .models import db, User
    if blueprint.name == 'google':
        resp = google.get('/oauth2/v2/userinfo')
        if resp.ok:
            user_info = resp.json()
            email = user_info['email']  
            user = User.query.filter_by(email=email).first()
            if not user:
                user = User()
                user.email = email
                db.session.add(user)
                db.session.commit()
            login_user(user)
            flash("You have been logged in.", category="success")
        else:
            flash("Failed to fetch user info from Google.", category="error")
            return redirect(url_for('google.login'))
"""
        


    
    
