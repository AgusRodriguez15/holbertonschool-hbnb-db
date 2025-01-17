""" Api Blueprint """

from flask import Blueprint
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from utils.constants import API_VERSION_PATH

from src.api.users import api as users_ns
from src.api.countries import api as countries_ns
from src.api.cities import api as cities_ns
from src.api.amenities import api as amenities_ns
from src.api.places import api as places_ns
from src.api.reviews import api as reviews_ns
from src.api.authentication import api as authentication_ns

api_bp = Blueprint("api", __name__)

api = Api(
    api_bp,
    version="1.0",
    title="HBNB API",
    prefix="",
    doc=API_VERSION_PATH,
    description="HBNB Project API",
    ordered=True,
    validate=True,
    default_mediatype="application/json",
)

api.add_namespace(users_ns, path="/users")
api.add_namespace(countries_ns, path="/countries")
api.add_namespace(cities_ns, path="/cities")
api.add_namespace(amenities_ns, path="/amenities")
api.add_namespace(places_ns, path="/places")
api.add_namespace(authentication_ns, path="/login")
api.add_namespace(reviews_ns, path="/")
