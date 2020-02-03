import flask
from flask_sessionstore import Session
# from pfchar.settings import SECRET_KEY, DEBUG
from pfchar.settings import DEBUG
from pfchar.server.views import Views
from pfchar.server.routes import Routes
from pfchar.server.rest import RESt
from pfchar.database.connection import redis_instance_sessions


app = flask.Flask(__name__)
SESSION_TYPE = 'redis'
SESSION_REDIS = redis_instance_sessions
app.config.from_object(__name__)
Session(app)

views = Views()
rest = RESt()
routes = Routes(app, views, rest)
