"""
Cities controller module
"""

from flask import request, abort
from src.models.city import City


def get_cities():
    """Returns all cities"""
    cities: list[City] = City.get_all()

    return [city.to_dict() for city in cities]


def create_city(data: dict):
    """Creates a new city"""
    try:
        city = City.create(data)
    except KeyError as e:
        abort(400, f"Missing field: {e}")
    except ValueError as e:
        abort(400, str(e))

    return city.to_dict(), 201


def get_city_by_id(city_id: str):
    """Returns a city by ID"""
    city: City | None = City.get(city_id)

    if not city:
        abort(404, f"City with ID {city_id} not found")

    return city.to_dict()


def update_city(city_id: str, data: dict):
    """Updates a city by ID"""
    try:
        city: City | None = City.update(city_id, data)
    except ValueError as e:
        abort(400, str(e))

    if not city:
        abort(404, f"City with ID {city_id} not found")

    return city.to_dict()


def delete_city(city_id: str):
    """Deletes a city by ID"""
    if not City.delete(city_id):
        abort(404, f"City with ID {city_id} not found")

    return "", 204