
import requests
from bs4 import BeautifulSoup

page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
quotes = soup.find_all("span", attrs={"class":"text"})
authors = soup.find_all("small", attrs={"class":"author"})

#for quote in quotes: 
    #print(quote.get_text)
#for author in authors:
    #print(author.get_text)

#for quote, author in zip(quotes, authors):
    #print(quote.text + " - " + author.text)

file = open ("scraped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])
file.close 
