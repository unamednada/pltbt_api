from flask import Flask, send_file

from api.utils.service import dim_return


app = Flask(__name__)


@app.route('/')
def test():
    return 'API is working. Try GET at /api/dim.'


@app.route('/api/dim')
def dim():
    return dim_return()


@app.route('/api/fatovalores')
def fatovalores():
    return send_file('./files/fatovalores.json', mimetype='application/json')
