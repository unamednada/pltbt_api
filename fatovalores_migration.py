from mongo_client import client
import json


try:
    db = client.politbotDB

    with open('./files/fatovalores.json') as f:
        fatovalores = json.load(f)
        db.fatovalores.insert_many(fatovalores["dados"])
    print("Migration completed")
except Exception as e:
    print(e)
    print("Migration failed")
    exit(1)
finally:
    client.close()
    exit(0)
