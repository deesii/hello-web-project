# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```

# Sort names route

POST / sort-names
    names: string (comma separated list)
    
# Request:
POST http://localhost:5000/sort-names

# With body parameters:
names=Joe,Alice,Zoe,Julia,Kieran

# Expected response (sorted list of names):
Alice,Joe,Julia,Kieran,Zoe

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE


# POST /sort-names
#  Parameters: names = Joe,Alice,Zoe,Julia,Kieran
#  Expected response (200 ok ): 'Joe,Alice,Zoe,Julia,Kieran'
"""
Please provide a name and a message
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
'''
When: I make a POST request to /sort-names
AND: I send "Joe,Alice,Zoe,Julia,Kieran" 
THEN : I get a 200 response with the order of the name 
(as comma,separated values) as "Alice,Joe,Julia,Kieran,Zoe"
'''

def test_post_sort_names(web_client):
    names = "Joe,Alice,Zoe,Julia,Kieran" 
    response = web_client.post('/sort-names' , data = {"names": names} )
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Alice,Joe,Julia,Kieran,Zoe"

'''
When: I make a POST request to /sort-names
AND: I send "Aaaa,Aaa,Aaab,Aaac,Aad" 
THEN : I get a 200 response with the order of the name 
(as comma,separated values) as "Aaa,Aaaa,Aaab,Aaac,Aad"

'''


def test_post_sort_names_starting_letters(web_client):
    names = "Aaaa,Aaa,Aaab,Aaac,Aad" 
    response = web_client.post('/sort-names' , data = {"names": names} )
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Aaa,Aaaa,Aaab,Aaac,Aad"




'''
When: I make a POST request to /sort-names
AND: I send nothing
THEN : I get a 400 response with "You have not specified a list!"
'''


def test_post_sort_names_no_input(web_client):
    
    response = web_client.post('/sort-names' )
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "You have not specified a list!"