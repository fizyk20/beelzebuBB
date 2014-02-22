from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flaskbb.config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
from flaskbb import app

engine = create_engine('postgresql://%s:%s@%s:%s/%s' % 
                        (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME), 
                       convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

from flaskbb.core import BaseModel
BaseModel.query = session.query_property()

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()