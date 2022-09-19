# Test Fixtures

Test fixtures are used to establish an initial known state before and after running tests. With test fixtures, we can describe what the test environment looks like before a test, or suite of tests, is run, and then again after the test runs.

## Lab Instructions

In this lab we are going to see the different ways in which test fixtures can be used to setup and teardown the initial state before and after testing.

You will do all of your editing work in the file `tests/test_account.py`. Open that up in the editor to get started.

### Step 1: Initialize database

In this step, you are going to set up a test fixture to connect and disconnect from the database. We only need to do this once before all and after all of the tests.

The following **SQLAlchemy** commands will help you do this:

```python
db.create_all()  # make the sqlalchemy tables

db.session.close() # close the database connection
```

Use the class level fixtures to invoke `db.create_all()` before all tests and `db.session.close()` after all tests.

Run `nosetests` to make sure that your test case executes without errors.

```bash
nosetests
```

#### Step 1 Solution

```python
@classmethod
def setUpClass(cls):
    """ Connect and Load data needed by tests """
    db.create_all()  # make our SQLAlchemy tables


@classmethod
def tearDownClass(cls):
    """Disconnect from database"""
    db.session.close() # close the database session
```

### Step 2: Load test data

In this step, we are going to load some test data so that it can be used during testing. This should only need to be done once before all tests so we will do this in a class method. We will load it into a global variable called `ACCOUNT_DATA` that has already been declared.

The data is in a file under the `tests/fixtures` folder and is called `account_data.json`.

This Python code to load the data is:

```python
with open('tests/fixtures/account_data.json') as json_data:
    ACCOUNT_DATA = json.load(json_data)
```

#### Step 2 Solution

```python
@classmethod
def setUpClass(cls):
    """ Connect and Load data needed by tests """
    db.create_all()  # make our SQLAlchemy tables
    global ACCOUNT_DATA
    with open('tests/fixtures/account_data.json') as json_data:
        ACCOUNT_DATA = json.load(json_data)
```

Run `nosetests` to make sure that your test case executes without errors.

```bash
nosetests
```

### Step 3: Write a test case to create an account

Now we are ready to write our first test. We will create a single account using the `ACCOUNT_DATA` dictionary which has test data for 5 accounts. 

The `Account` class has a `create()` method which can be used to add an account to the database. It also has an `all()` method which performs a query that returns all accounts. 

Your test cases should create an account and then call the `Account.all()` method and assert that one account was returned.

#### Step 3 Solution

```python
def test_create_an_account(self):
    """ Test create a single Account """
    data = ACCOUNT_DATA[0] # get the first account
    account = Account(**data)
    account.create()
    self.assertEqual(len(Account.all()), 1)
```

Run `nosetests` to make sure that your test case passes.

```bash
nosetests
```

You should see:

```bash
Test Account Model
- Test create a single Account

Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       6      0   100%
models/account.py       44     17    61%   26, 30, 34-41, 51-54, 58-60, 80-81
--------------------------------------------------
TOTAL                   50     17    66%
----------------------------------------------------------------------
Ran 1 test in 0.340s

OK
```

### Step 4: Write a test case to create all accounts

Now that we know that one account can be successfully created, let's write a test case that creates all 5 of the accounts in the `ACCOUNT_DATA` dictionary.

Use a `for` loop to load all of the data from the `ACCOUNT_DATA` dictionary and then use the `Account.all()` method to retrieve them and assert that the number of accounts returned is equal to the number of accounts in the test data dictionary.

#### Step 4 Solution

```python
def test_create_all_accounts(self):
    """ Test creating multiple Accounts """
    for data in ACCOUNT_DATA:
        account = Account(**data)
        account.create()
    self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))
```

Run `nosetests` to make sure that your test case passes.

```bash
nosetests
```

**ERROR:** This time the tests did not pass! You should have received two error about **AssertionError: 6 != 5** and **AssertionError: 7 != 1**:

```bash
======================================================================
FAIL: Test Account creation using known data
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/rofrano/Code/duwjx-tdd_bdd_PracticeCode/labs/03_test_fixtures/tests/test_account.py", line 52, in test_create_an_account
    self.assertEqual(len(Account.all()), 1)
AssertionError: 7 != 1
```

Why were 7 accounts returned when we only expect 1?
Let's see how we can fix this in the next step.

### Step 5: Clear out the tables before each test

The reason that our test case failed is because data from a previous test has affected the outcome of the next test. To avoid this, we need to add more test fixtures that will run because and after each test.

One way of removing the data from a table is with the `db.session.query(<Table>).delete()` command where `<Table>` is the class name of the tables.
This will delete all of the records in the table. You ust also use `db.session.commit()` to commit this change. Add that to the fixture that runs before each test.

The correct syntax for our `Account` class is:

```python
db.session.query(Account).delete()
```

It's also a good idea to use the `db.session.remove()` command after each test. Add that to the fixture that runs after each test.

#### Step 5 Solution

```python
def setUp(self):
    """Truncate the tables"""
    db.session.query(Account).delete()
    db.session.commit()

def tearDown(self):
    """Remove the session"""
    db.session.remove()
```

Run `nosetests` to make sure that your test case passes.

```bash
nosetests
```

You should see the following report:

```bash
Test Account Model
- Test creating multiple Accounts
- Test create a single Account

Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       6      0   100%
models/account.py       44     17    61%   26, 30, 34-41, 51-54, 58-60, 80-81
--------------------------------------------------
TOTAL                   50     17    66%
----------------------------------------------------------------------
Ran 2 tests in 0.346s

OK
```

**Congratulations!** All of your test cases have passed this time.

## Conclusion

We have seen how using test fixtures allows us to control the state of the system before and after each test so that tests run in isolation and get repeatable result every time.

## Author(s)

John Rofrano

## Changelog

| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2022-04-14 | 1.0 | Rofrano | Create new Lab |
|   |   |   |   |
|   |   |   |   |

## <h3 align="center"> © IBM Corporation 2022. All rights reserved. <h3/>
