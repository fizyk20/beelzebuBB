from flask import Flask, render_template

app = Flask(__name__)

import beelzebubb.config
import beelzebubb.plugins