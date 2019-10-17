import requests
r = reqests.post('http:/localhost:5000/aptients', json{''name:'bill', 'id': 0})
print(r.status_code)