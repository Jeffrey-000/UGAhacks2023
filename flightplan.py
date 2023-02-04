import requests

class API():
    url = "https://aerodatabox.p.rapidapi.com/airports/%7BcodeType%7D/DME"

headers = {
	"X-RapidAPI-Key": "008d59df7dmsh67f80f56bd24c7cp13f1d2jsn3ab57e172675",
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

{'distance': {
    'text': '10 ft', 'value': 3}, 
    'duration': {
    'text': '1 min', 
    'value': 0}, 
    'end_location': {'lat': 33.8160679, 'lng': -117.9225314}, 
    'html_instructions': 'Head <b>southwest</b>', 
    'polyline': {'points': 'qukmEvvvnUB@'}, 
    'start_location': {'lat': 33.8160897, 'lng': -117.9225226}, 'travel_mode': 'DRIVING'}