from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='gamaizing@gmail.com',
            first_name='Gamid',
            last_name='Gadzhimagomedov',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('bro')
        user.save()
