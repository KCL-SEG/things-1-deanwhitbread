from django.core.management.base import BaseCommand, CommandError
import uuid
from django.db import models
from things.models import Thing
from faker import Faker
from faker.providers import lorem

class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker("en_GB")
        Faker.seed(110)
        for n in range(0, 100):
            new_entry = Thing(n, faker.text(max_nb_chars=30), faker.text(max_nb_chars=120), faker.random_digit())
            new_entry.full_clean()
            new_entry.save()
