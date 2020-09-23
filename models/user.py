# coding=utf-8
from sqlalchemy import (Column, Integer, String, Boolean, DateTime)
import datetime
from pbkdf2 import PBKDF2
from models.dbsession import Base
from models.dbsession import dbSession


class User(Base):
    """ Subscriber & user
    """
    __tablename__ = 'tbl_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    _password = Column('password', String(64))
    email = Column(Boolean, default=True)
    last_login = Column(DateTime)
    loginnum = Column(Integer, default=0)
    creatime = Column(DateTime, default=datetime.datetime.utcnow)
    _locked = Column(Boolean, default=False, nullable=False)

    def _hash_password(self, password):
        return PBKDF2.crypt(password, iterations=0x2537)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = self._hash_password(password)

    def auth_password(self, other_password):
        if self._password:
            return self.password == PBKDF2.crypt(other_password, self.password)
        else:
            return False

    def __repr__(self):
        return """<User(id=%s,username=%s,password=%s,creatime=%s,_locked=%s)>
             """ % (
            self.id,
            self.username,
            self.password,
            self.email,
            self.creatime,
        )

    @classmethod
    def all(cls):
        return dbSession.query(cls).all()

    @classmethod
    def by_id(cls, id):
        return dbSession.query(cls).filter_by(id=id).first()

    @classmethod
    def by_uuid(cls, uuid):
        return dbSession.query(cls).filter_by(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        return dbSession.query(cls).filter_by(user_name=name).first()

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        assert isinstance(value, bool)
        self._locked = value

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'last_login': self.last_login,
        }
