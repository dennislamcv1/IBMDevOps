# Test Coverage

Test coverage is the percentage of lines of code that are executed during all of the tests. High test coverage gives you confidence that a large amount of code was executed during the tests. In turn, the more lines of code executed through tests, the more confident you can be that the code works as expected.

## Instructions

In this lab we are going learn how to improve your test coverage by reading the missing lines report and then writing test cases to cover those lines.

## Step 1: Missing 26

The first thing we wan to do is run `nosetests` and produce a `coverage` report to see the lines that are missing code coverage:

```bash
nosetests
```

The initial report looks like this:

```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       6      0   100%
models/account.py       40     13    68%   26, 30, 34-35, 45-48, 52-54, 74-75
--------------------------------------------------
TOTAL                   46     13    72%
----------------------------------------------------------------------
Ran 2 tests in 0.349s
```

We are starting with **72%** test coverage. Let's see if we can run that up to **100%**! 

We'll start by taking a look at line `26` in `account.py`:

```python
def __repr__(self):
    return '<Account %r>' % self.name
```

We see that this is one of the magic methods that gets call to represent the class when printing it out. Can you think of a test that would call the `__repr__()` method on an Account? _hint: call it in `str()`_

### Solution Step 1

```python
def test_repr(self):
    """Test the representation of an account"""
    account = Account()
    account.name = "Foo"
    self.assertEqual(str(account), "<Account 'Foo'>")
```

## Step 2: Missing 30

Let's run `nosetests` again and see what the next missing line is:

```bash
nosetests
```

This time we get:

```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       6      0   100%
models/account.py       40     12    70%   30, 34-35, 45-48, 52-54, 74-75
--------------------------------------------------
TOTAL                   46     12    74%
----------------------------------------------------------------------
Ran 3 tests in 0.387s
```

Let's go look at line `30` of `account.py` and see what that code is doing.

```python
def to_dict(self) -> dict:
    """Serializes the class as a dictionary"""
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}
```

We see this is the `to_dict()` method. Can you think of a test case that would execute the `to_dict()` method on an Account?

### Solution Step 2

```python
def test_to_dict(self):
    """ Test account to dict """
    data = ACCOUNT_DATA[self.rand] # get a random account
    account = Account(**data)
    result = account.to_dict()
    self.assertEqual(account.name, result["name"])
    self.assertEqual(account.email, result["email"])
    self.assertEqual(account.phone_number, result["phone_number"])
    self.assertEqual(account.disabled, result["disabled"])
    self.assertEqual(account.date_joined, result["date_joined"])
```

## Step 3: Missing 34-35

Let's run `nosetests` again and see what the next missing line is:

```bash
nosetests
```

This time we get:

```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       6      0   100%
models/account.py       40     11    72%   34-35, 45-48, 52-54, 74-75
--------------------------------------------------
TOTAL                   46     11    76%
----------------------------------------------------------------------
Ran 4 tests in 0.368s
```

Let's go look at lines `34-35` of `account.py` and see what that code is doing.

```python
def from_dict(self, data: dict) -> None:
    """Sets attributes from a dictionary"""
    for key, value in data.items():
        setattr(self, key, value)
```

We see this is the `from_dict()` method. Can you think of a test case that would execute the `from_dict()` method on an Account?

### Solution Step 3

```python
def test_from_dict(self):
    """ Test account from dict """
    data = ACCOUNT_DATA[self.rand] # get a random account
    account = Account()
    account.from_dict(data)
    self.assertEqual(account.name, data["name"])
    self.assertEqual(account.email, data["email"])
    self.assertEqual(account.phone_number, data["phone_number"])
    self.assertEqual(account.disabled, data["disabled"])
```

## Step 4: Missing 45-48

Let's run `nosetests` again and see what the next missing line is:

```bash
nosetests
```

This time we get:

```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       6      0   100%
models/account.py       40      9    78%   45-48, 52-54, 74-75
--------------------------------------------------
TOTAL                   46      9    80%
----------------------------------------------------------------------
Ran 5 tests in 0.377s
```

Wow, we've gotten our test coverage up to **80%** we're really doing good!

Let's go look at lines `45-48` of `account.py` and see what that code is doing.

```python
def update(self):
    """Updates a Account to the database"""
    logger.info("Saving %s", self.name)
    if not self.id:
        raise DataValidationError("Update called with empty ID field")
    db.session.commit()
```

We see this is the `update()` method. Can you think of a test case that would execute the `update()` method on an Account?

### Solution Step 4

```python
def test_update_an_account(self):
    """ Test Account update using known data """
    data = ACCOUNT_DATA[self.rand] # get a random account
    account = Account(**data)
    account.create()
    self.assertIsNotNone(account.id)
    account.name = "Rumpelstiltskin"
    account.update()
    found = Account.find(account.id)
    self.assertEqual(found.name, account.name)
```

## Step 5: Missing 47

Let's run `nosetests` again and see what the next missing line is:

```bash
nosetests
```

This time we get:

```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       6      0   100%
models/account.py       40      4    90%   47, 52-54
--------------------------------------------------
TOTAL                   46      4    91%
----------------------------------------------------------------------
Ran 6 tests in 0.366s
```

We're up to **91%** test coverage but what happened with line `47`? We though that we covered 45-48 in the last test but line 47 is still showing up. Obviously there was some conditional logic that didn't get executed in that last test.

Let's go look at lines `45-48` of `account.py` and see what that code is doing.

```python
if not self.id:
    raise DataValidationError("Update called with empty ID field")
```

We see that line `47` is only executed if the `update()` method is called with an `id` that is `None`. Can you think of a test case that would execute the `update()` method and cause this line of code to execute?

### Solution Step 5

```python
def test_invalid_id_on_update(self):
    """ Test invalid ID update """
    data = ACCOUNT_DATA[self.rand] # get a random account
    account = Account(**data)
    account.id = None
    self.assertRaises(DataValidationError, account.update)
```

## Step 6: Missing 53-54

Let's run `nosetests` again and see what the next missing line is:

```bash
nosetests
```

This time we get:

```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       6      0   100%
models/account.py       40      3    92%   52-54
--------------------------------------------------
TOTAL                   46      3    93%
----------------------------------------------------------------------
Ran 7 tests in 0.385s
```

Let's go look at lines `52-54` of `account.py` and see what that code is doing.

```python
def delete(self):
    """Removes a Account from the data store"""
    logger.info("Deleting %s", self.name)
    db.session.delete(self)
    db.session.commit()
```

We see that line `52-54` is the `delete()` method. Can you think of a test case that would execute the `delete()` method on an Account?

### Solution Step 6

```python
def test_delete_an_account(self):
    """ Test Account update using known data """
    data = ACCOUNT_DATA[self.rand] # get a random account
    account = Account(**data)
    account.create()
    self.assertEqual(len(Account.all()), 1)
    account.delete()
    self.assertEqual(len(Account.all()), 0)
```

## Step 7: 100% Test Coverage

Let's run `nosetests` one last time and see what our test coverage is:

```bash
nosetests
```

Wow, I think we are done! 100% code coverage with no missing lines.

```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       6      0   100%
models/account.py       40      0   100%
--------------------------------------------------
TOTAL                   46      0   100%
----------------------------------------------------------------------
Ran 8 tests in 0.415s

OK
```

## Congratulations

You did it! You wrote enough test cases to execute every line of code in the `account` module. You now know that at least every line of code works when it is tested with some known data. There could still be bugs in the code which will only reveal themselves wen sending bad or unexpected data into you code. Never give up writing new test cases that cover more possibilities.

## Author(s)

John Rofrano

## Changelog

| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2022-04-14 | 1.0 | Rofrano | Create new Lab |
|   |   |   |   |
|   |   |   |   |

## <h3 align="center"> © IBM Corporation 2022. All rights reserved. <h3/>
