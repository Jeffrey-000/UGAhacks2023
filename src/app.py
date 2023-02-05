import os 
from flask import Flask as onlyfans
from flask import render_template, request  
from dotenv import load_dotenv
from directionsv2 import directions
import urllib.parse
from gasprices import getGasPrices

load_dotenv()
GKEY = os.getenv("GOOGLE")
RKEY = os.getenv("RAPID")

your_mom = __name__

justkillmerightnow = []

app = onlyfans(your_mom)

brain = directions(GKEY, RKEY, 0, 0)

currentUrl = ''

@app.route('/')
def home():
    return render_template("map.html", url=brain.makeUrl("default"))

@app.route('/', methods=['POST', 'GET'])
def calc(start=None, end=None, mpg=1, tank=1):
    display = "default"
    if request.method == "POST":
        start = request.form['start']
        end = request.form['end']
        mpg = request.form['mpg']
        tank = request.form['tank']
        try:
            brain.updateVar(mpg, tank)
            start = brain.geocoding(start)
            end = brain.geocoding(end)
            route = brain.detailedDistances(start, end)
            display = brain.doMeth(route)
            currentUrl = brain.makeUrl(display)
            average  = makeTable(db=justkillmerightnow, data=display, link=currentUrl)
            distance = route['route']['distance'] / 1609.34
            length = distance / (int(mpg) * int(tank))
        except:
            print("exception")
    return render_template("map.html", url=currentUrl, db=justkillmerightnow, trip=length * average)



def makeTable(db=None, data=[], link=""):
    total = 0
    counter = 0
    for x in data:
        cityName = brain.getCity(x[0], x[1])
        gasPrice = getGasPrices(x[0], x[1], 1)[0]
        total += gasPrice
        gasPrice = "{:.2f}".format(gasPrice)
        link = "&waypoints=" + str(x[0]) + "," + str(x[1])
        link = urllib.parse.quote_plus(link)
        y = (cityName, '$' + gasPrice, link)
        db.append(y)
        counter += 1
    return total / counter


#opens a developmental server when play button is run
#make sure all code goes above these lines

if __name__ == "__main__":
    app.run(debug=True)
