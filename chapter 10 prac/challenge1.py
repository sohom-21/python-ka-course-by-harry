class Book:
         def __init__(self,title,author,price):
                  self.title = title
                  self.author = author
                  self.price = price

book1 = Book('good long drives', "Joe Samuel", 799)
book2 = Book('All along the sea shore', "Jenna Parker", 999)

print(book1.title,book1.price)
print(book2.title,book2.author,book2.price)