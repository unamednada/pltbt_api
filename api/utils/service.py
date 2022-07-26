import json

from flask import jsonify


def read_json(file_name):
    with open(file_name) as f:
        return json.load(f)


def dim_return():
    full_dim = read_json(
      '/home/unamednada/politbot/pltbt_api/api/files/dim.json')
    return jsonify(
      [{'nome': d['Nome'], 'twitter': d['Twitter']} for d in full_dim])
