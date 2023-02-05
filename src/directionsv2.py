import requests
import urllib.parse

class directions:
    def __init__(self, GKEY, RKEY, mpg, size):
        self.GKEY=GKEY
        self.RKEY=RKEY
        self.metersPerTank=mpg * size * 1609.34

    def updateVar(self, mpg, size):
        if len(mpg) != 0 and len(size) != 0:
            if type(mpg) == int and type(size) == int:
                self.metersPerTank=mpg * size * 1609.34
  
    #turns list of points on a direction route
    def detailedDistances(self, start, stop):
        print("detailed ran")
        URL = "https://trueway-directions2.p.rapidapi.com/FindDrivingRoute?rapidapi-key=" + self.RKEY + "&stops="
        data = requests.get(URL + str(start['lat']) + ',' + str(start['lng']) + ';' + str(stop['lat']) + ',' + str(stop['lng']))
        if data.status_code != 200:
            raise Exception("detailed distances")
        return data.json()      

    def geocoding(self, address):
        print("geocoding yes")
        URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=' + self.GKEY
        data = requests.get(URL + '&address=' + urllib.parse.quote_plus(address))
        if data.status_code != 200:\
            raise Exception("geocoding")
        return data.json()['results'][0]['geometry']['location']
    
    def doMeth(self, data):
        print("do meth rran")
        #distance of route
        distance = data['route']['distance']
        #list of all data points for route
        data = data['route']['geometry']['coordinates']
        #the amount of distance convered for each index  change
        changeInDistance = distance / len(data)
        #how many indexes to change before running out of gas
        index = self.metersPerTank / changeInDistance
        #if able to make it on 1 full tank of gas it returns -1
        importantPoints = []
        if index < 1:
            importantPoints.append(data[0])
            importantPoints.append(data[-1])
        else:
            counter = index
            #dist is distance in meters
            #coords is coordinates 
            #0 is lat
            #1 is longitude
            while (counter < len(data)):
                importantPoints.append(data[int(counter)])
                counter += index
        return importantPoints

    def makeUrl(self, args):
        print("make url ran")
        if args == "default":
            return "https://www.google.com/maps/embed/v1/place?key=" + self.GKEY + "&q=University+of+Georgia"
        start = "&origin={},{}".format(args[0][0], args[0][1])
        end = "&destination={},{}".format(args[-1][0], args[-1][1])
        URL = "https://www.google.com/maps/embed/v1/directions?key=" + self.GKEY 
        print(URL + start + end )
        return URL + start + end 

