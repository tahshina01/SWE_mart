from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app =FastAPI()

@app.get('/blog')
def index(limit=10, published:bool=True, sort:Optional[str]=None):
    if published:
        return {'data': f'{limit} published blocks'}
    else:
        return {'data': f'{limit} blogs from db'}

@app.get('/blog/unpub')
def unpublished():
    return {'data':'unpublished'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}

class Blog(BaseModel):
    title: str
    body:str
    published: Optional[bool]
    
@app.post('/blog')
def create_blog(request:Blog):
    return {'data':f"Blog is created as {request.title}"}