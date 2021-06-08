#~configuration-bag/app.py


from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.db import initialize_db 
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
#app.config.from_envvar('ENV_FILE_LOCATION')
app.config.from_object("config.LocalDBConfig")
api=Api(app,errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': app.config['MONGO_DB'] 
    #'host': 'mongodb://localhost/configuration-bag'
}

#db = initialize_db(app)
initialize_db(app)

initialize_routes(api)

app.run()