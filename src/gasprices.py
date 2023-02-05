import requests
import json
import ast
import math

# return (avg price (assume that it will be really super duper long), cheapest price) (includes gas stations whose prices are not listed)
def getGasPrices(lat,lng, fuelType): #1-4 for regular, midgrade, premium, diesel

    avgPrice = 0.00;
    cheapestPrice = 0.00;

    stations_list = list()
    url = "https://www.gasbuddy.com/gaspricemap/map"
    station_url = "https://www.gasbuddy.com/gaspricemap/station"

    # trig stuff to find lat + long changes in 5 mile radius
    lat_radian = math.radians(lat)

    deg_lat_miles = 69
    deg_long_miles = 69 * math.cos(lat_radian)
    delta_lat = 5 / deg_lat_miles
    delta_long = 5 / deg_long_miles

    top_lat = lat + delta_lat
    bottom_lat = lat - delta_lat
    left_lng = lng - delta_long
    right_lng = lng + delta_long

    # payload for stations
    payload = { 
    "fuelTypeId": str(fuelType),   
    "height": "1000",
    "maxLat": str(top_lat),
    "maxLng": str(right_lng),
    "minLat": str(bottom_lat),
    "minLng": str(left_lng),
    "width":  "1000"
    }

    # receives data of stations around
    response = requests.post(url, data=payload)

    # adds prices from primaryStations + secondaryStations into stations_list
    for data in response.json()['primaryStations']:
        if(data['price'] != '--'):
            stations_list.append(data['price'])

    for data in response.json()['secondaryStations']:
        if(data['price'] != '--'):
            stations_list.append(data['price'])

    # finds minimum price
    min = float(stations_list[0]);

    for i in stations_list:

        avgPrice += float(i)

        if(min > float(i)):
            min = float(i) 
    
    answer = list((avgPrice/len(stations_list), min))

    return answer