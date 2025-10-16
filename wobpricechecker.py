from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Import books
from books import books

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