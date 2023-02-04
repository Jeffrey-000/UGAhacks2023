import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()
KEY = os.getenv("GOOGLE")

class steps:

    url = "https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key="
 

    response = requests.get(url + KEY).json()["routes"][0]['legs'][0]["steps"]

    # turns list into json, and then to dictionary
    jsonString = json.dumps(response)
    fDict = json.loads(jsonString)

    # tracks start location and distance
    startLocaList = []
    distList = []

    # converts everything into miles
    def mileConverter(dist):
        form = dist.split(' ')
        num = float(form[0])
        unit = form[1]
        if (unit == 'ft'):
            num /= 52800
        return num
    

    # extraxts start ,ocations and distance
    for x in fDict:
        startLocaList.append(x['start_location'])
        distList.append(mileConverter(x['distance']['text']))

    gasMiles = 1.0 # gas milage of car
    milesDriven = 0.0

    print(startLocaList)
    print()
    print(distList)
    print()

    length = len(distList)
    pos = 0

    startLocaListPos = [] # positions where refill is needed

    while (pos < length - 1):
        if (milesDriven + distList[pos] >= gasMiles):
            startLocaListPos.append(pos)
            print(distList[pos])
            milesDriven = 0.0
        milesDriven + distList[pos]
        pos += 1
    
    pos = 0
    length = len(startLocaListPos)

    updatedPointsLoca = []
    updatedPointsDist = []

    # makes updated list and dictionary with points where refill will be needed
    while (pos < length):
        updatedPointsLoca.append({'start':startLocaList[startLocaListPos[pos]], 'end':startLocaList[startLocaListPos[pos] + 1]})
        updatedPointsDist.append(distList[startLocaListPos[pos]])
        pos += 1
    
    print(updatedPointsLoca)
    print(updatedPointsDist)
            

