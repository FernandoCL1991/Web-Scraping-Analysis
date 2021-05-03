from flask import Flask, render_template, rediret
from flask_pymongo import PyMongo
import scrape_mars

# Flask
app = Flask(__name__)




#################### MONGO SETUP ####################
# Importing pymongo
import pymongo
# Creating connection to local host
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
# Creating DB
db = client.mars_website_db
# Creating collection inside the DB
all_hemispheres_dict= db.all_hemispheres_dict
#######################################################BORRAR EL DROP ANTES DE SUBIR
mongo.db.collection.drop()
####





## Home route
@app.route("/")
def index():
    # Find one record of data from mongo database
    hemisphere_image_urls = mongo.db.collection.find_one()
    # Return rendered list of dictionaries
    return render_template("index.html", hemispheres=hemisphere_image_urls)


## Scrape route
@app.route("/scrape")
def scrape():
    # Running the scrape function and passing results as a variable
    hemisphere_image_urls=scrape_mars.scrape_info()

    # upsert=True if info is updated
    mongo.db.collection.update({}, hemispheres_data, upsert= True)

    # Redirecting back to home page
    return redirect ("/")





############ USE THIS????
    #hemispheres = mongo.db.hemispheres
    #hemispheres_data = scrape_mars.scrape()
    
    #return redirect("/", code=302)


if __name__ == "__main__":
    app.run()


    