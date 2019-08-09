# Web-Scraping-and-Document-Databases-for-Mars

The purpose of this project was to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The initial scraping used a Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

Items on the HTML page include NASA Mars news, a featured Mars Space Image, the state of mars weather from the Mars Weather twitter account, Mars facts scraped from another webpage, and a dictionary of high resolution image urls scraped from the USGS Astrogeology site.

Finally, this project uses MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
