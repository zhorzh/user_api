This USER API has three main parts:

core: this is WSGI application made with Flask framework, application config and sqlite database.
    http://flask.pocoo.org
    https://www.sqlite.org
    
identity: this part contains user model and provide REST API with Json Web Token(JWT) authentication.
    https://tools.ietf.org/html/rfc7519

features: this part contains BDD tests built with behave python library.
    http://pythonhosted.org/behave/

To run this API please install dependencies, run the tests and launch the web app:
    pip install -r requirements.txt
    behave
    python run.py
