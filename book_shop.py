import json
import logging

logging.basicConfig(filename='library.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Book:
    def __init__(self, title, author, book_id, publication_year):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.publication_year = publication_year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ID: {self.book_id}, Publication Year: {self.publication_year}"

class Library:
    def __init__(self):
        self.books = []
        self.users = {}
        
    # Add a book to the library
    def add_book(self):
            try:
                logging.info("Adding a book")
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                book_id = input("Enter the ID of the book: ")
                publication_year = int(input("Enter the publication year of the book: "))
                
                new_book = Book(title, author, book_id, publication_year)
                self.books.append(new_book.__dict__)
                logging.info(f"Book '{title}' added successfully")
            except ValueError:
                logging.error("Invalid input")
        
    # Load The File
    def load_books(self):
        try:
            with open('books.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error("File Not Found")
        
    # Save the file
    def save_books(self):
        try:
            with open('books.json', 'w') as file:
                json.dump(self.books, file)
        except FileNotFoundError:
            logging.error("File Not Found")
            
    # Choose what you want to do
    def choose_option(self):
        print("1. Add Book")
        print("2. Search Book")
        print("3. Delete Book")
        print("4. Update Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.add_book()
        elif choice == '2':
            self.search_book()
        elif choice == '3':
            self.delete_book()
        elif choice == '4':
            self.update_book()
        elif choice == '5':
            exit()
        return choice

# All def function will be called from here
def main():
    library = Library()
    library.load_books()
    library.choose_option()
    library.save_books()
    
if __name__ == '__main__':
    main()
