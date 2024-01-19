from django.test import TestCase
from main.models import *

class GenreModelTest(TestCase):
    def test_str_representation(self):
        genre = Genre(name='Mystery', description='A mysterious genre')
        self.assertEqual(str(genre), 'Mystery')

    def test_create_genre(self):
        genre = Genre.objects.create(name='Fantasy', description='A fantasy genre')
        self.assertEqual(genre.name, 'Fantasy')
        self.assertEqual(genre.description, 'A fantasy genre')

class AuthorModelTest(TestCase):
    def test_str_representation(self):
        author = Author(name='John', surname='Doe')
        self.assertEqual(str(author), 'John Doe')

    def test_create_author(self):
        author = Author.objects.create(name='Jane', surname='Smith')
        self.assertEqual(author.name, 'Jane')
        self.assertEqual(author.surname, 'Smith')

class BookModelTest(TestCase):
    def test_str_representation(self):
        author = Author.objects.create(name='Jane', surname='Doe')
        genre = Genre.objects.create(name='Mystery', description='A mysterious genre')
        book = Book(author=author, title='Mysterious Book', description='A mysterious story')
        self.assertEqual(str(book), 'Jane Doe by Mysterious Book')

    def test_create_book(self):
        author = Author.objects.create(name='John', surname='Smith')
        genre = Genre.objects.create(name='Science Fiction', description='A sci-fi genre')
        book = Book.objects.create(author=author, title='Sci-Fi Adventure', description='An exciting sci-fi adventure')
        self.assertEqual(book.title, 'Sci-Fi Adventure')
        self.assertEqual(book.description, 'An exciting sci-fi adventure')
        self.assertEqual(book.genres.count(), 0)

    def test_add_genre_to_book(self):
        author = Author.objects.create(name='Jane', surname='Doe')
        genre = Genre.objects.create(name='Romance', description='A romantic genre')
        book = Book.objects.create(author=author, title='Love Story', description='A heartwarming love story')
        book.genres.add(genre)
        self.assertEqual(book.genres.count(), 1)
        self.assertEqual(book.genres.first().name, 'Romance')

    def test_unique_together_constraint(self):
        author = Author.objects.create(name='Jane', surname='Doe')
        Book.objects.create(author=author, title='Mysterious Book', description='A mysterious story')
        # Attempt to create another book with the same author and title (violating unique_together constraint)
        with self.assertRaises(Exception):
            Book.objects.create(author=author, title='Mysterious Book', description='Another mysterious story')
