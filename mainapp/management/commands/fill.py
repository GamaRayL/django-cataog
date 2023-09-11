from django.core.management import BaseCommand

from mainapp.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()

        catalog_list = [
            {'name': 'Мониторы', 'description': 'Устройства отображения данных'},
            {'name': 'Устройства ввода данных', 'description': 'Клавиатуры, мыши и другие манипуляторы'},
            {'name': 'Холодильники', 'description': 'Оборудование, что сохранит ваши продукты на долгий срок'},
        ]

        category_for_create = []

        for category in catalog_list:
            category_for_create.append(
                Category(**category)
            )

        Category.objects.bulk_create(category_for_create)
