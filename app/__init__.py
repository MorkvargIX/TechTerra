from flask import Flask
from .view.index import index

app = Flask(__name__)
app.register_blueprint(index)



