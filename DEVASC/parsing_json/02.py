import json
import os

here = os.path.abspath(os.path.dirname("/Users/bryan/dne-devfun-code/"
                            "intro-python/parsing-json/interfaces.json"))

with open(os.path.join(here, "/Users/bryan/dne-devfun-code/"
                            "intro-python/parsing-json/interfaces.json")) as file:
    json_text = json.loads(file.read())

for i in json_text["ietf-interfaces:interfaces"]["interface"]:
    print("{name}: {ip} {netmask}".format(
    name = i["name"],
    ip = i["ietf-ip:ipv4"]["address"][0]["ip"],
    netmask = i["ietf-ip:ipv4"]["address"][0]["netmask"],
    ))