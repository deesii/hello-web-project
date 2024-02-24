# File: tests/test_app.py

# Note: you will need to do this in the starter codebase.

"""
When: I make a GET request to /
Then: I should get a 200 response
"""
def test_get_wave(web_client):
    # We'll simulate sending a GET request to /wave?name=Dana
    # This returns a response object we can test against.
    response = web_client.get('/wave?name=Dana')

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'I am waving at Dana'

"""
When: I make a POST request to /submit
And: I send a name and message as body parameters
Then: I should get a 200 response with the right content
"""
def test_post_submit(web_client):
    # We'll simulate sending a POST request to /submit with a name and message
    # This returns a response object we can test against.
    response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'

# To run these tests:
# ; pipenv shell
# ; pytest tests/test_app.py
    
#adding further tests (Exercise 1)
    
# File: tests/test_app.py

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'


# excercise 2 
    
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


