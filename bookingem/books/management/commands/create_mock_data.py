import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from books.models import Author, Book, Review


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()
        authors_amount = 10000
        books_amount = 50000
        reviews_amount = 99999

        genres = [
            "fiction",
            "non-fiction",
            "science",
            "fantasy",
            "history",
            "biography",
            "romance",
        ]
        possible_tags = [
            "bestseller",
            "new",
            "classic",
            "award-winning",
            "popular",
            "trending",
        ]

        self.stdout.write(self.style.HTTP_INFO("Starting data generation..."))
        try:
            with transaction.atomic():
                # Cleanup
                Author.objects.all().delete()
                Book.objects.all().delete()
                Review.objects.all().delete()

                author_emails = set()
                while len(author_emails) < authors_amount:
                    author_emails.add(faker.unique.email())
                author_emails = list(author_emails)

                authors = [
                    Author(
                        first_name=faker.first_name(),
                        last_name=faker.last_name(),
                        email=author_emails[i],
                        is_active=True,
                    )
                    for i in range(authors_amount)
                ]
                authors = Author.objects.bulk_create(authors)
                self.stdout.write(
                    self.style.SUCCESS(f"{len(authors)} authors created successfully!")
                )

                books = []
                for _ in range(books_amount):
                    genre = random.choice(genres)
                    tags_count = random.randint(0, 3)
                    tags = random.sample(possible_tags, tags_count)
                    tags = [tag.lower() for tag in tags]

                    books.append(
                        Book(
                            title=faker.catch_phrase(),
                            author=random.choice(authors),
                            published_date=faker.date_time_between(
                                start_date="-10y", end_date="now"
                            ),
                            price=Decimal(random.uniform(5.00, 100.00)).quantize(
                                Decimal("0.01")
                            ),
                            discount=Decimal(random.uniform(0, 50)).quantize(
                                Decimal("0.01")
                            ),
                            metadata={
                                "genre": genre,
                                "tags": tags,
                                "pages": random.randint(100, 1000),
                                "isbn": faker.isbn13(),
                            },
                        )
                    )
                books = Book.objects.bulk_create(books)
                self.stdout.write(
                    self.style.SUCCESS(f"{len(books)} books created successfully!")
                )

                reviews = []
                for _ in range(reviews_amount):
                    reviews.append(
                        Review(
                            book=random.choice(books),
                            rating=random.randint(1, 5),
                            comment=faker.text(max_nb_chars=150),
                        )
                    )
                reviews = Review.objects.bulk_create(reviews)
                self.stdout.write(
                    self.style.SUCCESS(f"{len(reviews)} reviews created successfully!")
                )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error during data generation: {e}"))
