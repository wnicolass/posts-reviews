# Simple Blog 🖊️
Posts and reviews... Hmmm... Maybe it can be a blog?

## Create a virtual environment for Python

Open a command line (or the VS Code integrated terminal). On Unix, under the 
root folder, issue the following command:

    $ python3 -m venv .venv

This will create a virtual environment for Python inside the `.venv` directory.
VS Code will automatically detect this directory and will use the python 
interpreter inside that directory. 

**NOTE 1**: On Windows use `python` instead of `python3`.

**NOTE 2**: Please read 
[venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

## Activating the Virtual Environment

Whenever you open the terminal, you need to activate it with:

    $ source .venv/bin/activate

In Windows do:

    C:\> .venv\Scripts\activate.bat      -> cmd
    C:\> .venv\Scripts\Activate.ps1      -> PowerShell
    
After activating the virtual environment, execute:
    
```bash
pip install -r requirements.txt
```
## Running the Application

Before running the application, copy the **.env.example** to **.env** and add your connection string.

**NOTE 3**: This app was developed using MySQL. All SQLAlchemy models were developed to work with this dialect, so if you want to use another one, adapt the models so that the app works well.

With all modules installed, you can see all available commands with:

```bash
python app.py --help
```
