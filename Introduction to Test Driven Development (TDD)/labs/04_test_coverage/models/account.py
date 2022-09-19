"""
Account class
"""
import logging
from sqlalchemy.sql import func
from models import db

logger = logging.getLogger()


class DataValidationError(Exception):
    """Used for an data validation errors when deserializing"""


class Account(db.Model):
    """ Class that represents an Account """
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone_number = db.Column(db.String(32), nullable=True)
    disabled = db.Column(db.Boolean(), nullable=False, default=False)
    date_joined = db.Column(db.Date, nullable=False, server_default=func.now())

    def __repr__(self):
        return '<Account %r>' % self.name

    def to_dict(self) -> dict:
        """Serializes the class as a dictionary"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def from_dict(self, data: dict) -> None:
        """Sets attributes from a dictionary"""
        for key, value in data.items():
            setattr(self, key, value)

    def create(self):
        """Creates an Account in the database"""
        logger.info("Creating %s", self.name)
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Updates an Account in the database"""
        logger.info("Saving %s", self.name)
        if not self.id:
            raise DataValidationError("Update called with empty ID field")
        db.session.commit()

    def delete(self):
        """Removes an Account from the database"""
        logger.info("Deleting %s", self.name)
        db.session.delete(self)
        db.session.commit()

    ##################################################
    # CLASS METHODS
    ##################################################

    @classmethod
    def all(cls) -> list:
        """Returns all of the Accounts in the database"""
        logger.info("Processing all Accounts")
        return cls.query.all()

    @classmethod
    def find(cls, account_id: int):
        """Finds an Account by it's ID
        :param account_id: the id of the Account to find
        :type account_id: int
        :return: an instance with the account_id, or None if not found
        :rtype: Account
        """
        logger.info("Processing lookup for id %s ...", account_id)
        return cls.query.get(account_id)
