from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from shop.models import Category

UserModel = get_user_model()

CATEGORIES = [
    {
        'name': 'Fruit',
        'active': True,
        'products': [
            {
                'name': 'Banane',
                'active': True,
                'articles': [
                    {
                        'name': 'Unité',
                        'price': 2.50,
                        'active': True
                    },
                    {
                        'name': 'Lot de 2',
                        'price': 4.50,
                        'active': True
                    },
                ]
            },
            {
                'name': 'Kiwi',
                'active': True,
                'articles': [
                    {
                        'name': 'Unité',
                        'price': 0.75,
                        'active': True
                    },
                    {
                        'name': 'Lot de 5',
                        'price': 3.00,
                        'active': True
                    },
                ]
            },
            {
                'name': 'Ananas',
                'active': False,
                'articles': [
                    {
                        'name': 'Unité',
                        'price': 2.50,
                        'active': False
                    }
                ]
            },
        ]
    },
    {
        'name': 'Légumes',
        'active': True,
        'products': [
            {
                'name': 'Courgette',
                'active': True,
                'articles': [
                    {
                        'name': 'Unité',
                        'price': 1.00,
                        'active': True
                    },
                    {
                        'name': 'Lot de 3',
                        'price': 2.50,
                        'active': False
                    },
                ]
            }
        ]
    },
    {
        'name': 'Épicerie',
        'active': True,
        'products': [
            {
                'name': 'Sel',
                'active': True,
                'articles': [
                    {
                        'name': '100g',
                        'price': 1.00,
                        'active': False
                    },
                    {
                        'name': '300g',
                        'price': 2.50,
                        'active': False
                    },
                ]
            }
        ]
    }
]

ADMIN_ID = 'admin-oc'
ADMIN_PASSWORD = 'password-oc'


class Command(BaseCommand):

    help = 'Initialize project for local development'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))

        Category.objects.all().delete()

        for data_category in CATEGORIES:
            category = Category.objects.create(name=data_category['name'],
                                               active=data_category['active'])
            for data_product in data_category['products']:
                product = category.products.create(name=data_product['name'],
                                                   active=data_product['active'])
                for data_article in data_product['articles']:
                    product.articles.create(name=data_article['name'],
                                            active=data_article['active'],
                                            price=data_article['price'])

        UserModel.objects.create_superuser(ADMIN_ID, 'admin@oc.drf', ADMIN_PASSWORD)

        self.stdout.write(self.style.SUCCESS("All Done !"))
