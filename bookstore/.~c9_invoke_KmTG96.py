class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def get_books(self):
      return self.books
      
    def add_book(self, book):
      self.books.append(book)
      return self.books
      
    def search_books(self, title=None, author=None):
        if title is None and author is None:
            return "You must construct additional Pylons"
        if title is not None and author is None:
            for book in self.books:
                return book.title
                    return book
        elif title is None and author is not None:
            book_list = []
            for book in author.authored_books:
                if book.author == author.:
                    book_list.append(book.title)
            return book_list
        elif title is not None and author is not None:
            for book in self.books:
                if book.author == author and book.title == title:
                    return book
        else:
            pass
            
        
    


class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.authored_books = []
        
    def get_books(self):
        return self.authored_books
        
    def get_author_name(self):
        return self.name
        
    def add_to_author_list(self, title):
        return self.authored_books.append(title)
        

class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author.name
        author.add_to_author_list(title)
        
        