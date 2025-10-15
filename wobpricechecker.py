from urllib.request import urlopen
import re

url = 'https://www.worldofbooks.com/en-gb/products/sword-art-online-9-book-reki-kawahara-9780316390422'

def extract_data(url):
    page = urlopen(url)
    print(page)

extract_data(url)