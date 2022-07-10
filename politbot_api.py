from mongo_client import client
from pprint import pprint


dim_table = client.get_database('politbotDB').get_collection('dim').find()

for info in dim_table:
    pprint(info)
    print('\n')

fatovalores_table = client.get_database(
  'politbotDB').get_collection('fatovalores').find().limit(10)

# for info in fatovalores_table:
#     pprint(info)
#     print('\n')
