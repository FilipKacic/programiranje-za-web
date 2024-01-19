import random
from django.core.management.base import BaseCommand
from main.factories import AuthorFactory, GenreFactory, BookFactory

NUM_AUTHORS = 64
NUM_GENRES = 8
NUM_BOOKS = 64

class Command(BaseCommand):
    help = "Generates test data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        self.stdout.write("Creating new data...")

        # Generate genres and print for verification
        genres = self.generate_genres()
        self.print_verification("Genre", genres)

        # Generate authors and print for verification
        authors = self.generate_authors()
        self.print_verification("Author", authors)

        # Generate books with random authors and a random number of genres
        self.generate_books(authors, genres)

        self.stdout.write(self.style.SUCCESS("Test data created successfully."))

    def generate_genres(self):
        return GenreFactory.create_batch(NUM_GENRES)

    def generate_authors(self):
        return AuthorFactory.create_batch(NUM_AUTHORS)

    def generate_books(self, authors, genres):
        for _ in range(NUM_BOOKS):
            num_genres_for_book = random.randint(1, NUM_GENRES)
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
