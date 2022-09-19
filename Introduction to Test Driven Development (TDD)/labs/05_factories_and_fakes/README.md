# Factories and Fakes

Welcome to the Factories and Fakes lab. You often need fake data to test against. You can, of course, use some "hard coded" sample data in your tests. But what if you need hundreds of records, or even thousands of records of test data? That can get tedious to create and maintain.

In this lab we're going to see how to use a popular Python package called **FactoryBoy** to provide fake data for testing.

## Learning Objectives

After completing this lab you will be able to:

- Understand how to create a Factory class
- Utilize the Faker class and Fuzzy attributes to provide realistic test data
- Write test cases that use Factory classes to provide test data

## Prerequisites

Let's start by installing the required Python packages for this lab:

```bash
pip install -r requirements.txt
```

## Step 1: Run nosetests

Before you make any changes to the code, you want to be sure that all of the test cases are passing. Otherwise, you may encounter failing test cases later and you won't know if you caused them to fail, or if they were failing before you changed anything.

Let's run `nosetests` and be sure that all of the tests are passing with **100%** test coverage.

```bash
nosetests
```

You should see the following output:

```
Test Account Model
- Test creating multiple Accounts
- Test Account creation using known data
- Test Account update using known data
- Test account from dict
- Test invalid ID update
- Test the representation of an account
- Test account to dict
- Test Account update using known data

Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       6      0   100%
models/account.py       40      0   100%
--------------------------------------------------
TOTAL                   46      0   100%
----------------------------------------------------------------------
Ran 8 tests in 0.377s

OK
```

We can now move on to modifying the code.

## Step 2: Create an AccountFactory class

In this step we will create an `AccountFactory` class.

Open the `models/account.py` file to familiarize yourself with the attributes of the `Account` class. These are the same attributes that you will need to add to the `AccountFactory` class.

Open the `tests/factories.py` file in the IDE editor.

We want to take advantage of the fact that **FactoryBoy** comes with the **Faker** class which has [Fake providers](https://faker.readthedocs.io/en/master/providers/baseprovider.html) and a number of [Fuzzy attributes](https://factoryboy.readthedocs.io/en/stable/fuzzy.html).

Here are some useful providers for the Faker class:

```
Faker("name")
Faker("email")
Faker("phone_number")
```

Here are some Fuzzy attributes you might find useful:

```
FuzzyChoice(choices=[True, False])
FuzzyDate(date(2008, 1, 1))
```

Use the **Faker** providers and **Fuzzy** attributes to create fake data for the `id`, `name`, `email`, `phone_number`, `disabled`, and `date_joined` fields by adding them to the `AccountFactory` class.

### Solution for Step 2

```python
id = Sequence(lambda n: n)
name = Faker("name")
email = Faker("email")
phone_number = Faker("phone_number")
disabled = FuzzyChoice(choices=[True, False])
date_joined = FuzzyDate(date(2008, 1, 1))
```

## Step 3: Update the test cases

In this step we will update the test cases to use the new `AccountFactory` that you created in the previous step.

Open the `tests/test_account.py` file. Then add the following import near the top of the file, after the other `imports`. This will import your new `AccountFactory` class from the `factories` module:

```python
from factories import AccountFactory
```

In the remaining steps, we want to change all of the referenced to `Account` to now use `AccountFactory`. We will do this one test at a time.

Let's start with the `test_create_all_accounts()` test. Remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`. Also change the code to create 10 Accounts.

Run `nosetests` to make sure the test cases still pass.

```bash
nosetests
```

### Solution for Step 3

```python
def test_create_all_accounts(self):
    """ Test creating multiple Accounts """
    for _ in range(10):
        account = AccountFactory()
        account.create()
    self.assertEqual(len(Account.all()), 10)
```

## Step 4: Update test_create_an_account()

In this step we wil update the `test_create_an_account()` test. Modify the code to remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`.

Run `nosetests` to make sure the test cases still pass.

```bash
nosetests
```

### Solution for Step 4

```python
def test_create_an_account(self):
    """ Test Account creation using known data """
    account = AccountFactory()
    account.create()
    self.assertEqual(len(Account.all()), 1)
```

## Step 5: Update test_to_dict()

In this step we wil update the `test_to_dict()` test. Modify the code to remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`.

Run `nosetests` to make sure the test cases still pass.

```bash
nosetests
```

### Solution for Step 5

```python
def test_to_dict(self):
    """ Test account to dict """
    account = AccountFactory()
    result = account.to_dict()
    self.assertEqual(account.name, result["name"])
    self.assertEqual(account.email, result["email"])
    self.assertEqual(account.phone_number, result["phone_number"])
    self.assertEqual(account.disabled, result["disabled"])
    self.assertEqual(account.date_joined, result["date_joined"])
```

## Step 6: Update test_from_dict()

In this step we wil update the `test_from_dict()` test. Modify the code to remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`.

Run `nosetests` to make sure the test cases still pass.

```bash
nosetests
```

### Solution for Step 6

```python
def test_from_dict(self):
    """ Test account from dict """
    data = AccountFactory().to_dict()
    account = Account()
    account.from_dict(data)
    self.assertEqual(account.name, data["name"])
    self.assertEqual(account.email, data["email"])
    self.assertEqual(account.phone_number, data["phone_number"])
    self.assertEqual(account.disabled, data["disabled"])
```

## Step 7: Update test_update_an_account()

In this step we wil update the `test_update_an_account()` test. Modify the code to remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`.

Run `nosetests` to make sure the test cases still pass.

```bash
nosetests
```

### Solution for Step 7

```python
def test_update_an_account(self):
    """ Test Account update using known data """
    account = AccountFactory()
    account.create()
    self.assertIsNotNone(account.id)
    account.name = "Rumpelstiltskin"
    account.update()
    found = Account.find(account.id)
    self.assertEqual(found.name, account.name)
```

## Step 8: Update test_invalid_id_on_update()

In this step we wil update the `test_invalid_id_on_update()` test. Modify the code to remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`.

Run `nosetests` to make sure the test cases still pass.

```bash
nosetests
```

### Solution for Step 8

```python
def test_invalid_id_on_update(self):
    """ Test invalid ID update """
    account = AccountFactory()
    account.id = None
    self.assertRaises(DataValidationError, account.update)
```

## Step 9: Update test_delete_an_account()

In this step we wil update the `test_delete_an_account()` test. Modify the code to remove the references to `ACCOUNT_DATA` and `Account` and replace it with `AccountFactory`.

Run `nosetests` to make sure the test cases still pass.

```bash
nosetests
```

### Solution for Step 9

```python
def test_delete_an_account(self):
    """ Test Account update using known data """
    account = AccountFactory()
    account.create()
    self.assertEqual(len(Account.all()), 1)
    account.delete()
    self.assertEqual(len(Account.all()), 0)
```

## Step 10: Remove ACCOUNT_DATA references

Since we have replaced all of the instance of `ACCOUNT_DATA` with `AccountFactory`, we can clean up the code by removing all remaining references to `ACCOUNT_DATA` and also remove loading it from the json data file.

Remove line 31 from `setUp()`:

```python
self.rand = randrange(0, len(ACCOUNT_DATA))
```

### Solution 10a

```python
def setUp(self):
    """Truncate the tables"""
    db.session.query(Account).delete()
    db.session.commit()
```

Remove lines 20-22 from `setUpClass()`:

```python
global ACCOUNT_DATA
with open('tests/fixtures/account_data.json') as json_data:
    ACCOUNT_DATA = json.load(json_data)
```

## Solution 10b

```python
@classmethod
def setUpClass(cls):
    """ Load data needed by tests """
    db.create_all()  # make our sqlalchemy tables
```

You can also delete line `11` that declares `ACCOUNT_DATA`:

```python
ACCOUNT_DATA = {}   # <- delete this line
```

Finally delete line 4-5 that imports `json` and  `randrange`:

```python
import json
from random import randrange
```

Save you changes and run `nosetests` one last time to make sure the test cases still pass.

```bash
nosetests
```

You should see:

```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       6      0   100%
models/account.py       40      0   100%
--------------------------------------------------
TOTAL                   46      0   100%
----------------------------------------------------------------------
Ran 8 tests in 0.548s
```

## Conclusion

Congratulations on completing the Factories and Fakes lab. Hopefully you have a good understand of how to build a Factory for your classes using **Faker** and **Fuzzy** attributes. You have also learned how to use a Factory class in your test cases to provide unlimited test data.

Try and apply what you have learned to your personal projects. Anywhere you have created static data to test your code, you can substitute dynamic factories to make testing more robust.

## Author(s)

John Rofrano

## Changelog

| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2022-04-15 | 1.0 | Rofrano | Create new Lab |
|   |   |   |   |
|   |   |   |   |

## <h3 align="center"> © IBM Corporation 2022. All rights reserved. <h3/>
