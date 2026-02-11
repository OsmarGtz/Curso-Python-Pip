import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1, 2, 3]

@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
    <h1>Contact us</h1>
    <p>Phone: 123-456-7890</p>
    Mexico City, Mexico"""

def run():
    store.get_categories()

if __name__ == '__main__':
    run()