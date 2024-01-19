import random
import factory
from factory.django import DjangoModelFactory

from main.models import *


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker("first_name")
    surname = factory.Faker("last_name")

class GenreFactory(DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Faker("sentence", nb_words=1)
    description = factory.Faker("sentence", nb_words=32)

class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("sentence", nb_words=64)

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            if hasattr(self, 'author'):
                self.author = random.choice(extracted)
                self.save()

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            if hasattr(self, 'genre'):
                self.genres.add(*extracted)
                self.save()
