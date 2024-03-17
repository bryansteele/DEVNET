import json
import os
from pprint import pprint

here = os.path.abspath(os.path.dirname("/Users/bryan/dne-devfun-code/"
                            "intro-python/parsing-json/nested_data.py"))

with open(os.path.join(here, "/Users/bryan/dne-devfun-code/"
                            "intro-python/parsing-json/nested_data.py")) as file:
    json_text = file.read()

print(json_text) 

