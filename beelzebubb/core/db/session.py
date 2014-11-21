from beelzebubb.config import DB_ENGINE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
from beelzebubb import app
from .sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = '%s://%s:%s@%s:%s/%s' % (DB_ENGINE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
db = SQLAlchemy(app)