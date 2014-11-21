from beelzebubb.core import BaseView
from flask import render_template

class IndexView(BaseView):
    _name = 'base.index'
    url = '/'
    
    def view(self, *args, **kwargs):
        return render_template('index.html')