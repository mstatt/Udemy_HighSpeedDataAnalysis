# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def scrape_articles(url,filename):
	articletext = ''
	# Connect to the URL
	response = requests.get(url)

	# Parse HTML and save to BeautifulSoup object¶
	soup = BeautifulSoup(response.text, "html.parser")
	#********VERY IMPORTANT TO MATCH WITH THE SITE YOU ARE SCRAPING**************
	article_news = soup.find_all('p')

    #Combine all of the paragraph tag text into a single var with a newline seperator.
	for p in article_news:
		articletext = articletext + p.get_text() + '\n'

    #Output the text to a file in the scrapes folder.
	with open("scrapes/"+filename+".txt", "w") as text_file:
	    text_file.write(articletext)






# Set the URL's you want to webscrape content from as a list.
#Example format Title | Url
url_list = []
url_list.append("TensorFlow | https://www.udemy.com/course/deep-learning-tensorflow-2/")
url_list.append("Time_Series | https://www.udemy.com/course/python-for-time-series-data-analysis/")
url_list.append("Data_Science | https://www.udemy.com/course/the-data-science-course-complete-data-science-bootcamp/")



for u in url_list:
	name = str(u.split('|')[0])
	url = str(u.split('|')[1])
	scrape_articles(url,name.strip())