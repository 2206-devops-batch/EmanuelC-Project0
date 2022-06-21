from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'populate database'

    def handle(self, *args, **options):
        print('test successful')
        title = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet']
        descriptions =[]
        username = ['emanuel', 'edgar', 'carlos']
    
    def random_number_generator():
        pass

    def random_username(username):
        pass

    def random_title(title):
        pass

    def random_description(description):
        pass