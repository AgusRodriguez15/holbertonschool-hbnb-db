""" Abstract base class for all models """

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from datetime import datetime
from typing import Any, Optional
from src import repo
import uuid
from abc import ABC, abstractmethod


class Base:
    """
    Base Interface for all models
    """

    id = sa.Column(sa.String, primary_key=True)
    created_at = sa.Column(sa.DateTime, default=func.now())
    updated_at = sa.Column(sa.DateTime, default=func.now())

    def __init__(
        self,
        id: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        **kwargs,
    ) -> None:
        """
        Base class constructor
        If kwargs are provided, set them as attributes
        """

        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    continue
                setattr(self, key, value)

        self.id = str(id or uuid.uuid4())
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
    #alchemy
    
    

    @classmethod
    def get(cls, id) -> "Any | None":
        """
        This is a common method to get an specific object
        of a class by its id

        If a class needs a different implementation,
        it should override this method
        """
        return repo.get(cls.__name__.lower(), id)

    @classmethod
    def get_all(cls) -> list["Any"]:
        """
        This is a common method to get all objects of a class

        If a class needs a different implementation,
        it should override this method
        """
        return repo.get_all(cls.__name__.lower())

    @classmethod
    def delete(cls, id) -> bool:
        """
        This is a common method to delete an specific
        object of a class by its id

        If a class needs a different implementation,
        it should override this method
        """
        obj = cls.get(id)

        if not obj:
            return False

        return repo.delete(obj)

    @abstractmethod
    def to_dict(self) -> dict:
        """Returns the dictionary representation of the object"""

    @staticmethod
    @abstractmethod
    def create(data: dict) -> Any:
        """Creates a new object of the class"""

    @staticmethod
    @abstractmethod
    def update(entity_id: str, data: dict) -> Any | None:
        """Updates an object of the class"""
