import json
import logging

logging.basicConfig(filename='library.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Library:
    def __init__(self):
        self.books = [] #storage 

    # Our Libraries Json File will be Load From here
    def load_books(self):
        try:
            with open('books.json', 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            logging.warning('No book data found.')
            self.books = []

    # Our Libraries Json File will be Save From here
    def save_books(self):
        with open('books.json', 'w') as file:
            json.dump(self.books, file, indent=4)

    # Our first step is add item or book let's create function for it
    # """ add_book Function Start """
    def add_book(self): 
        while True:
            title = input("Enter your book title: ")
            author = input("Enter your book author: ")
            book_id = input("Enter your book ID: ")
            published_year = input("Enter the book published year: ")
            book = {'title': title, 'author': author, 'id': book_id, 'published_year': published_year}
            
            self.books.append(book)
            logging.info(f"Added book: {book['title']} by {book['author']}")
            # if you want to add more at a time
            more = input("Do you want to add more books? If yes, then press '1' or '7' to exit: ")
            if more == '1':
                continue
            elif more == '7':
                self.save_books()
                break
            else:
                print("Invalid input. Please enter '1' to add more books or '7' to exit.")
    # """add_book Function End """
    
    # Our second step is Update item or book if there is any mistake in exiting book or item
    # """ Update_book Function Start """
    def update_book(self):
        book_id = input("Enter your book ID which you want to update: ")
        found = False
        for book in self.books:
            if book['id'] == book_id:
                try:
                    title = input("Enter your new book title: ")
                    author = input("Enter your new book author: ")
                    new_id = input("Enter your new book ID: ")
                    published_year = input("Enter the new book published year: ")
                    book.update({'title': title, 'author': author, 'id': new_id, 'published_year': published_year})
                    logging.info(f"Updated book: {book['title']} by {book['author']}")
                    found = True
                except Exception as e:
                    logging.error(f"Error updating book: {e}")
                break
        if not found:
            logging.error(f"Book with ID {book_id} are not found.")
        self.save_books()
    # """update_book Function End """
    
    # Our third step is delete item or book let's create function for it
    # """ delete_book Function Start """
    def delete_book(self):
        book_id = input("Enter your book ID which you want to delete: ")
        found = False
        for book in self.books:
            if book['id'] == book_id:
                try:
                    self.books.remove(book)
                    logging.info(f"Deleted book: {book['title']} by {book['author']}")
                    found = True
                except Exception as e:
                    logging.error(f"Error deleting book: {e}")
                break
        if not found:
            logging.error(f"Book with ID {book_id} not found.")
        self.save_books()
    # """ delete_book Function End """
    
    # Our fourth step is display item or book let's create function for it
    # """ display_book Function Start """
    def display_books(self):
        if book not in self.books:
            logging.warning("books are not available.")
        else:
            print("Available books in the Libraries:")
            for i, book in enumerate(self.books):
                print(f"{i}: {book['title']} by {book['author']}, ID: {book['id']}, Published Year: {book['published_year']}")
    # """ display_book Function Start """
    
    # Our fifth step is Lend item or book let's create function for it
    # """ lend_book Function Start """
    def lend_book(self):
        book_id = input("Enter book ID which you want to lend: ")
        found = False
        for book in self.books:
            if book['id'] == book_id:
                try:
                    user = input("Enter user name: ")
                    logging.info(f"Lent book: {book['title']} by {book['author']} to {user}")
                    self.books.remove(book)
                    found = True
                except Exception as e:
                    logging.error(f"Error lending book: {e}")
                break
        if not found:
            logging.error(f"Book with ID {book_id} not found.")
        self.save_books()
    # """ lend_book Function End """
    
    # Our sixth step is Return item or book let's create function for it
    # """ return_book Function Start """
    def return_book(self):
        title = input("Enter the book title to return: ")
        author = input("Enter the book author to return: ")
        book_id = input("Enter the book ID to return: ")
        published_year = input("Enter published year of the book: ")
        book = {'title': title, 'author': author, 'id': book_id, 'published_year': published_year}
        self.books.append(book)
        logging.info(f"Returned book: {book['title']} by {book['author']}")
        self.save_books()
    # """ return_book Function End """

# Class and all def will be call from here
def main():
    library = Library()
    library.load_books()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Display Available Books")
        print("5. Lend Book")
        print("6. Return Book")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            library.add_book()
        elif choice == '2':
            library.update_book()
        elif choice == '3':
            library.delete_book()
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            library.lend_book()
        elif choice == '6':
            library.return_book()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            

if __name__ == "__main__":
    main()
