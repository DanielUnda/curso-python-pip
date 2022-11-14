import requests

def get_catehories():
    r=requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    categories=r.json()
    for category in categories:
        print(category['name'])