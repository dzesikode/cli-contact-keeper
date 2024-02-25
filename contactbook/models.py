#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional, Type
from typing_extensions import Self
from sqlalchemy import ColumnExpressionArgument, Sequence, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.session import _PKIdentityArgument

from contactbook.database import session


class Base(DeclarativeBase):

    @classmethod
    def commit(cls: Type[Self]) -> None:
        for _ in range(3):
            try:
                session().commit()
                break
            except Exception as exception:
                session().rollback()
                raise exception

    @classmethod
    def get(cls: Type[Self], ident: _PKIdentityArgument) -> Self | None:
        return session().get(cls, ident)

    @classmethod
    def get_all(cls: Type[Self], order_by: Optional[str] = None) -> list[Self]:
        query = session().query(cls)
        if order_by:
            query = query.order_by(getattr(cls, order_by))
        return query.all()

    @classmethod
    def create(cls: Type[Self], data: dict) -> Self:
        new_obj = cls(**data)
        session().add(new_obj)
        cls.commit()
        return new_obj

    def update(self: Self, data: dict) -> None:
        for key, value in data.items():
            setattr(self, key, value)
        self.commit()

    def delete(self: Self) -> None:
        session().delete(self)
        self.commit()

    @classmethod
    def search(
        cls: Type[Self], *whereclause: ColumnExpressionArgument[bool]
    ) -> list[Self]:
        return session().query(cls).filter(*whereclause).all()

    def to_dict(self: Self) -> dict:
        """Return fields as a dictionary."""
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict_


class Contact(Base):

    __tablename__ = "contacts"

    id = Column(Integer, Sequence("contact_id_seq"), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    city = Column(String)
    state = Column(String)
    zipcode = Column(String)
    country = Column(String)

    @classmethod
    def get_fields(cls: Type[Self]) -> list[str]:
        return cls.__table__.columns.keys()
