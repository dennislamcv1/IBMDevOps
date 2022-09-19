# Lab 6: Mocking Objects

Welcome to the **Mocking Objects** lab. Mocking is a process for creating objects that mimic the behavior of real objects. It can be very useful when your code calls another system that it depends on which might not be available during test. Understanding mocking is critical for making sure that you are only testing your code, not someone else’s system.

## Introduction

In this lab we are going to use both patching and mocking to mock the real calls to the Internet Movie Database (IMDb) service during testing. We are also going to use test fixtures to provide us with valid responses that we would have gotten back from the IMDb service had we really called it. In this way, we can control what is returned from the service without every having to make an actual call to it.

## Learning Objectives

After completing this lab you will be able to:

- Use test fixtures to load mock responses from real APIs
- Understand how to use the patch decorator during testing
- Utilize the Mock class to mimic the behavior of other objects
- Write test cases that patch and mock returned objects using test fixture data

## Establishing Test Fixtures

In the `tests/fixtures/` folder you will find a file called `imdb_responses.json`. We created this file by actually calling the IMDb API and recording the responses that came back. Then we gave each one of them a name and placed them into a `json` file to be loaded during test. 

We also copied a few responses and modified them to simulate good and bad responses. Hopefully you can see how powerful this concept is of controlling what is returned under test conditions. You can make the responses do anything you want.

Open the `tests/fixtures/imdb_responses.json` file in the IDE to familiarize yourself with the various responses that we will be using in the tests.

## The IMDb Class

In the `models/` folder you will find a file called `imdb.py`. This module contains the `IMDb` class that we will be testing. It implements three (3) of the many APIs that the IMDb service exposes. Currently the SearchTitle, Reviews, and Ratings APIs have been implemented by the methods `search_titles()`, `movie_reviews()`, and `movie_ratings()` respectively.

Open the `models/imdb.py` file in the IDE to familiarize yourself with the various methods of calling it. We will be calling these methods in out tests.

## The Test Cases

In the `tests/` folder you will find a file called `test_imdb.py`. This is the file that we will add our test cases to in order to test the `IMDb` class.

Open the `tests/test_imdb.py` file in the IDE editor. We will be working in this file for the remainder of the lab.

## Step 1: Test Search by Title

We will start by implementing a test case for search by title. Below is the test method that currently implements search by title without any patching or mocking. 

Copy and paste this code into `test_imdb.py` as the first test but don't run it yet:

```python
def test_search_by_title(self):
    """Test searching by title"""
    imdb = IMDb("k_12345678")
    results = imdb.search_titles("Bambi")
    self.assertIsNotNone(results)
    self.assertIsNone(results["errorMessage"])
    self.assertIsNotNone(results["results"])
    self.assertEqual(results["results"][0]["id"], "tt1375666")
```

> Notice this code instantiates an IMDb object initializing it with an apikey. It then calls `imdb.search_titles()` for the movie "Bambi" and asserts that the results are not none. It also checks that the error message is empty, and the `id` returned is `tt1375666`.

If you had a real IMDb api key, this code will actually call the IMDb service and return a response. But we don't want to use up our allocation of API calls on testing so we will patch this method to not call the service at all.

We want to patch the `search_titles()` method of the `IMDb` class (i.e., `IBDb.search_titles()`) so that it doesn't get called at all. For this we will use the `@patch()` decorator and patch the `return_value` to return the `GOOD_SEARCH` test fixture.

In `test_imdb.py`, add the following line of code before the `test_search_by_title(self)` method and add a parameter for the new mock called `imdb_mock`. 

```python
@patch('test_imdb.IMDb.search_titles')
def test_search_by_title(self, imdb_mock):
```

> Notice that this is patching `test_imdb.IMDb.search_titles`. The name of our test module is `test_imdb` and so we want to patch the `IMDb` class that we imported, not the one in the `models` package. This is an important concept to understand. You always want to patch the function that is within the namespace that you are testing. This is why you need to fully qualify `IMDb.search_titles` as `test_imdb.IMDb.search_titles`.

Next add this line of code as the first line inside the method after the docstring and before the call to instantiate the `IMDb` class:

```python
imdb_mock.return_value = IMDB_DATA["GOOD_SEARCH"]
```

> Notice that `imdb_mock` is the extra parameter that we added to the method call after using `@patch()`. This variable represents the patch that was made. You can use `return_value` or `side_effect` on this variable. We are using `return_value` to control what is returned from the patched call.

Those two changes are enough to not call the `IMDb.search_titles()` method and instead simply return the `GOOD_SEARCH` response.

Run `nosetests` and make sure the test cases pass:

```bash
nosetests
```

The results should look like this:

```
Tests Cases for IMDb Database
- Test searching by title

Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       1      0   100%
models/imdb.py          24     15    38%   19-23, 27-31, 35-39
--------------------------------------------------
TOTAL                   25     15    40%
----------------------------------------------------------------------
Ran 1 test in 0.112s

OK
```

### Solution to step 1

```python
@patch('test_imdb.IMDb.search_titles')
def test_search_by_title(self, imdb_mock):
    """Test searching by title"""
    imdb_mock.return_value = IMDB_DATA["GOOD_SEARCH"]
    imdb = IMDb("k_12345678")
    results = imdb.search_titles("Bambi")
    self.assertIsNotNone(results)
    self.assertIsNone(results["errorMessage"])
    self.assertIsNotNone(results["results"])
    self.assertEqual(results["results"][0]["id"], "tt1375666")
```

## Step 2: Search with No Result

Now we are going to slowly get more sophisticated in what we patch and mock. This next test is a "sad path". It will test a call that returns no result.

Start by cutting and pasting the non-patched version of the `test_search_with_no_results(self)` method into `test_imdb.py`. Here is the code to copy:  

```python
def test_search_with_no_results(self):
    """Test searching with no results"""
    imdb = IMDb("k_12345678")
    results = imdb.search_titles("Bambi")
    self.assertEqual(results, {})
```

> Notice this instantiates a new IMDb instance with an apikey and then calls `imdb.search_titles("Bambi")` and asserts that it sent back and empty dictionary. That's not very likely unless you can get the IMDb service to fail... but we can simulate that failure with a mock!

In `test_imdb.py`, add the following line of code before the `test_search_with_no_results(self)` method and add a parameter for the new mock called `imdb_mock`. This is patch the call to `requests.get()` and allow us to control what comes back using the `imdb_mock` variable.

```python
@patch('models.imdb.requests.get')
def test_search_with_no_results(self, imdb_mock):
```

> Notice that this time we are patching a 3rd party library called `requests`. But it's not the requests package that we have imported into our test module. It's the requests package in the `imdb` module (`models.imdb.requests.get`) Specifically we are patching the `get` function because we know that `IMDb.search_titles()` is going to eventually call the `requests.get()` method to make the call to the IMDb API. We want to intercept (or patch) that call to control what is returned.

Next add this line of code as the first line inside the method after the docstring and before the call to instantiate the `IMDb` class:

```python
imdb_mock.return_value = Mock(status_code=404)
```

> Notice this is patching the `return_value` of the `requests.get()` call with a `Mock` object that has an attribute called `status_code` set to `404`. If we look in the source code for `IMDb.search_titles()` we will see that after the call to `requests.get()` is made, it checks that the `status_code` is `200` and if it isn't, it returns an empty dictionary `{}`. This is the behavior we want to test.

Those two changes are enough to cause the `requests.get()` method to not be called and instead, return a `Mock` object with a `status_code` of `404` and send back `{}`.

Run `nosetests` and make sure the test cases pass:

```bash
nosetests
```

The results should look like this:

```
Tests Cases for IMDb Database
- Test searching by title
- Test searching with no results

Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       1      0   100%
models/imdb.py          24     11    54%   22, 27-31, 35-39
--------------------------------------------------
TOTAL                   25     11    56%
----------------------------------------------------------------------
Ran 2 tests in 0.114s

OK
```

### Solution to Step 2

```python
@patch('models.imdb.requests.get')
def test_search_with_no_results(self, imdb_mock):
    """Test searching with no results"""
    imdb_mock.return_value = Mock(status_code=404)
    imdb = IMDb("k_12345678")
    results = imdb.search_titles("Bambi")
    self.assertEqual(results, {})
```

## Step 3: Search by Title Failed

Next we are going to build another failure test case but this time we need a Mock that behaves like a `Response` object from the `requests` package. We will return a good return code of `200` but we are simulating the use of a bad apikey so we need a specific error message returned. Luckily, we have one in our test fixture data.

Let's start by cutting and pasting the non-patched version of the `test_search_by_title_failed(self)` method into `test_imdb.py`. Here is the code to copy:  

```python
def test_search_by_title_failed(self):
    """Test searching by title failed"""
    imdb = IMDb("bad-key")
    results = imdb.search_titles("Bambi")
    self.assertIsNotNone(results)
    self.assertEqual(results["errorMessage"], "Invalid API Key")
```

> Notice that this instantiates a new IMDb instance passing in a bad apikey, and then calls `imdb.search_titles("Bambi")` and asserts that it sent back and error message of _"Invalid API Key"_.

In `test_imdb.py`, add the following line of code before the `test_search_by_title_failed(self)` method and add a parameter for the new mock called `imdb_mock`. This is the patch the call to `requests.get()` and allow us to control what comes back using the `imdb_mock` variable.

```python
@patch('models.imdb.requests.get')
def test_search_by_title_failed(self, imdb_mock):
```

> Notice that once again, we are patching the 3rd part library called `requests` that is imported by the `imdb` module in the `models` package (i.e, `models.imdb.requests.get`) Specifically we are patching the `get` function because we know that `IMDb.search_titles()` is going to eventually call the `requests.get()` method to make the call to the IMDb API. We want to intercept (or patch) that call to control what is returned.

We are going to send back a good return code of `200` which is going to cause the `IMDb.search_titles()` method to make this call on the returned request: `request.json()`. In order to fool `search_titles()` into thinking it got back a real `requests.Response`, we must use `spec=Response,` when creating the mock so that it behaves like the real `Response` class.

Further, we need to mock the `json()` call to return the `json` response that we want which is `INVALID_API` from our test fixture data. We will accomplish this by adding one line of code to our test before any other calls.

Next add a this line of code as the first line inside the method after the docstring and before the call to instantiate the `IMDb` class:

```python
imdb_mock.return_value = Mock(
    spec=Response,
    status_code=200, 
    json=Mock(return_value=IMDB_DATA["INVALID_API"])
)
```

> Notice this is patching the `return_value` of the `requests.get()` call with a `Mock` object that has an attribute called `status_code` set to `200`. If we look in the source code for `IMDb.search_titles()` we will see that after the call to `requests.get()` is made, it checks that the `status_code` is `200` and if it is, it then calls `request.json()` to get the payload. This is why we must also mock the call to `json()` and return the payload that we want.

Those two changes are enough to cause the `requests.get()` method to not be called and instead return a `Mock` object with a `status_code` of `200` and a `Response.json()` method that will send back the `INVALID_API` payload that we have specified when called.

Run `nosetests` and make sure the test cases pass:

```bash
nosetests
```

The results should look like this:

```
Tests Cases for IMDb Database
- Test searching by title
- Test searching by title failed
- Test searching with no results

Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       1      0   100%
models/imdb.py          24     10    58%   27-31, 35-39
--------------------------------------------------
TOTAL                   25     10    60%
----------------------------------------------------------------------
Ran 3 tests in 0.111s

OK
```

### Solution to Step 3

```python
@patch('models.imdb.requests.get')
def test_search_by_title_failed(self, imdb_mock):
    """Test searching by title failed"""
    imdb_mock.return_value = Mock(
        spec=Response,
        status_code=200, 
        json=Mock(return_value=IMDB_DATA["INVALID_API"])
    )
    imdb = IMDb("k_12345678")
    results = imdb.search_titles("Bambi")
    self.assertIsNotNone(results)
    self.assertEqual(results["errorMessage"], "Invalid API Key")
```

## Step 4: Test Movie Ratings

In this final step we are going to test the movie ratings call. Since we don't want to call the real IMDb database under test, we will once again mock the `requests.get()` call and substitute our own movie ratings response from our test fixture data.

Hopefully you can see that by patching the remote call, we can test the rest of the function code before and after the call to make sure that it behaves properly under all kinds of test conditions.

Let's start by cutting and pasting the non-patched version of the `test_movie_ratings(self)` method into `test_imdb.py`. Here is the code to copy:  

```python
def test_movie_ratings(self):
    """Test movie Ratings"""
    imdb = IMDb("k_12345678")
    results = imdb.movie_ratings("tt1375666")
    self.assertIsNotNone(results)
    self.assertEqual(results["title"], "Bambi")
    self.assertEqual(results["filmAffinity"], 3)
    self.assertEqual(results["rottenTomatoes"], 5)
```

> Notice this instantiates a new IMDb instance passing in an apikey. Then calls `imdb.movie_ratings({id})` passing in a movie id. Finally, it asserts that the results are not `None` and it checks a few of the ratings to be sure it's the correct data.

In `test_imdb.py`, add the following line of code before the `test_movie_ratings(self)` method and add a parameter for the new mock called `imdb_mock`. This is patch the call to `requests.get()` and allow us to control what comes back using the `imdb_mock` variable.

```python
@patch('models.imdb.requests.get')
def test_movie_ratings(self, imdb_mock):
```

> Notice that once again, we are patching the 3rd part library function `requests.get()` and creating a variable called `imdb_mock` that allows us to control how the patch behaves.

We are going to send back a good return code of `200` which is going to cause the `IMDb.movie_ratings()` method to make this call on the returned request: `request.json()`. In order to fool `movie_ratings()` into thinking it got back a real `requests.Response`, we must use `spec=Response,` when creating the mock so that it behaves like the real `Response` class.

Also once again, we need to mock the `json()` call to return the `json` response that we want which is `GOOD_RATING` from our test fixture data. We will accomplish this by adding one line of code to our test.

Next add a this line of code as the first line inside the method after the docstring and before the call to instantiate the `IMDb` class:

```python
imdb_mock.return_value = Mock(
    spec=Response,
    status_code=200, 
    json=Mock(return_value=IMDB_DATA["GOOD_RATING"])
)
```

> Notice this is patching the `return_value` of the `requests.get()` call with a `Mock` object that has an attribute called `status_code` set to `200`. If we look in the source code for `IMDb.movie_ratings()` we will see that after the call to `requests.get()` is made, it checks that the `status_code` is `200` and if it is, it then calls `request.json()` to get the results. This is why we must also mock the call to `json()` and return the results that we want.

Those two changes are enough to cause the `requests.get()` method to not be called and instead return a `Mock` object with a `status_code` of `200`. Then when `Response.json()` is called, it will send back the `GOOD_RATING` response that we have specified.

Run `nosetests` and make sure the test cases pass:

```bash
nosetests
```

The results should look like this:

```
Tests Cases for IMDb Database
- Test movie Ratings
- Test searching by title
- Test searching by title failed
- Test searching with no results

Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
models/__init__.py       1      0   100%
models/imdb.py          24      6    75%   27-31, 39
--------------------------------------------------
TOTAL                   25      6    76%
----------------------------------------------------------------------
Ran 4 tests in 0.109s

OK
```

### Solution to Step 4

```python
@patch('models.imdb.requests.get')
def test_movie_ratings(self, imdb_mock):
    """Test movie Ratings"""
    imdb_mock.return_value = Mock(
        spec=Response,
        status_code=200, 
        json=Mock(return_value=IMDB_DATA["GOOD_RATING"])
    )
    imdb = IMDb("k_12345678")
    results = imdb.movie_ratings("tt1375666")
    self.assertIsNotNone(results)
    self.assertEqual(results["title"], "Bambi")
    self.assertEqual(results["filmAffinity"], 3)
    self.assertEqual(results["rottenTomatoes"], 5)
```

## Conclusion

Congratulations! You just completed the **Mock Objects** lab. Hopefully you are seeing the pattern with mocking. First you use the `@patch()` decorator to wrap your test case with a patch that will change the behavior of a function call that will eventually be called during the test. Then you add a new parameter to the test method call that represent the patched object. Finally you use that parameter to patch either the `return_value` or `side_effect` that will change the behavior of the patched function.

You also learned how to use Mock objects to mimic other classes like the `Response` class, to control how they behave and what they return. You even mocked the `json()` function call on the mocked `Response` class to control what it returned.

Your next challenge is to apply these techniques in your projects to mock out any external dependencies during testing so that you can be sure that you are testing the behavior of your code, and not someone else's service.

## Author(s)

John Rofrano

## Changelog

| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2022-04-16 | 1.0 | Rofrano | Create new Lab |
|   |   |   |   |
|   |   |   |   |

## <h3 align="center"> © IBM Corporation 2022. All rights reserved. <h3/>
