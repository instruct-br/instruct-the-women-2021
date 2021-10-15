from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, **options):
        user=User.objects.create_user('instruct', password='instruct')
        user.save()
        self.stdout.write(self.style.SUCCESS('Usuário de API `instruct` e senha `instruct` criado'))
