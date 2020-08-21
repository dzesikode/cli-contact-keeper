#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence, Column, Integer, String

Base = declarative_base()

class Contact(Base):

    __tablename__ = 'contacts'

    fields = ['last_name', 'first_name', 'address_line_1', 'address_line_2',
             'city', 'state', 'zipcode', 'country', 'phone_number', 'email']

    id = Column(Integer, Sequence('contact_id_seq'), primary_key=True)
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

    def __repr__(self):
        return self.last_name + ', ' + self.first_name
