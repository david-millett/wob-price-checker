from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

class Book:
    def __init__(self, name, url, price):
        self.name = name
        self.url = url
        self.price = price

SAO9 = Book("SAO9", 'https://www.worldofbooks.com/en-gb/products/sword-art-online-9-book-reki-kawahara-9780316390422', 0)

def get_price(book):
    driver.get(book.url)
    try:
        book.price = driver.find_element(By.CLASS_NAME, "price-item").text
    except:
        book.price = "Price not found"
    print(f'{book.name} Price: {book.price}')
    driver.quit()

get_price(SAO9)