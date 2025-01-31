from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all(name = 'span', class_='titleline')

# article_texts = []
# article_links= []
#
# for article_tag in articles:
#     text = articles.getText()
# links = articles.find('a').get('href')


article_titles = [title.getText() for title in articles]
article_links = [link.find('a').get('href') for link in articles]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

print (article_titles)
print(article_links)
print(article_upvotes)

top_score = max(article_upvotes)
largest_index = article_upvotes.index(top_score)

top_article = article_titles[largest_index]
top_article_link = article_links[largest_index]
print(top_article + top_article_link)

## import lxml ##if html parser isnt working

# with open("website.html") as file: ## Open HTML file
#     soup = BeautifulSoup(file, 'html.parser') ## Parse HTML file
#
# print (soup.prettify()) ## print soup
#
# all_anchor_tags = soup.find_all(name='a') ## find all anchor tags
# print(all_anchor_tags) ##print anchor tags
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
#
# heading = soup.find(name='h1', id='name')
# print(heading)
#
# section_heading = soup.find(name='h3', class_ = 'heading')
# print(section_heading.get('class'))
#
# company_url = soup.select_one(selector='p a')
# print(company_url)
#
# headings = soup.select('.heading')
# print(headings)