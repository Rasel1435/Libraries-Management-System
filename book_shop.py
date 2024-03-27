import json
import logging

logging.basicConfig(filename='library.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Library:
    def __init__(self):
        self.books = []

    # Loading File From Here
    def load_books(self):
        try:
            with open('books.json', 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            logging.warning('No book data found.')
            self.books = []

    # Save File From Here
    def save_books(self):
        with open('books.json', 'w') as file:
            json.dump(self.books, file, indent=4)

    # Add Book to the Libraries
    def add_book(self):
        while True:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book_id = int(input("Enter book ID: "))
            published_year = input("Enter published year: ")
            book = {'title': title, 'author': author, 'id': book_id, 'published_year': published_year}
            
            self.books.append(book)
            logging.info(f"Added book: {book['title']} by {book['author']}")
            
            more = input("Do you want to add more books? (y/n): ")
            if more.lower() != 'yes':
                self.save_books()
                break

    # Updated Book 
    def update_book(self):
        book_id = int(input("Enter book ID to update: "))
        title = input("Enter new book title: ")
        author = input("Enter new book author: ")
        new_id = input("Enter new book ID: ")
        published_year = input("Enter new published year: ")
        new_book = {'title': title, 'author': author, 'id': new_id, 'published_year': published_year}
        try:
            self.books[book_id] = new_book
            logging.info(f"Updated book: {new_book['title']} by {new_book['author']}")
            self.save_books()
        except IndexError:
            logging.error(f"Book with ID {book_id} not found.")

    # Delete The Book
    def delete_book(self):
        book_id = int(input("Enter book ID to delete: "))
        try:
            deleted_book = self.books.pop(book_id)
            logging.info(f"Deleted book: {deleted_book['title']} by {deleted_book['author']}")
            self.save_books()
        except IndexError:
            logging.error(f"Book with ID {book_id} not found.")

    # Display All The Item
    def display_books(self):
        if not self.books:
            print("No books available.")
            logging.warning("No books available.")
        else:
            print("Available books:")
            for i, book in enumerate(self.books):
                print(f"{i}: {book['title']} by {book['author']}, ID: {book['id']}, Published Year: {book['published_year']}")

    # lend Book 
    def lend_book(self):
        book_id = int(input("Enter book ID to lend: "))
        user = input("Enter user name: ")
        try:
            lent_book = self.books.pop(book_id)
            logging.info(f"Lent book: {lent_book['title']} by {lent_book['author']} to {user}")
            self.save_books()
        except IndexError:
            logging.error(f"Book with ID {book_id} not found.")

    # Return book 
    def return_book(self):
        title = input("Enter book title to return: ")
        author = input("Enter book author to return: ")
        book_id = input("Enter book ID to return: ")
        published_year = input("Enter published year of the book: ")
        book = {'title': title, 'author': author, 'id': book_id, 'published_year': published_year}
        self.books.append(book)
        logging.info(f"Returned book: {book['title']} by {book['author']}")
        self.save_books()


# class and all def will call from here
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
