import requests

class API():
    url = "https://aerodatabox.p.rapidapi.com/airports/%7BcodeType%7D/DME"

headers = {
	"X-RapidAPI-Key": "008d59df7dmsh67f80f56bd24c7cp13f1d2jsn3ab57e172675",
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

