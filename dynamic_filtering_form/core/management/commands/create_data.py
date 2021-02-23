from django.core.management.base import BaseCommand
import random
import datetime
from core.models import *

categories = ["Sports", "Tech", "Fashion", "Music", "Travelling"]

authors = ["Ola Aremu", "Yomi Akanbi", "Seyi Adisa", "Kemi Adebola", "Bunmi Atinuke", "Dimeji Theophilus", "Kunbi Olalude"]


def generate_author_name():
    index = random.randint(0, len(authors) - 1)
    return authors[index]


def generate_category_name():
    index = random.randint(0, len(categories) - 1)
    return categories[index]


def generate_view_count():
    return random.randint(0, 250)


def generate_is_reviewed():
    index = random.randint(0, 1)
    return bool(index)


def generate_publish_date():
    year = random.randint(2000, 2030)
    month = random.randint(1, 12)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = random.randint(1, 31)
    elif month == 2:
        day = random.randint(1, 28)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = random.randint(1, 30)

    return datetime.date(year, month, day)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "file_name", type=str, help="the text file that contains the journal titles.")

    def handle(self, *args, **kwargs):
        file_name = kwargs["file_name"]
        with open(f'{file_name}.txt') as file:
            for row in file:
                title = row
                author_name = generate_author_name()
                category_name = generate_category_name()
                publish_date = generate_publish_date()
                views = generate_view_count()
                reviewed = generate_is_reviewed()

                author = Author.objects.get_or_create(
                    name=author_name
                )

                journal = Journal.objects.create(
                    title=title,
                    author=Author.objects.get(name=author_name),
                    publish_date=publish_date,
                    views=views,
                    reviewed=reviewed
                )

                journal.save()

                category = Category.objects.get_or_create(name=category_name)

                journal.categories.add(Category.objects.get(name=category_name))

        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
