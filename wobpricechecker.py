# from urllib.request import urlopen
# import re

url = 'https://www.worldofbooks.com/en-gb/products/sword-art-online-9-book-reki-kawahara-9780316390422'

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

driver = webdriver.Chrome()

driver.get(url)

price = driver.find_element(By.CLASS_NAME, "price-item").text
print(price)

driver.quit()