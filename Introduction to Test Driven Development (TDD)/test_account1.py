"""
Test Cases TestAccountModel
"""
import json
from unittest import TestCase
from models import db
from models.account import Account

ACCOUNT_DATA = {}

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Connect and load data needed by tests """
        db.create_all()  # make our SQLAlchemy tables
        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database"""
        db.session.close() # close the database session

    def setUp(self):
        """Truncate the tables"""
        db.session.query(Account).delete()
        db.session.commit()
    def tearDown(self):
        """Remove the session"""
        db.session.remove()
    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_an_account(self):
        """ Test create a single Account """
        data = ACCOUNT_DATA[0] # get the first account
        account = Account(**data)
        account.create()
        self.assertEqual(len(Account.all()), 1)

    def test_create_all_accounts(self):
        """ Test creating multiple Accounts """
        for data in ACCOUNT_DATA:
            account = Account(**data)
            account.create()
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))