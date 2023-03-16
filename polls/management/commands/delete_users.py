from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = 'Deletes users from database (by id)'

    def add_arguments(self, parser):
        parser.add_argument('users_id', nargs="+", type=int)

    def handle(self, *args, **kwargs):
        users_id = kwargs['users_id']
        superuser_list = []
        for user in users_id:
            superuser_list.append(
                User.objects.filter(id=user, is_superuser=True).values_list('is_superuser', flat=True).first()
            )
        if True in superuser_list:
            return self.stdout.write("You can't delete a superuser")
        User.objects.filter(id__in=users_id).delete()
        self.stdout.write("Specified users has been deleted from database!")
