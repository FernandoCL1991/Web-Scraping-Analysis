from flask import Flask, render_template, rediret
from flask_pymongo import PyMongo
import scrape_mars

# Flask
app = Flask(__name__)



# MONGO HERE! ######## REVISAR!


########## REVISAR! USAR MONGO !!




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


    