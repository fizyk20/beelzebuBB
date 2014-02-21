from flaskbb import app
from flaskbb.core import BaseView
from flask import render_template

class IndexView(BaseView):
    _name = 'base.index'
    
    def __init__(self):
        app.add_url_rule('/', 'index', self.view)
    
    def view(self, *args):
        return render_template('index.html')