"""
Place related functionality
"""

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from src import repo
from src.models.base import Base
from src.models.city import City
from src.models.user import User
from src import db

class Place(Base, db.Model):
    """Place representation"""

    name = sa.Column(sa.String(255))
    description = sa.Column(sa.String(255))
    address = sa.Column(sa.String(255))
    latitude = sa.Column(sa.Float)
    longitude = sa.Column(sa.Float)
    host_id = sa.Column(sa.String(255))
    city_id = sa.Column(sa.String(255))
    price_per_night = sa.Column(sa.Integer)
    number_of_rooms = sa.Column(sa.Integer)
    number_of_bathrooms = sa.Column(sa.Integer)
    max_guests = sa.Column(sa.Integer)
    
    def __init__(self, data: dict | None = None, **kw) -> None:
        """Dummy init"""
        super().__init__(**kw)

        if not data:
            return

        self.name = data.get("name", "")
        self.description = data.get("description", "")
        self.address = data.get("address", "")
        self.city_id = data["city_id"]
        self.latitude = float(data.get("latitude", 0.0))
        self.longitude = float(data.get("longitude", 0.0))
        self.host_id = data["host_id"]
        self.price_per_night = int(data.get("price_per_night", 0))
        self.number_of_rooms = int(data.get("number_of_rooms", 0))
        self.number_of_bathrooms = int(data.get("number_of_bathrooms", 0))
        self.max_guests = int(data.get("max_guests", 0))

    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<Place {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "city_id": self.city_id,
            "host_id": self.host_id,
            "price_per_night": self.price_per_night,
            "number_of_rooms": self.number_of_rooms,
            "number_of_bathrooms": self.number_of_bathrooms,
            "max_guests": self.max_guests,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "Place":
        """Create a new place"""
        user: User | None = User.get(data["host_id"])

        if not user:
            raise ValueError(f"User with ID {data['host_id']} not found")

        city: City | None = City.get(data["city_id"])

        if not city:
            raise ValueError(f"City with ID {data['city_id']} not found")

        new_place = Place(data=data)

        repo.save(new_place)

        return new_place

    @staticmethod
    def update(place_id: str, data: dict) -> "Place | None":
        """Update an existing place"""
        place: Place | None = Place.get(place_id)

        if not place:
            return None

        for key, value in data.items():
            setattr(place, key, value)

        repo.update(place)

        return place
