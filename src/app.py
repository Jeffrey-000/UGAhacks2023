import os 
from flask import Flask as onlyfans
from flask import render_template, request  
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("GOOGLE")

your_mom = __name__

app = onlyfans(your_mom)

googlemapsurl = "https://www.google.com/maps/embed/v1/place?key=" + KEY + "&q=Space+Needle,Seattle+WA"

@app.route('/')
def home():
    return render_template("map.html", url=googlemapsurl)

@app.route('/', methods=['POST', 'GET'])
def calc(start=None, end=None):
    if request.method == "POST":
        start = request.form['start']
        end = request.form['end']
    return render_template("map.html", url=googlemapsurl,start=start, end=end)


#opens a developmental server when play button is run
#make sure all code goes above these lines
def runApp():
    os.system("flask --app ./src/app.py run")

if __name__ == "__main__":
    app.run(debug=True)