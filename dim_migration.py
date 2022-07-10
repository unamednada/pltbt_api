from mongo_client import client
import json


def fix_keys(data):
    for item in data:
        item['Codigo'] = item['C�digo']
        item['Coligacao'] = item['Coliga��o']
        del item['C�digo']
        del item['Coliga��o']


def fix_values(data):
    for item in data:
        if item['Estado'] == 'S�O PAULO':
            item['Estado'] = 'SAO PAULO'


try:
    db = client.politbotDB

    with open('./files/dim.json') as f:
        dim = json.load(f)
        fix_keys(dim)
        fix_values(dim)
        db.dim.drop()
        db.dim.insert_many(dim)
    print("Migration completed")
except Exception as e:
    print(e)
    print("Migration failed")
    exit(1)
finally:
    client.close()
    exit(0)
