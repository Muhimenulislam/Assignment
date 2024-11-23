class Book:
    def __init__(self, title, author, pages):
        """
        Initializes the book with title, author, and pages.

        Args:
        title (str): The title of the book.
        author (str): The author of the book.
        pages (int): The number of pages in the book.
        """
        self.title = title
        self.author = author
        self.pages = pages

    def get_description(self):
        """
        Returns a string description of the book.

        Returns:
        str: Description of the book in the format "Title by Author, Pages: X".
        """
        return f"{self.title} by {self.author}, Pages: {self.pages}"


# Sample Input and Output
book1 = Book("1984", "George Orwell", 328)
print(book1.get_description())

