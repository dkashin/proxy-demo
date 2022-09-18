
'''
SQLAlchemy database models
'''

import datetime

from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Requests(Base):
    '''
    SQLAlchemy Base class model.
    Requests: Table for HTTP requests storage.
    '''
    __tablename__ = 'Requests'
    id = Column(Integer, primary_key = True, unique = True, autoincrement = True)
    username = Column(String, nullable = False)
    ip_address = Column(String)
    jwt = Column(String)
    timestamp = Column(DateTime, default = datetime.datetime.now())

    # Serializing table data
    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'ip_address': self.ip_address,
            'jwt': self.jwt,
            'timestamp': self.timestamp
        }
