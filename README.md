# Flask-Test

A simple program to test the implementation of flask with the project: Bucket-List-Ultima

## Testing the server class:
Flask enabled environment is not necessary for this test.
Edit the test cases in the test/test_server.py file by varying input and observe the unittest result messages.
Tests available:
1. Email address validity
2. Input matched against existing records when creating new clients
    Input tested is:
    i. Email address
    ii. Username
    iii. Password
3. Delete clients
4. View bucket lists by client username
5. Search for username using email address
6. View bucket list by its name

## Testing the client class:
Flask enabled environment is not necessary for this test.
Edit the test cases in the test/test_client.py file by varying input and observe the unittest result messages.
Tests available:
1. Create new bucket lists
2. Input matched against existing records when creating new bucket lists
    Input tested is list name
3. View bucket lists in client object
4. Delete bucket list
5. Follow another user's bucket list