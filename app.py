#################### DEPENDENCIES #####################
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pandas as pd

##################### MONGO SETUP #####################
# Importing pymongo
import pymongo
# Flask
app = Flask(__name__)
# Creating connection variable to local host
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
# Creating DB
db = client.mars_website_db
# Creating collection inside the DB
all_hemispheres_dict= db.all_hemispheres_dict



################### CREATING ROUTES ####################

## Home route
@app.route("/")
def index():
    try:
        # Find one record of data from mongo database , JSON
        mars_data = db.mars.data.find_one()
        # Find one record of data from mongo database , HTML
        table = pd.DataFrame(mars_data["mars_facts"])
        # Return rendered list of dictionaries
        return render_template("index.html", mars_data=mars_data, mars_table=table.to_html())
    except:
        return render_template("index.html", mars_data={}, mars_table="")


## Scrape route
@app.route("/scrape")
def scrape():
    # Running the scrape function and passing results as a variable
    hemispheres_data=scrape_mars.scrape()
    # upsert=True if info is updated
    db.mars.data.update({}, hemispheres_data, upsert= True)
    # Redirecting back to home page
    return redirect ("/")


if __name__ == "__main__":
    app.run()


    