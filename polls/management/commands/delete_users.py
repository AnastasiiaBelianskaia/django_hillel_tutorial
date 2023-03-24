from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

User = get_user_model()


class Command(BaseCommand):
    help = 'Deletes users from database (by id)'

    def add_arguments(self, parser):
        parser.add_argument('users_id', nargs="+", type=int)

    def handle(self, *args, **kwargs):
        users_id = kwargs['users_id']

        if User.objects.filter(pk__in=users_id, is_superuser=True).exists():
            raise CommandError("You can't delete a superuser")
        count, _ = User.objects.filter(id__in=users_id, is_superuser=False).delete()
        self.stdout.write(f" {count} specified users has been deleted from database!")
