from sqlalchemy import desc, func
from flask import render_template, Blueprint, flash, redirect, url_for, current_app #flask_login, flask_required
from .models import db, Markers, Activity
from flask_googlemaps import GoogleMaps, Map
#from ..webapp.map.forms import CommentForm
import folium

app_blueprint = Blueprint(
    'web',
    __name__,
    template_folder='./templates',
    #url_prefix="/main"
    )
@app_blueprint.route('/getmap')
def getMap():
    return redirect(url_for('web.mapView'))

@app_blueprint.route('/map')
def mapView():

    return render_template('mapTest.html')

