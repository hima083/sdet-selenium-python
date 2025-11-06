import requests

BASE = 'https://jsonplaceholder.typicode.com'

def test_get_posts():
    r = requests.get(f'{BASE}/posts')
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_create_post():
    payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
    r = requests.post(f'{BASE}/posts', json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data.get('title') == 'foo'
