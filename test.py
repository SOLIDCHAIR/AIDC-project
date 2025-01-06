import mechanicalsoup
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re 
brower = mechanicalsoup.Browser()

url = "https://edhrec.com/commanders/urza-lord-high-artificer"
page = brower.get(url)
soup = page.soup

cards = soup.find_all("span")
for card in cards :
    Str = card.find("strong",string='Str')
    if Str is not None:
        Str_text = Str.text
        # here is the value of Str
        value = Str.next_sibling
        print(value)

print(cards)