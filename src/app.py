import os 
from flask import Flask as onlyfans
your_mom = __name__

app = onlyfans(your_mom)

@app.route('/')
def hello_world():
    return "<p>Hello World</p>"


#opens a developmental server when play button is run
def runApp():
    os.system("flask --app ./src/app.py run")

if __name__ == "__main__":
    runApp()