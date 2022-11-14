import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact')
def get_dict():
    return {'name':'daniel'}

@app.get('/HTML')
def get_html():
    return """
        <h1> Soy una pagina</h1>
    """

def run():
    store.get_catehories()

if __name__=='__main__':
    run()