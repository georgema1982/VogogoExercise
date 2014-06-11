from django.core.management.base import BaseCommand
from checkout.core import print_receipt, checkout
from checkout.models import Item, Price

class Command(BaseCommand):

    help = 'A console program that takes as input an unordered list of singular items from a shopping cart and "checks them out", printing an itemized receipt and a total price.'
    args = 'code [code ...]'

    def handle(self, *args, **options):
        if not args:
            print 'Nothing to checkout'
            return
        print_receipt(checkout(list(args), lambda code: Item.objects.get(code = code), lambda code: Price.objects.filter(item__code = code, active = True)), 50)
