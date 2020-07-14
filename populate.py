import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','TrainerForm.settings')
import django
django.setup()

from app_TrainerForm.models import *
from faker import Faker
from random import *
faker = Faker()

def populate(n):
    for i in range(n):
        first_name = faker.name()
        middle_name = faker.name()
        last_name = faker.name()
        trainer_id = randint(100,200)
        address = faker.city()
        trainer =Trainer.objects.get_or_create(first_name=first_name,middle_name=middle_name,last_name=last_name,trainer_id=trainer_id,address=address)

populate(10)
