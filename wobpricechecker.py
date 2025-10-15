# from urllib.request import urlopen
# import re

class Book:
    def __init__(self, name, url, price):
        self.name = name
        self.url = url
        self.price = price

SAO9 = Book("SAO9", 'https://www.worldofbooks.com/en-gb/products/sword-art-online-9-book-reki-kawahara-9780316390422', 0)

# def extract_data(url):
#     page = urlopen(url)
#     html_bytes = page.read()
#     html = html_bytes.decode("utf-8")
#     start_index = html.find('<span class="price_item')
#     end_index = html.find('<div id="rrp-container')
#     page_body = html[start_index:end_index]
#     print(page_body)

# extract_data(url)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get(SAO9.url)

try:
    SAO9.price = driver.find_element(By.CLASS_NAME, "price-item").text
except:
    SAO9.price = "Price not found"

print(f'{SAO9.name} Price: {SAO9.price}')

driver.quit()