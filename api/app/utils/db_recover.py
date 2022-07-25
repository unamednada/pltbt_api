from api.db.mongo_client import client

dim_table = client.get_database('politbotDB').get_collection('dim').find()

fatovalores_table = client.get_database(
  'politbotDB').get_collection('fatovalores').find()
