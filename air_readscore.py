"""
make class for getting the readability of books
"""


import re
import os
import nltk


class Book:
    def __init__(self, name, path):
        self.path = path
        self.name = name
        self.content = self.open_book()
        self.the_clean_text = None
        self.char_count = None
        self.word_count = None
        self.sent_count = None
        self.content = None

    def open_book(self):
        with open(self.path, 'r') as f:
            self.content = f.read()
            return self

    def clean_text(self):
        """
        clean the text
        """
        the_clean_text = re.sub(r'[^a-zA-Z\s]', '', self.content)
        self.the_clean_text = the_clean_text.replace('\n', '')
        return self

    def prosses_text(self):
        """
        removes unwanted thigs and split text
        so we can count words, lines and character
        """
        nltk_sent = nltk.sent_tokenize(self.content)
        # words = self.content.split()
        nltk_words = nltk.word_tokenize(self.content)
        char_str = self.the_clean_text.replace(' ', '')
        # all counts for readibility are here -- V
        self.char_count = len(char_str)
        self.word_count = len(nltk_words)
        self.sent_count = len(nltk_sent)
        return self

    def get_readability(self):
        """
        get the read scor for books
        using the automated readability index (ARI)
        https://en.wikipedia.org/wiki/Automated_readability_index
        """
        # lol htis is all fucked
        readability = 4.71 * (self.char_count / self.word_count) + 0.5 \
            * (self.word_count / self.sent_count) - 21.43

        return [self.name[:-4], readability]


def get_books(the_path):
    """
    get books and send them thru the book class
    """

    # make list of books in given dir
    the_files = [a_file for a_file in os.listdir(the_path)
                 if a_file.endswith('.txt')]

    # call the whole book class on a file
    books = []
    for sing_file in the_files:
        the_book = Book(sing_file, the_path + sing_file)
        # the_book.open_book().clean_text().prosses_text().get_readability()
        the_book.open_book()
        the_book.clean_text()
        the_book.prosses_text()
        books.append(the_book.get_readability())
    return books


def show_books(books):
    for book in books:
        print(book)


def lord_func():
    """
    lets start this shit
    """
    library_path = '/home/chris/unsort/ari/books/'
    books = get_books(library_path)
    show_books(books)


lord_func()
