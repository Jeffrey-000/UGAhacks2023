import requests
import json

class steps:

    url = "https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key="
    key = "AIzaSyABX1PJ8A4S6LRrPWwnnnFlIscn5etDQM0"

    response = requests.get(url + key).json()["routes"][0]['legs'][0]["steps"]

    jsonString = json.dumps(response)
    fDict = json.loads(jsonString)

    startLocaList = []
    distList = []

    def mileConverter(dist):
        form = dist.split(' ')
        num = float(form[0])
        unit = form[1]
        if (unit == 'ft'):
            num /= 52800
        return num
    

    for x in fDict:
        startLocaList.append(x['start_location'])
        distList.append(mileConverter(x['distance']['text']))

    gasMiles = 1.0
    milesDriven = 0.0

    print(startLocaList)
    print()
    print(distList)
    print()

    length = len(distList)
    pos = 0

    updatedStartLocaList = []

    while (pos < length - 1):
        if (milesDriven + distList[pos + 1] >= gasMiles):
            updatedStartLocaList.append(startLocaList[pos])
            print(distList[pos])
            milesDriven = 0.0
        milesDriven + distList[pos + 1]
        pos += 1
    
    print(updatedStartLocaList)
            

