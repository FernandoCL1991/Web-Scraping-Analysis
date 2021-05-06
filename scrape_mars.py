#################### JUPYTER NOTEBOOK ####################

#!/usr/bin/env python
# coding: utf-8

# Base Code

# In[1]:


# Importing Dependencies

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def mars_news(browser):
   # Scrape Mars News
   # Visit the mars nasa news site
   url = 'https://mars.nasa.gov/news/'
   browser.visit(url)
   # Optional delay for loading the page
   browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
   # Convert the browser html to a soup object and then quit the browser
   html = browser.html
   news_soup = soup(html, 'html.parser')
   # Add try/except for error handling
   try:
       slide_elem = news_soup.select_one("ul.item_list li.slide")
       # Use the parent element to find the first 'a' tag and save it as 'news_title'
       news_title = slide_elem.find("div", class_="content_title").get_text()
       # Use the parent element to find the paragraph text
       news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
   except AttributeError:
       return None, None
   return news_title, news_p

# Defining a function to the result of the scrape: current_img_url


def current_img_url(browser):

    # Passing url for 'current_img_url' function
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # Scrapping with Beautiful Soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Retrieving elements
    article = img_soup.find('div', class_='header')
    # Creating 'image_url' variable
    image_url = article.find('img', class_='headerimage fade-in').get('src')

    # Creating final url variable
    featured_image_url = f'https://spaceimages-mars.com/{image_url}'

    # Closing function difining: current_img_url
    return featured_image_url

# Defining a function to the result of the scrape: mars_facts

def mars_facts(browser):

    # Passing url for 'mars_facts_df'
    url = 'https://galaxyfacts-mars.com/'

    # Retrieving elements into 'tables'
    tables = pd.read_html(url)

    try:
        # Selecting desired table. Creating 'mars_facts_df' variable
        mars_facts_df = tables[0]
        mars_facts_df_cols = ['Mars-Earth Comparisson', 'Mars', 'Earth']
        mars_facts_df.columns = mars_facts_df_cols
        mars_facts_df.drop(labels=[0], axis=0, inplace=True)
        mars_facts_dict= mars_facts_df.to_dict(orient = 'record')

    except:
        return mars_facts_dict == None

    else:
        return mars_facts_dict

    # Closing function difining: mars_facts
    return mars_facts_dict

# Defining a function to the result of the scrape: all_hemispheres_data


def hemispheres(browser):
   # A way to break up long strings
   url = (
       "https://astrogeology.usgs.gov/search/"
       "results?q=hemisphere+enhanced&k1=target&v1=Mars"
   )
   browser.visit(url)
   # Click the link, find the sample anchor, return the href
   hemisphere_image_urls = []
   for i in range(4):
       # Find the elements on each loop to avoid a stale element exception
       browser.find_by_css("a.product-item h3")[i].click()
       hemi_data = scrape_hemisphere(browser.html)
       # Append hemisphere object to list
       hemisphere_image_urls.append(hemi_data)
       # Finally, we navigate backwards
       browser.back()
   return hemisphere_image_urls

def scrape_hemisphere(html_text):
    hemi_soup=soup(html_text,"html.parser")
    try:
        title_elem=hemi_soup.find("h2", class_="title").get_text()
        sample_elem=hemi_soup.find("a", text="Sample").get("href")
    except AttributeError:
        title_elem = None
        sample_elem = None
    hemispheres={
        "title":title_elem,
        "img_url":sample_elem
    }
    return hemispheres

# Defining a function to the result of the scrape: scrape


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    news_title,news_p=mars_news(browser)
    data = {
        "news_title": news_title,
        "news_p": news_p,
        "current_img_url": current_img_url(browser),
        "mars_facts": mars_facts(browser),
        "all_hemispheres_dict": hemispheres(browser)
    }

    return data



if __name__ == "__main__":
    print(scrape())
