import json
import os
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

# Define color scheme
COLORS = {
    'title': Fore.CYAN + Style.BRIGHT,
    'header': Fore.YELLOW + Style.BRIGHT,
    'success': Fore.GREEN + Style.BRIGHT,
    'error': Fore.RED + Style.BRIGHT,
    'warning': Fore.YELLOW,
    'info': Fore.BLUE,
    'menu': Fore.MAGENTA,
    'book': Fore.LIGHTGREEN_EX,
    'author': Fore.LIGHTBLUE_EX,
    'year': Fore.LIGHTCYAN_EX,
    'genre': Fore.LIGHTMAGENTA_EX,
    'read': Fore.LIGHTGREEN_EX,
    'unread': Fore.LIGHTRED_EX,
    'reset': Style.RESET_ALL
}

def display_banner():
    """Display a beautiful ASCII art banner"""
    print(COLORS['title'] + r"""
  ____               _          _       _     _                 __  __             _ _             
 |  _ \ ___  ___ ___(_)_ ______| | __ _| |__ | | ___    ___    |  \/  | ___  _ __ (_) |_ ___  _ __ 
 | |_) / _ \/ __/ __| | |______| |/ _` | '_ \| |/ _ \  / _ \   | |\/| |/ _ \| '_ \| | __/ _ \| '__|
 |  __/ (_) \__ \__ \ | |      | | (_| | |_) | |  __/ | (_) |  | |  | | (_) | | | | | || (_) | |   
 |_|   \___/|___/___/_|_|      |_|\__,_|_.__/|_|\___|  \___/   |_|  |_|\___/|_| |_|_|\__\___/|_|   
    """)
    print(COLORS['header'] + " " * 20 + "Manage Your Book Collection with Style!")
    print("\n")

def display_menu():
    """Display the colorful main menu"""
    print(COLORS['menu'] + "\n" + "═" * 50)
    print(COLORS['header'] + "📚 MAIN MENU".center(50))
    print(COLORS['menu'] + "═" * 50)
    print(COLORS['menu'] + "1. 📖 Add a book")
    print(COLORS['menu'] + "2. 🗑️ Remove a book")
    print(COLORS['menu'] + "3. 🔍 Search for a book")
    print(COLORS['menu'] + "4. 📚 Display all books")
    print(COLORS['menu'] + "5. 📊 Display statistics")
    print(COLORS['menu'] + "6. 🚪 Exit")
    print(COLORS['menu'] + "═" * 50)

def add_book(library):
    """Add a new book to the library with colorful prompts"""
    print(COLORS['header'] + "\n" + "📖 ADD A NEW BOOK".center(50, "─"))
    
    title = input(COLORS['book'] + "📝 Enter the book title: " + COLORS['reset']).strip()
    author = input(COLORS['author'] + "✍️ Enter the author: " + COLORS['reset']).strip()
    
    # Validate publication year
    while True:
        try:
            year = int(input(COLORS['year'] + "📅 Enter the publication year: " + COLORS['reset']))
            if year < 0 or year > 2025:
                print(COLORS['warning'] + "⚠️ Please enter a valid year (0-2025).")
                continue
            break
        except ValueError:
            print(COLORS['error'] + "❌ Please enter a valid year number.")
    
    genre = input(COLORS['genre'] + "🏷️ Enter the genre: " + COLORS['reset']).strip()
    
    # Validate read status
    while True:
        read_status = input(COLORS['info'] + "👓 Have you read this book? (yes/no): " + COLORS['reset']).lower().strip()
        if read_status in ['yes', 'y']:
            read = True
            break
        elif read_status in ['no', 'n']:
            read = False
            break
        else:
            print(COLORS['warning'] + "⚠️ Please enter 'yes' or 'no'.")
    
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    
    library.append(book)
    print(COLORS['success'] + f"\n✅ Book '{title}' added successfully!")
    return library

def remove_book(library):
    """Remove a book from the library with colorful interface"""
    if not library:
        print(COLORS['warning'] + "\n📚 Your library is empty!")
        return library
    
    print(COLORS['header'] + "\n" + "🗑️ REMOVE A BOOK".center(50, "─"))
    title = input(COLORS['book'] + "📝 Enter the title of the book to remove: " + COLORS['reset']).strip()
    
    found_books = [book for book in library if book['title'].lower() == title.lower()]
    
    if not found_books:
        print(COLORS['error'] + f"\n❌ No book with title '{title}' found.")
        return library
    
    if len(found_books) > 1:
        print(COLORS['info'] + f"\n🔍 Multiple books found with title '{title}':")
        for i, book in enumerate(found_books, 1):
            status = COLORS['read'] + "Read" if book['read'] else COLORS['unread'] + "Unread"
            print(f"{COLORS['menu']}{i}. {COLORS['author']}{book['author']} {COLORS['year']}({book['year']}) - {status}")
        
        while True:
            try:
                choice = int(input(COLORS['info'] + "\n⌨️ Enter the number of the book to remove: " + COLORS['reset']))
                if 1 <= choice <= len(found_books):
                    book_to_remove = found_books[choice-1]
                    library.remove(book_to_remove)
                    print(COLORS['success'] + f"\n✅ Book '{title}' removed successfully!")
                    return library
                else:
                    print(COLORS['warning'] + "⚠️ Invalid choice. Please try again.")
            except ValueError:
                print(COLORS['error'] + "❌ Please enter a valid number.")
    else:
        library.remove(found_books[0])
        print(COLORS['success'] + f"\n✅ Book '{title}' removed successfully!")
        return library

def search_books(library):
    """Search for books with colorful results"""
    if not library:
        print(COLORS['warning'] + "\n📚 Your library is empty!")
        return
    
    print(COLORS['header'] + "\n" + "🔍 SEARCH BOOKS".center(50, "─"))
    print(COLORS['menu'] + "1. 🔤 Search by title")
    print(COLORS['menu'] + "2. ✍️ Search by author")
    
    while True:
        try:
            choice = int(input(COLORS['info'] + "\n⌨️ Enter your choice (1-2): " + COLORS['reset']))
            if choice not in [1, 2]:
                print(COLORS['warning'] + "⚠️ Please enter 1 or 2.")
                continue
            break
        except ValueError:
            print(COLORS['error'] + "❌ Please enter a number.")
    
    search_term = input(COLORS['info'] + "\n🔎 Enter the search term: " + COLORS['reset']).strip().lower()
    results = []
    
    if choice == 1:
        results = [book for book in library if search_term in book['title'].lower()]
    else:
        results = [book for book in library if search_term in book['author'].lower()]
    
    if not results:
        print(COLORS['warning'] + "\n🔍 No matching books found.")
    else:
        print(COLORS['success'] + f"\n📚 Found {len(results)} matching book(s):")
        for i, book in enumerate(results, 1):
            status = (COLORS['read'] + "✔ Read") if book['read'] else (COLORS['unread'] + "✖ Unread")
            print(f"""
{COLORS['menu']}{i}. {COLORS['book']}{book['title']}
   {COLORS['author']}by {book['author']} {COLORS['year']}({book['year']})
   {COLORS['genre']}Genre: {book['genre']}
   {status}""")

def display_all_books(library):
    """Display all books with beautiful formatting"""
    if not library:
        print(COLORS['warning'] + "\n📚 Your library is empty!")
        return
    
    print(COLORS['header'] + "\n" + "📚 YOUR LIBRARY".center(50, "─"))
    for i, book in enumerate(library, 1):
        status = (COLORS['read'] + "✔ Read") if book['read'] else (COLORS['unread'] + "✖ Unread")
        print(f"""
{COLORS['menu']}{i}. {COLORS['book']}{book['title']}
   {COLORS['author']}by {book['author']} {COLORS['year']}({book['year']})
   {COLORS['genre']}Genre: {book['genre']}
   {status}""")
    print(COLORS['menu'] + "─" * 50)
    print(COLORS['success'] + f"Total books: {len(library)}")

def display_statistics(library):
    """Display statistics with visual elements"""
    if not library:
        print(COLORS['warning'] + "\n📚 Your library is empty!")
        return
    
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books) * 100
    
    # Create a simple bar chart
    read_bar = "▓" * int(percentage_read / 5)
    unread_bar = "░" * (20 - len(read_bar))
    
    print(COLORS['header'] + "\n" + "📊 LIBRARY STATISTICS".center(50, "─"))
    print(f"\n{COLORS['info']}📚 Total books: {COLORS['book']}{total_books}")
    print(f"\n{COLORS['info']}📖 Read books: {COLORS['read']}{read_books}")
    print(f"{COLORS['info']}📕 Unread books: {COLORS['unread']}{total_books - read_books}")
    print(f"\n{COLORS['info']}📈 Completion: {COLORS['read']}{percentage_read:.1f}%")
    print(f"\n{COLORS['menu']}[{read_bar}{unread_bar}]")
    print(COLORS['menu'] + "─" * 50)

def save_library(library, filename='library.json'):
    """Save the library to a file with status message"""
    try:
        with open(filename, 'w') as f:
            json.dump(library, f, indent=4)
        print(COLORS['success'] + f"\n💾 Library saved to {filename}")
    except Exception as e:
        print(COLORS['error'] + f"\n❌ Error saving library: {e}")

def load_library(filename='library.json'):
    """Load the library from a file with status message"""
    if not os.path.exists(filename):
        print(COLORS['warning'] + "\n📂 No existing library file found. Starting with empty library.")
        return []
    
    try:
        with open(filename, 'r') as f:
            library = json.load(f)
        print(COLORS['success'] + f"\n📂 Library loaded from {filename}")
        return library
    except Exception as e:
        print(COLORS['error'] + f"\n❌ Error loading library: {e}")
        return []

def main():
    """Main program function with colorful interface"""
    # Display beautiful banner
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    
    # Load library from file if it exists
    library = load_library()
    
    while True:
        display_menu()
        
        try:
            choice = int(input(COLORS['info'] + "\n⌨️ Enter your choice (1-6): " + COLORS['reset']))
        except ValueError:
            print(COLORS['error'] + "❌ Please enter a number between 1 and 6.")
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
            print(COLORS['header'] + "\n" + "🚪 EXITING".center(50, "─"))
            print(COLORS['success'] + "\n🌟 Thank you for using Personal Library Manager!")
            print(COLORS['menu'] + "✨ Happy reading!\n")
            break
        else:
            print(COLORS['error'] + "❌ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()