import requests
import urllib.parse
import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("GOOGLE")
rapid = os.getenv("RAPID")

class directions:
    def __init__(self, GKEY, RKEY, mpg, size):
    #origin=Disneyland&destination=Universal+Studios+Hollywood&key='
        self.GKEY=GKEY
        self.RKEY=RKEY
        self.metersPerTank=mpg * size * 1609.34
  
    #turns list of points on a direction route
    def detailedDistances(self, start, stop):
        URL = "https://trueway-directions2.p.rapidapi.com/FindDrivingRoute?rapidapi-key=" + self.RKEY + "&stops="
        data = requests.get(URL + str(start['lat']) + ',' + str(start['lng']) + ';' + str(stop['lat']) + ',' + str(stop['lng']))
        return data.json()      

    def geocoding(self, address):
        URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=' + self.GKEY
        data = requests.get(URL + '&address=' + urllib.parse.quote_plus(address))
        return data.json()['results'][0]['geometry']['location']
    
    def doMeth(self, data):
        distance = data['route']['distance']
        data = data['route']['geometry']['coordinates']
        changeInDistance = distance / len(data)
        index = self.metersPerTank / changeInDistance
        importantPoints = []
        if index < 1:
            return -1
        else:
            counter = index
            while (counter < len(data)):
                mydic = {
                    "dist" : counter * index,
                    "cord" : data[int(counter)]
                    }
                importantPoints.append(mydic)
                counter += index
            return importantPoints



def main():
    bot = directions(key ,rapid, 5 , 1)
    start = bot.geocoding("2776 sudbury trace")
    end = bot.geocoding('900 south lumpkin street')
    data = bot.detailedDistances(start, end)
    data = bot.doMeth(data)
    
    print(data)
    #print(bot.detailedDistances(data))
    #for x in bot.distances(data):
        #print(x[1])
        #print("\n")

if __name__ == "__main__":
    main()