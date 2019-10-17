import requests
URL = 'http:/localhost:5000/aptients'
def test_create()
	r = reqests.post('http:/localhost:5000/aptients', json{''name:'bill', 'id': 0})
	assert r.status_code() == 201

def test_read()
	r = reqests.get(URL+ '\0'})
	assert r.json() == 'Bill'
    
def test_list()
	r = reqests.get(URL})
	assert len(r.json()) == 0

def test_delete()
	r = reqests.delete(URL +'/0'})
	assert r.status_code() == 204
def test_update()
	r = reqests.put(URL +'/0'})
	assert r.status_code() == 201