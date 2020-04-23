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
	article_news = soup.find_all('p', class_='gnt_ar_b_p')

    #Combine all of the paragraph tag text into a single var with a newline seperator.
	for p in article_news:
		articletext = articletext + p.get_text() + '\n'

    #Output the text to a file in the scrapes folder.
	with open("scrapes/"+filename+".txt", "w") as text_file:
	    text_file.write(articletext)






# Set the URL's you want to webscrape content from as a list.
#Example format Title | Url
url_list = []
url_list.append("Locust | https://www.usatoday.com/story/news/world/2020/04/11/east-africa-kenya-locust-plague-cant-fought-amid-coronavirus/2975544001/")
url_list.append("Wisconsin | https://www.usatoday.com/story/news/politics/2020/04/13/wisconsin-supreme-court-election-results-daniel-kelly-vs-jill-karofsky-conservative-liberal/2986880001/")
url_list.append("Left-Out | https://www.usatoday.com/story/news/politics/2020/04/10/coronavirus-who-doesnt-get-stimulus-check-millions-people-left-out/5112027002/")
url_list.append("Joshua-Tree | https://www.usatoday.com/story/news/nation/2020/04/13/joshua-tree-nursing-home-coronavirus-endangered-california/2982922001/")
url_list.append("Michigan-Protests | https://www.usatoday.com/story/news/nation/2020/04/13/coronavirus-michigan-protest-gretchen-whitmer-lansing/2986535001/")



for u in url_list:
	name = str(u.split('|')[0])
	url = str(u.split('|')[1])
	scrape_articles(url,name.strip())