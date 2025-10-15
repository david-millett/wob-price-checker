from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Book class
class Book:
    def __init__(self, name, url, price):
        self.name = name
        self.url = url
        self.price = price

# Books
books = [
    Book("SAO9", 'https://www.worldofbooks.com/en-gb/products/sword-art-online-9-book-reki-kawahara-9780316390422', 0),
    Book("SAO11", 'https://www.worldofbooks.com/en-gb/products/sword-art-online-11-book-reki-kawahara-9780316390446', 0),
]

# Setup Chrome
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(0.5)

# Function to fetch price
def get_price(book):
    driver.get(book.url)
    try:
        book.price = driver.find_element(By.CLASS_NAME, "price-item").text
    except:
        book.price = "Price not found"
    print(f'{book.name} Price: {book.price}')

# Run
for book in books:
    get_price(book)

driver.quit()