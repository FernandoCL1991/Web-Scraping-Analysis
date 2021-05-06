#!/usr/bin/env python
# coding: utf-8

# Base Code

# In[1]:


# Importing Dependencies

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


# Splinter setup

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless = False)


# NASA Mars News

# In[3]:


# Defining a function to the result of the scrape: news_title

def news_title(browser):
    
    # Passing url for 'news_title' function
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Scrapping with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    # Retrieving elements
    article = soup.find('div', class_='list_text') 
    # Creating 'title' variable
    title = article.find('div', class_= 'content_title').text

    # Closing function difining: news_title
    return title

# Defining a function to the result of the scrape: news_p

def news_p(browser):
    
    # Passing url for 'news_p' function
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Scrapping with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    # Retrieving elements
    article = soup.find('div', class_='list_text') 
    # Creating 'paragraph' variable
    paragraph = article.find('div', class_= 'article_teaser_body').text 

    # Closing function difining: news_p
    return paragraph


# In[6]:


news_p(browser)


# JPL Mars Space Images

# In[7]:


# Defining a function to the result of the scrape: current_img_url

def current_img_url(browser):

    # Passing url for 'current_img_url' function
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # Scrapping with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html,'html.parser') 

    # Retrieving elements
    article = soup.find('div', class_='header')
    # Creating 'image_url' variable
    image_url = article.find('img', class_= 'headerimage fade-in').get('src')

    # Creating final url variable
    featured_image_url = f'https://spaceimages-mars.com/{image_url}'

    # Closing function difining: current_img_url
    return featured_image_url


# In[8]:


current_img_url(browser)


# Mars Facts

# In[9]:


# Defining a function to the result of the scrape: mars_facts

def mars_facts(browser):

    # Passing url for 'mars_facts_df'
    url = 'https://galaxyfacts-mars.com/'

    # Retrieving elements into 'tables'
    tables = pd.read_html(url)
    # Selecting desired table. Creating 'mars_facts_df' variable
    mars_facts_df = tables[0]
    mars_facts_df_cols = ['Mars-Earth Comparisson', 'Mars', 'Earth']
    mars_facts_df.columns = mars_facts_df_cols
    mars_facts_df.drop(labels=[0], axis= 0, inplace=True)
    mars_facts_dict = mars_facts_df.to_dict(orient='record')

    # Closing function difining: mars_facts
    return mars_facts_df


# In[10]:


mars_facts(browser)


# Mars Hemispheres

# In[11]:


# Defining a function to the result of the scrape: all_hemispheres_data

def all_hemispheres_data(browser):
    
    # Passing url for 'hemisphere_image_urls'
    url = 'https://marshemispheres.com'
    browser.visit(url)

    # Scrapping with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    # Total number of hemispheres pages to visit to
    links= browser.find_by_css('a.product-item img')

    # Creating a list w/ 4 dictionaries with title and link to image per hemisphere w/ Splinter
    hemisphere_image_urls  = []

    for i in range(len(links)):

        # creating dictionary
        hemispheres_dict = {}

        # first page, click to second
        browser.find_by_css('a.product-item img')[i].click()

        # on second page, retrieving title   
        title= browser.find_by_css('h2').text
        hemispheres_dict['title']= title

        # on second page, retrieving url
        img_url= browser.links.find_by_text('Sample').first['href']
        hemispheres_dict['img_url']= img_url

        # appending both results to list 'empty_list'
        hemisphere_image_urls.append(hemispheres_dict)

        # browse back to home page
        browser.back()        
            
    # Closing function difining: all_hemispheres_data
    return hemisphere_image_urls


# In[12]:


all_hemispheres_data(browser)


# In[13]:


# Defining a function to the result of the scrape: scrape

def scrape(browser):
    
    data={
        "news_title": news_title(browser),
        "news_p": news_p(browser),
        "current_img_url" : current_img_url(browser),
        "mars_facts" : mars_facts(browser),
        "all_hemispheres_data" : all_hemispheres_data(browser)
    }

    return data


# In[14]:


scrape(browser)


# In[15]:


browser.quit()

