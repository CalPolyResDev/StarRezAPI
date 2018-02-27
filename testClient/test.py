import os
import starrez_client

from dotenv import find_dotenv, load_dotenv
from starrez_client.rest import ApiException

# In order for this to work a .env file must be in project root
load_dotenv(find_dotenv())

configuration = starrez_client.Configuration()
configuration.username = os.environ.get("USERNAME")
configuration.password = os.environ.get("PASSWORD")
configuration.host = os.environ.get("HOST")
api_instance = starrez_client.DefaultApi(starrez_client.ApiClient(configuration))

entry_id = 51431
name_web = 'test@calpoly.edu'

entry_item = starrez_client.EntryItem()
entry_item.name_web = name_web

api_instance.update_entry(entry_id, entry_item)

test = api_instance.search_entry(name_last="Reis")

# print(test)

try:
    api_instance.search_entry()
except ApiException as e:
    if e.body:
        print(e.body)
    else:
        print(e)
