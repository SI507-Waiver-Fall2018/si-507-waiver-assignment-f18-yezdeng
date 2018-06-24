# Name: Yezhi Deng 
# Uniq: yezdeng
# UMID 43578445

#############

# these should be the only imports you need
import requests
from bs4 import BeautifulSoup

# the url of Michigan Daily site
base_url = "https://www.michigandaily.com/"

# get HTML page content using request
page_content = requests.get(base_url).text

# parse the page into BeautifulSoup format
soup = BeautifulSoup(page_content, 'html.parser')



### soup.ol --> get content with <ol> tag, which is the most read article title
### soup.ol.content --> store all content with <ol> tag in a list
### i.string --> extract the text from ol, which is the most read article title

### define two lists to store urls and article titles
most_read_url = []
most_read_name = []

j = 0 
for i in soup.ol.contents:
	j += 1
	## if i have ['href'] attribute, append i.string to most_read_name list
	## and base_url + i.a['href'] is the url linking to the article page
	# delete void item in the list
	if (j % 2 == 1 ):
		most_read_name.append(i.string.strip())
		most_read_url.append(base_url + i.a['href'])


# print(most_read_name)
# print(most_read_url)


### create a list to store article writer names
article_writer = []

### Request author data from the urls
for url in most_read_url:
	article_page_content = requests.get(url).text
	article_soup = BeautifulSoup(article_page_content, 'html.parser')

	# use class_="title" to find title element at first
	# then go to the previous sibling, which is the author name
	author = article_soup.find('div',class_="byline")

	# if there's author name in this page
	if (author != None):
		# find author string using .next_element
		author_string = author.next_element.next_element.next_element.string
		article_writer.append(author_string)
	else:
		article_writer.append("BY DAILY STAFF WRITER")

# print(article_writer)


### print the data we get
print("Michigan Daily -- MOST READ")

i = 0
while (i < len(article_writer)):
	print(most_read_name[i])
	print("   by " + article_writer[i])
	i = i + 1



