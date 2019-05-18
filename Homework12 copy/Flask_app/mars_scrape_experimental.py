def scrape_info():
    import requests

    from bs4 import BeautifulSoup

    import pandas as pd

#NASA Mars News¶

    page = requests.get("https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest")
    soup = BeautifulSoup(page.content, 'html.parser')
    articles = soup.find(class_="image_and_description_container")
    first_article = articles
    data = first_article.prettify()
    print(data)

    news_paragraph = first_article.find(class_="rollover_description_inner").get_text()
    print(news_paragraph)

    imgs = first_article.find_all("img")

    img = imgs[1]  
    news_title = img["alt"]
    news_title

    news_paragraph

    news_title

## JPL Mars Space Images - Featured Image

    from splinter import Browser

#!which chromedriver

    from splinter import Browser
    browser = Browser('chrome')

    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

    marshtml = browser.html
    soup = BeautifulSoup(marshtml, 'html.parser')

    backgroundhtml = soup.findAll('div', attrs={'class' : 'carousel_items'})
    backgroundhtml

    for item in backgroundhtml:
        imagedirect = item.article['style']
        print(imagedirect)

    urlsecondhalf = imagedirect.split('(')[1].split(')')[0].split("'")[1]
    urlfirsthalf = "https://www.jpl.nasa.gov"
    featuredimageurl = urlfirsthalf + urlsecondhalf
    featuredimageurl

    featuredimageurl

    browser.quit()


    ## Mars Weather

    page2 = requests.get("https://twitter.com/marswxreport?lang=en")
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    tweets = soup2.find(class_="js-tweet-text-container")
    first_tweet = tweets
    data2 = first_tweet.prettify()
    print(data2)


    mars_weather = first_tweet.find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()
    #period = tonight.find(class_="period-name").get_text()
    print(mars_weather)

    mars_weather

## Mars Facts

    page3 = requests.get("https://space-facts.com/mars/")
    soup3 = BeautifulSoup(page3.content, 'html.parser')
    table = soup3.find(id="tablepress-mars")
    data3 = table.prettify()
    print(data3)

    data = []
    table = soup3.find('table', attrs={'class':'tablepress tablepress-id-mars'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values


    data


    df = pd.DataFrame(data)
    df

    import pandas as pd
    import requests
    import numpy as np

    from bs4 import BeautifulSoup

    site = requests.get("https://space-facts.com/mars/")
    soup = BeautifulSoup(site.content,'html')
    table = soup.find_all('table')[0] 
    #df = pd.read_html(str(table))
    table_rows = table.find_all('tr')
    table_rows
    res = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text.strip() for tr in td if tr.text.strip()]
        if row:
            res.append(row)


    df = pd.DataFrame(res, columns=["Category", "Measurement"])
    print(df)


    dfhtmltablestring = df.to_html()
    dfhtmltablestring

    dfhtmltablestring

    ## Mars Hemispheres

    from splinter import Browser
    browser = Browser('chrome')
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


    browser.visit(url)
    # Iterate through all pages
    h3list = []
    #for x in range(4):
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
    hemispheres = soup.find_all('div', class_='description')

    # Iterate through each book
    for item in hemispheres:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        h3 = item.find('h3')
        h3list.append(h3)
    #print(h3)

    h3list

    item = str(h3list[2])
    item.split(">")[1].split("<")[0].split(" ")
    #item.split(">")[1].split("<")[0].split(" ")[-1]
    item.split(">")[1].split(" E")[0]

    titlelist = []
    for item in h3list:
        titlelist.append(str(item).split(">")[1].split(" E")[0])
    titlelist

    browser.quit()


    from splinter import Browser
    browser = Browser('chrome')
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    

    browser.visit(url)

    urllist = []

    for x in range(5):
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain book information
        hemispherehtml = soup.find_all('div', class_='downloads')

        # Iterate through each book
        for item in hemispherehtml:
            # Use Beautiful Soup's find() method to navigate and retrieve attributes
            li = item.find('li')
            link = li.find('a')
            href = link['href']
            #title = link['title']
        
            urllist.append(href)
        
            print('-----------')
            #print(href)
            #print('http://books.toscrape.com/' + href)

        # Click the 'Next' button on each page
        try:
            browser.click_link_by_partial_text(f'{titlelist[x]}')
            print("success")
          
        except:
            print("fail")

    
    titlelist

    urllist

    marsdatadict = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featuredimageurl,
        "current_weather": mars_weather,
        "facts_table": data3,
        "Cerberus": {
            "title": titlelist[0],
            "img_url": urllist[0]
        },
        "Schiaparelli": {
            "title": titlelist[1],
            "img_url": urllist[1]
        },
        "Syrtis": {
            "title": titlelist[2],
            "img_url": urllist[2]
        },
        "Valles": {
            "title": titlelist[3],
            "img_url": urllist[3]
        }
    }

    print(marsdatadict["Schiaparelli"]["img_url"])

    browser.quit()
    
    return marsdatadict