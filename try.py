import json
import os

def display_menu():
    """Display the main menu"""
    print("\nPersonal Library Manager")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book(library):
    """Add a new book to the library"""
    print("\nAdd a New Book")
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    
    # Validate publication year
    while True:
        try:
            year = int(input("Enter the publication year: "))
            if year < 0 or year > 2025:  # Assuming we're not accepting future years beyond 2025
                print("Please enter a valid year.")
                continue
            break
        except ValueError:
            print("Please enter a valid year number.")
    
    genre = input("Enter the genre: ").strip()
    
    # Validate read status
    while True:
        read_status = input("Have you read this book? (yes/no): ").lower().strip()
        if read_status in ['yes', 'y']:
            read = True
            break
        elif read_status in ['no', 'n']:
            read = False
            break
        else:
            print("Please enter 'yes' or 'no'.")
    
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    
    library.append(book)
    print(f"Book '{title}' added successfully!")
    return library

def remove_book(library):
    """Remove a book from the library"""
    if not library:
        print("Your library is empty!")
        return library
    
    print("\nRemove a Book")
    title = input("Enter the title of the book to remove: ").strip()
    
    found_books = [book for book in library if book['title'].lower() == title.lower()]
    
    if not found_books:
        print(f"No book with title '{title}' found.")
        return library
    
    if len(found_books) > 1:
        print(f"Multiple books found with title '{title}':")
        for i, book in enumerate(found_books, 1):
            print(f"{i}. {book['author']} ({book['year']}) - {'Read' if book['read'] else 'Unread'}")
        
        while True:
            try:
                choice = int(input("Enter the number of the book to remove: "))
                if 1 <= choice <= len(found_books):
                    book_to_remove = found_books[choice-1]
                    library.remove(book_to_remove)
                    print(f"Book '{title}' removed successfully!")
                    return library
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    else:
        library.remove(found_books[0])
        print(f"Book '{title}' removed successfully!")
        return library

def search_books(library):
    """Search for books by title or author"""
    if not library:
        print("Your library is empty!")
        return
    
    print("\nSearch for a Book")
    print("1. Search by title")
    print("2. Search by author")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-2): "))
            if choice not in [1, 2]:
                print("Please enter 1 or 2.")
                continue
            break
        except ValueError:
            print("Please enter a number.")
    
    search_term = input("Enter the search term: ").strip().lower()
    results = []
    
    if choice == 1:
        results = [book for book in library if search_term in book['title'].lower()]
    else:
        results = [book for book in library if search_term in book['author'].lower()]
    
    if not results:
        print("No matching books found.")
    else:
        print(f"\nFound {len(results)} matching book(s):")
        for i, book in enumerate(results, 1):
            status = "Read" if book['read'] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_all_books(library):
    """Display all books in the library"""
    if not library:
        print("Your library is empty!")
        return
    
    print("\nYour Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book['read'] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics(library):
    """Display library statistics"""
    if not library:
        print("Your library is empty!")
        return
    
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books) * 100
    
    print("\nLibrary Statistics:")
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

def save_library(library, filename='library.json'):
    """Save the library to a file"""
    try:
        with open(filename, 'w') as f:
            json.dump(library, f)
        print(f"Library saved to {filename}")
    except Exception as e:
        print(f"Error saving library: {e}")

def load_library(filename='library.json'):
    """Load the library from a file"""
    if not os.path.exists(filename):
        return []
    
    try:
        with open(filename, 'r') as f:
            library = json.load(f)
        print(f"Library loaded from {filename}")
        return library
    except Exception as e:
        print(f"Error loading library: {e}")
        return []

def main():
    """Main program function"""
    # Load library from file if it exists
    library = load_library()
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Please enter a number between 1 and 6.")
            continue
        
        if choice == 1:
            library = add_book(library)
        elif choice == 2:
            library = remove_book(library)
        elif choice == 3:
            search_books(library)
        elif choice == 4:
            display_all_books(library)
        elif choice == 5:
            display_statistics(library)
        elif choice == 6:
            save_library(library)
            print("Thanks for visit my library Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()