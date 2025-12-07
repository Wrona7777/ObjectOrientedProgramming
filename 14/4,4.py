from ebook import EBook

def main():
    my_book = EBook("The Hobbit", "J.R.R. Tolkien", 310)
    
    my_book.open()
    my_book.show_status()
    
    my_book.next_page()
    my_book.next_page()
    my_book.next_page()
    my_book.show_status()
    
    my_book.close()
    my_book.next_page()

if __name__ == "__main__":
    main()