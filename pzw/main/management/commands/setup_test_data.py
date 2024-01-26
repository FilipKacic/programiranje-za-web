import random
from django.core.management.base import BaseCommand
from main.models import *
from main.factories import AuthorFactory, GenreFactory, BookFactory

NUM_AUTHORS = 64
NUM_GENRES = 8
NUM_BOOKS = 64

class Command(BaseCommand):
    help = "Deletes old and generates new test data."

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        self.delete_old_data()

        self.stdout.write("Generating new data...")

        # Generate genres and print for verification
        genres = self.generate_genres()
        self.print_verification("Genre", genres)

        # Generate authors and print for verification
        authors = self.generate_authors()
        self.print_verification("Author", authors)

        # Generate books with random authors and a random number of genres
        self.generate_books(authors, genres)

        self.stdout.write(self.style.SUCCESS("Test data generated successfully."))

    def delete_old_data(self):
        Genre.objects.all().delete()
        Author.objects.all().delete()
        Book.objects.all().delete()

    def generate_genres(self):
        return GenreFactory.create_batch(NUM_GENRES)

    def generate_authors(self):
        return AuthorFactory.create_batch(NUM_AUTHORS)

    def generate_books(self, authors, genres):
        for _ in range(NUM_BOOKS):
            num_genres_for_book = min(random.randint(1, NUM_GENRES), len(genres))
            author = random.choice(authors)
            book = BookFactory(author=author)
            book.genres.set(random.sample(genres, num_genres_for_book))  # Assign random genres to the book

            # Debug information
            self.stdout.write(self.style.SUCCESS(f"Selected Genres for Book: {book.genres.all()}"))
            self.stdout.write(self.style.SUCCESS(f"Selected Author for Book: {author}"))

    def print_verification(self, entity_type, entities):
        # Print entities for verification
        for entity in entities[:len(entities)]:
            self.stdout.write(self.style.SUCCESS(f"{entity_type}: {entity}"))
