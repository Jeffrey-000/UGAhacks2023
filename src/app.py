import os 
from flask import Flask as onlyfans
from flask import render_template, request  
from dotenv import load_dotenv
from directionsv2 import directions
from gasprices import getGasPrices

load_dotenv()
GKEY = os.getenv("GOOGLE")
RKEY = os.getenv("RAPID")

your_mom = __name__

justkillmerightnow = []

app = onlyfans(your_mom)

brain = directions(GKEY, RKEY, 0, 0)

@app.route('/')
def home():
    return render_template("map.html", url=brain.makeUrl("default"))

@app.route('/', methods=['POST', 'GET'])
def calc(start=None, end=None, mpg=0, tank=0):
    display = "default"
    if request.method == "POST":
        print("if statment")
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
            makeTable(db=justkillmerightnow, data=display, link=brain.makeUrl(display))
        except:
            print("exception")
    return render_template("map.html", url=brain.makeUrl(display), db=justkillmerightnow)

@app.route('/<url>')
def waypoint(url):
    return render_template("map.html", url=brain.makeUrl(url, waypoint=True), db=justkillmerightnow)

def makeTable(db=None, data=[], link=""):
    for x in data:
        cityName = brain.getCity(x[0], x[1])
        print(cityName)
        gasPrice = getGasPrices(x[0], x[1], 1)[0]
        print(gasPrice)
        link = link + "&waypoints=" + str(x[0]) + "," + str(x[1])
        print(link)
        y = (cityName, gasPrice, link)
        db.append(y)



#opens a developmental server when play button is run
#make sure all code goes above these lines

if __name__ == "__main__":
    app.run(debug=True)
