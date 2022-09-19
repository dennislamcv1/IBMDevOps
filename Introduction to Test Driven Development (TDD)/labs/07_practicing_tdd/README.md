# Lab 7: Practicing Test Driven Development

Welcome to the **Practicing Test Driven Development** lab. It is important to understand the workflow for practicing true test driven development by writing the test cases first to describe the behavior of the code, and then writing the code to make the tests pass, thus ensure that it has that behavior. In this lab we will do just that.

## Update a counter

You will start by implementing a test case to test updating a counter. Following REST API guidelines, an update uses a `PUT` request and returns code `200_OK` if successful. Create a counter and then update it.

Then you’ll write the code to make the test pass. If you’re unfamiliar with Flask, note that all of the routes for the counter service are the same; only the method changes.

To start, you will implement a function to update the counter. Per REST API guidelines, an update uses a PUT request and returns a `200_OK` code if successful. Create a function that updates the counter that matches the specified name.

## Read a counter

Next, you will write a test case to read a counter. Following REST API guidelines, a read uses a `GET` request and returns a `200_OK` code if successful. Create a counter and then read it.

Once again, it's time to write code to make a test pass. You will implement the code for read a counter. Per REST API guidelines, a read uses a GET request and returns a `200_OK` code if successful. Create a function that returns the counter that matches the specified name.

## Delete a counter

Now you will write a test case to delete a counter. Per REST API guidelines, a read uses a `DELETE` request and returns a `204_NO_CONTENT` code if successful. Create a function that deletes the counter that matches the specified name.

In this last step, you will again write code to make a test pass. This time, you will implement the code to delete a counter. Per REST API guidelines, a delete uses a `DELETE` request and returns a `204_NO_CONTENT` code if successful.
