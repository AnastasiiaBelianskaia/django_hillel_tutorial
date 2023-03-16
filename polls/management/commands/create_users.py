from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates users for database (from 1 to 10)'

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, choices=range(1, 11))

    def handle(self, *args, **kwargs):
        quantity = kwargs['quantity']
        users_list = []
        for number in range(quantity):
            users_list.append(User(username=f"User{number}",
                                   email=f"users{number}email@example.com",
                                   password=make_password(f"User{number}")))
        User.objects.bulk_create(users_list)
        self.stdout.write(f"{quantity} users has been created in database!")
