from flask import Flask, render_template

app = Flask(__name__)

import flaskbb.config
import flaskbb.plugins