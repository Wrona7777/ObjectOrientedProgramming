class EBook:
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page = 1
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def next_page(self):
        if self.is_open:
            if self.current_page < self.number_of_pages:
                self.current_page += 1
        else:
            print("The book is closed.")

    def previous_page(self):
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
        else:
            print("The book is closed.")

    def show_status(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Page count: {self.number_of_pages}")
        print(f"Current page: {self.current_page}")