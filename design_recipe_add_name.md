# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```

# Sort names route

POST / sort-names
    names: string (comma separated list)
    
# Request:
POST http://localhost:5000/name

# With GET query parameters:
add=Eddie

# Expected response (sorted list of names):
Julia, Alice, Karim, Eddie

the predefined list is "Julia, Alice, Karim"

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE


# GET/name
#  Parameters: add = Eddie
#  Expected response (200 ok ): "Julia, Alice, Karim, Eddie"
"""
Please provide a name and a message
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

'''
# Request:
When: I make a GET request to /names?add=Eddie (sending a name with Eddie as the parameter)

# This route returns a list of pre-defined names, plus the name Eddie.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie
'''

def test_get_add_name_to_predefined_list(web_client):
    response = web_client.get('/name?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Julia, Alice, Karim, Eddie"

'''
# Request:
When: I make a GET request to /names?add= (sending a name with no parameter)

# This route returns the error "No name added!"

# Expected response (400):
"No name added!"
'''

def test_get_add_no_name_to_predefined_list(web_client):
    response = web_client.get('/name')
    assert response.status_code == 400 
    assert response.data.decode('utf-8') == "No name added!"

