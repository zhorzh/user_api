This USER API has three main parts:

core: this is WSGI application made with Flask framework, application config and postgres database.
    http://flask.pocoo.org
    
identity: this part contains user model and provide REST API with Json Web Token(JWT) authentication.
    https://tools.ietf.org/html/rfc7519

features: this part contains BDD tests built with behave python library.
    http://pythonhosted.org/behave/

To create database install postgress and run:
    sudo -i -u
    psql -c "create user api with password '123'"
    psql -c "create database api_database with owner api"
    python create_tables.py

To run this API please install dependencies, run the tests and launch the web app:
    pip install -r requirements.txt
    behave
    python run.py
