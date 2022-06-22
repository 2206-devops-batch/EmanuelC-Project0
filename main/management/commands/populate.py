from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from main.models import Task
from lorem_text import lorem
import random

class Command(BaseCommand):
    help = 'populate database'

    def handle(self, *args, **options):
        title_length = [1, 2, 3, 4, 5]
        des_length = [1, 2, 3]
        username_lst = ['emanuel', 'edgar', 'carlos']
        for n in range(10):
            title = lorem.words(random.choice(title_length))
            description = lorem.paragraph()
            username = random.choice(username_lst)
            user = User.objects.get(username = username) # using ORM getting user object becuase we have to pass user object during creation of new Task
            Task.objects.create(user = user, title = title, description = description, complete = 'True') # creating new Task