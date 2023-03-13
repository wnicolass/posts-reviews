from fastapi import FastAPI
from routes import review_routes, post_routes
from config.database import create_metadata

app = FastAPI()

app.include_router(post_routes.router)
app.include_router(review_routes.router)

def main():
    # config_routes()
    start_uvicorn()

# def config_routes():
#     for rtr in [review_routes, post_routes]:
#         app.include_router(rtr.router)

def start_uvicorn():
    import uvicorn
    from docopt import docopt

    help_doc = """
A Web accessible FastAPI server that allow reviewers to review posts.

Usage:
  app.py [-c | -c -d] [-p PORT] [-h HOST_IP] [-r]

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
    )

if __name__ == '__main__':
    main()