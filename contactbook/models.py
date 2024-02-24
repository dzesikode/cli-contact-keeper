#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing_extensions import Self
from sqlalchemy import Sequence, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):

    def to_dict(self: Self) -> dict:
        """Return fields as a dictionary."""
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict_


class Contact(Base):

    __tablename__ = "contacts"

    fields = [
        "id",
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "address_line_1",
        "address_line_2",
        "city",
        "state",
        "zipcode",
        "country",
    ]

    id = Column(Integer, Sequence("contact_id_seq"), primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    city = Column(String)
    state = Column(String)
    zipcode = Column(String)
    country = Column(String)

    def __repr__(self: Self) -> str:
        return f"{self.id}  {self.first_name} {self.last_name}"
