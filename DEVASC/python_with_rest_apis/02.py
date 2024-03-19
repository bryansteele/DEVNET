import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"
querystring = {"deck_count": "6"}
headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "dd1d8ca5-7000-21b2-2230-39969d585419"
    }
response = requests.request("GET", url, headers=headers, params=querystring)

if response.status_code == 200:
    deck_id = response.json()['deck_id']
    requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/")
else:
    print(f"Request unsuccessful. Status code: {response.status_code}")
    exit()

draw_response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/"
                                "draw/?count=5")
draw = draw_response.json()

i = 1
for card in draw['cards']:
    print(f"Card {i} is {card['value']} of {card['suit']}")
    i +=1

#print(response.text)