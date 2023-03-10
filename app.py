from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

def main():
    import uvicorn
    from docopt import docopt

    help_doc = """
A Web accessible FastAPI server that allow reviewers to review posts.

Usage:
  app.py [-c | -c -d] [-p PORT] [-h HOST_IP] [-r]

Options:
  -p PORT, --port=PORT                 Listen on this port [default: 8000]
  -h HOST_IP, --host=HOST_IP           Listen on this IP address [default: 127.0.0.1]
  -r, --reload                         Reload the application
"""
    args = docopt(help_doc)    
            
    uvicorn.run(
        'app:app', 
        port = int(args['--port']),
        host = args['--host'],
        reload = args['--reload'],
    )

if __name__ == '__main__':
    main()