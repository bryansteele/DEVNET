import json
import os
from pprint import pprint

here = os.path.abspath(os.path.dirname("/Users/bryan/dne-devfun-code/"
                            "intro-python/parsing-json/interface-config.json"))

with open(os.path.join(here, "/Users/bryan/dne-devfun-code/intro-python/"
                            "parsing-json/interface-config.json")) as file:
    json_text = file.read()

print("json_text is a", type(json_text))

print('########################################################')
print(json_text)

print('########################################################')

json_data = json.loads(json_text)

print("json_data is a", type(json_data))

print('########################################################')

pprint(json_data)

print('########################################################')

pprint(json_data["ietf-interfaces:interface"])

print('########################################################')

print(json_data["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"])

