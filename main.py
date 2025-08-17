from fastapi import FastAPI 

app = FastAPI() # Creates an API object that will initialise the API in our code. 

# We are beginning to define the endpoints that our API will give access to.

@app.get("/")
def home():
    return {"Data" : "test"}

@app.get("/about/")
def about():
    return {"Data" : "This is the data on the endpoint about."}

