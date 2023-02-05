import os 
from flask import Flask as onlyfans
from flask import render_template, request  
from dotenv import load_dotenv
from directionsv2 import directions

load_dotenv()
GKEY = os.getenv("GOOGLE")
RKEY = os.getenv("RAPID")

your_mom = __name__

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
            #brain.updateVar(mpg, tank)
            start = brain.geocoding(start)
            end = brain.geocoding(end)
            route = brain.detailedDistances(start, end)
            display = brain.doMeth(route)
        except:
            print("exception")
    return render_template("map.html", url=brain.makeUrl(display))


#opens a developmental server when play button is run
#make sure all code goes above these lines

if __name__ == "__main__":
    app.run(debug=True)