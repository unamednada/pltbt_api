from flask import Flask, jsonify
from api.app.utils.db_recover import dim_table, fatovalores_table

app = Flask(__name__)


@app.route('/')
def test():
    return 'API is working. Try GET at /api/dim.'


@app.route('/api/dim')
def dim():
    response = app.response_class(
        response=jsonify(dim_table.__dict__),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route('/api/fatovalores')
def fatovalores():
    response = app.response_class(
        response=fatovalores_table,
        status=200,
        mimetype='application/json'
    )

    return response
