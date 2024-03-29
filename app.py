from fastapi import FastAPI
from fastapi_chameleon import global_init
from fastapi.staticfiles import StaticFiles
from views import (review, post)
from config.database import create_metadata

app = FastAPI()

def main():
    start_uvicorn()

app.mount('/static', StaticFiles(directory = 'static'), name = 'static')
app.include_router(post.router)
app.include_router(review.router)
global_init('./templates')

# def config_routes():
#     for view in [post, review]:
#         app.include_router(view.router)

def start_uvicorn():
    import uvicorn
    from docopt import docopt

    help_doc = """
A Web accessible FastAPI server that allow reviewers to review posts.

Usage:
  app.py [-c] [-p PORT] [-h HOST_IP] [-r]

Options:
  -p PORT, --port=PORT                 Listen on this port [default: 8000]
  -c, --create-ddl                     Create datamodel in the database
  -h HOST_IP, --host=HOST_IP           Listen on this IP address [default: 127.0.0.1]
  -r, --reload                         Reload the application
"""
    args = docopt(help_doc)    
    create_ddl = args['--create-ddl']
    if create_ddl:
        create_metadata()

    uvicorn.run(
        'app:app', 
        port = int(args['--port']),
        host = args['--host'],
        reload = args['--reload'],
        reload_includes=[
            '*.pt',
            '*.css',
        ]
    )

if __name__ == '__main__':
    main()