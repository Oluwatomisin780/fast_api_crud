from http.client import HTTPException
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI
from models import Blog, update_Blog_Request
from typing import List
app =FastAPI()

Blog_db:List[Blog] = [
   Blog(
       id ='842d6722-629b-4eed-a935-3bf57e081ef7',
       title= 'my first blog post',
       description = 'this is my first blog post',
       link ='fsdskksddkasd'

   )
   
    
]

@app.get('/')
async def root():
    return {'hello':'goodmorning'}

@app.get('/api/v1/blogs')
async def get_post():
    return Blog_db

@app.post('/api/v1/blogs')
async def create_post(blog:Blog):
    return Blog_db.append(blog)

@app.delete('/api/v1/blog/{blog_id}')
async def delete_post(blog_id:UUID):
    for post in Blog_db:
        if post.id ==blog_id:
            Blog_db.remove(post)
            return 'deleted'
    raise HTTPException(
        status_code =404,
        detail = 'user does not exist '
    )
@app.put('/api/v1/blog/{blog_id}')
async def update_post(update_post:update_Blog_Request,blog_id:UUID):
    for blog in Blog_db:
        if blog.id == blog_id:
            if update_post.title is not None:
                blog.title = update_post.title
            if update_post.description is not None:
                blog.description = update_post.description
            if update_post.link is not None:
                blog.link = update_post.link
            if update_post.updated_At is not None:
                blog.link = update_post.updated_At
            return
    raise HTTPException(
        status_code =404,
        detail=(f'blog with {blog_id} does not exist')
    )
            