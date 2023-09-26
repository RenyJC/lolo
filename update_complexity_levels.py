from django.core.management.base import BaseCommand
from Soluciones_Textiles.models import Operation  # Reemplaza 'myapp' con el nombre de tu aplicación

class Command(BaseCommand):
    help = 'Update the complexity level of all operations'

    def handle(self, *args, **kwargs):
        for operation in Operation.objects.all():
            operation.update_complexity_level()
        self.stdout.write(self.style.SUCCESS('Successfully updated complexity levels'))
