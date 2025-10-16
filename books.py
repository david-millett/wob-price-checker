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