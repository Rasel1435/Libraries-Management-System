# Libraries-Management-System

# Summary:

I've developed a simple Library Management System using Python. Here's an overview of its functionality:

1. **Library Class**: 
    - It manages the operations related to books such as adding, updating, deleting, displaying, lending, and returning books.
    - It loads and saves book data from/to a JSON file.

2. **Functionality**:
    - **Add Book**: Allows users to add new books to the library inventory.
    - **Update Book**: Enables users to update information about existing books based on their ID.
    - **Delete Book**: Allows users to remove a book from the library using its ID.
    - **Display Available Books**: Displays all available books in the library.
    - **Lend Book**: Facilitates lending a book to a user by removing it from the library inventory.
    - **Return Book**: Allows users to return a previously borrowed book, adding it back to the library inventory.

3. **Logging**:
    - Utilizes Python's logging module to log important events such as adding, updating, deleting, lending, and returning books. Logs are stored in a file named 'library.log'.

4. **User Interface**:
    - Provides a simple command-line interface for users to interact with the library system.
    - Users can input numeric choices to perform various operations.

5. **Main Function**:
    - Initializes the Library class, loads existing book data, and starts a loop to prompt users for actions until they choose to exit.

This system provides basic functionality for managing a library's book inventory efficiently. It can be expanded with additional features such as user authentication, searching books, or categorizing books based on genres. Overall, it demonstrates fundamental principles of object-oriented programming, file handling, and user interaction in Python.


### I have created requrements.txt file by
    pip freeze > requirements.txt
