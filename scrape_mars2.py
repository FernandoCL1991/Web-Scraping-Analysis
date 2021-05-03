#################### DEPENDENCIES ####################
from flask import Flask, render_template
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

#################### SCRAPING JUPYTER NOTEBOOK ####################



def scrape():
    my_dictionary = {}
    my_dictionary['hemisphere_url'] = get_hemipshere_url()
    my_dictionary['mars_facts'] =mars_facts()

 return my_dictionary



# Working with Jupyter notebook with scrape function
def scrape():

    # Splinter setup

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless = False)


    # In[3]:


    # Passing url

    url = 'https://redplanetscience.com/'
    browser.visit(url)


    # In[4]:


    # Scrapping with Beautiful Soup

    html = browser.html
    soup = BeautifulSoup(html,'html.parser')


    # In[5]:


    # Retrieving text into variables

    # Retrieving elements
    article = soup.find('div', class_='list_text') 
    # Creating 'news_title' variable
    news_title = article.find('div', class_= 'content_title').text 
    # Creating 'news_p' variable
    news_p = article.find('div', class_= 'article_teaser_body').text 

    print(f'The news title is: {news_title}')
    print(f'The news title is: {news_p}')


    # JPL Mars Space Images Web Scraping

    # In[6]:


    # Passing url

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)


    # In[7]:


    # Scrapping with Beautiful Soup

    # Passing in the HTML
    html = browser.html
    # Parsing HTML with BS
    soup = BeautifulSoup(html,'html.parser') 


    # In[8]:


    # Retrieving info into variable

    # Retrieving elements
    article = soup.find('div', class_='header')
    # Creating 'image_url' variable
    image_url = article.find('img', class_= 'headerimage fade-in').get('src')


    # In[9]:


    # Creating 'image_url' variable

    featured_image_url = f'https://spaceimages-mars.com/{image_url}'
    featured_image_url


    # Mars Facts

    # In[10]:


    # Importing Dependencies

    import pandas as pd


    # In[11]:


    # Passing url

    url = 'https://galaxyfacts-mars.com/'


    # In[12]:


    # Retrieving info into tables variable

    tables = pd.read_html(url)
    tables


    # In[13]:


    # Printing dataframe 

    df = tables[0]
    df.head()


    # Mars Hemispheres

    # In[14]:


    # Passing url

    url = 'https://marshemispheres.com'
    browser.visit(url)


    # In[15]:


    # Scrapping with Beautiful Soup

    # Passing in the HTML
    html = browser.html
    # Parsing HTML with BS
    soup = BeautifulSoup(html,'html.parser') 


    # In[16]:


    # Printing total number of hemispheres pages

    links= browser.find_by_css('a.product-item img')
    len(links)


    # In[17]:


    # Creating a list w/ 4 dictionaries with title and link to image per hemisphere w/ Splinter

    browser.visit(url)

    links= browser.find_by_css('a.product-item img')
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
        hemisphere_image_urls .append(hemispheres_dict)
        
        # browse back to home page
        browser.back()


        # In[18]:


        print(hemisphere_image_urls)


        # In[19]:


        browser.quit()

        return(hemisphere_image_urls)

    

if __name__ == "__main__":
    print(scrape())
    

