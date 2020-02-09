from flask import Flask
from views.hello import world
app = Flask(__name__)
app.add_url_rule('/', 'index', world)

