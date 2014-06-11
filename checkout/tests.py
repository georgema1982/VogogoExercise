from checkout.models import Price, Item
from django.test import TestCase
from random import shuffle
from checkout.core import checkout, print_receipt

# Create your tests here.
def item_lookup(code):
    '''
    Item code 1: Apple
    Item code 2: Orange
    Item code 3: Banana
    '''
    if code == '1': return Item(name = 'Apple', code = '1')
    if code == '2': return Item(name = 'Orange', code = '2')
    if code == '3': return Item(name = 'Banana', code = '3')

def prices_lookup(code):
    '''
    Item code 1: Apple
    Item code 2: Orange
    Item code 3: Banana
    '''
    if code == '1': return (Price(quantity = 5, price = 1.8), Price(quantity = 3, price = 1.2), Price(quantity = 1, price = 0.5))
    if code == '2': return (Price(quantity = 3, price = 1.4), Price(quantity = 1, price = 0.8))
    if code == '3': return (Price(quantity = 1, price = 0.4),)

class CheckoutTest(TestCase):

    def test_checkout_one_orange(self):
        items = ['2']
        receipt = checkout(items, item_lookup, prices_lookup)
        self.assertEqual(len(receipt), 1, 'There should be only 1 item.')
        item = receipt[0]
        self.assertEqual(item[0].code, '2', 'The item should be orange')
        self.assertListEqual(item[1], [(1, '$0.80 ea', 0.8)], 'The receipt item should be\n1 @ $0.80 ea    0.80')

    def test_checkout_two_oranges(self):
        items = ['2'] * 2
        receipt = checkout(items, item_lookup, prices_lookup)
        self.assertEqual(len(receipt), 1, 'There should be only 1 item.')
        item = receipt[0]
        self.assertEqual(item[0].code, '2', 'The item should be orange')
        self.assertListEqual(item[1], [(2, '$0.80 ea', 1.6)], 'The receipt item should be\n2 @ $0.80 ea    1.60')

    def test_checkout_three_oranges(self):
        items = ['2'] * 3
        receipt = checkout(items, item_lookup, prices_lookup)
        self.assertEqual(len(receipt), 1, 'There should be only 1 item.')
        item = receipt[0]
        self.assertEqual(item[0].code, '2', 'The item should be orange')
        self.assertListEqual(item[1], [(3, '3/$1.40', 1.4)], 'The receipt item should be\n3 @ 3/$1.40    1.40')

    def test_checkout_four_oranges(self):
        items = ['2'] * 4
        receipt = checkout(items, item_lookup, prices_lookup)
        self.assertEqual(len(receipt), 1, 'There should be only 1 item.')
        item = receipt[0]
        self.assertEqual(item[0].code, '2', 'The item should be orange')
        self.assertListEqual(item[1], [(3, '3/$1.40', 1.4), (1, '$0.80 ea', 0.8)], 'The receipt items should be\n3 @ 3/$1.40    1.40\n1 @ $0.80 ea    0.80')

    def test_checkout_eight_oranges(self):
        items = ['2'] * 8
        receipt = checkout(items, item_lookup, prices_lookup)
        self.assertEqual(len(receipt), 1, 'There should be only 1 item.')
        item = receipt[0]
        self.assertEqual(item[0].code, '2', 'The item should be orange')
        self.assertListEqual(item[1], [(6, '3/$1.40', 2.8), (2, '$0.80 ea', 1.6)], 'The receipt items should be\n6 @ 3/$1.40    2.80\n2 @ $0.80 ea    1.60')

    def test_checkout_mixed_itmes(self):
        items = ['3'] * 2 + ['2'] * 14 + ['1'] * 24
        shuffle(items)
        receipt = checkout(items, item_lookup, prices_lookup)
        self.assertEqual(len(receipt), 3, 'There should be 3 items.')
        apple = receipt[0]
        self.assertEqual(apple[0].code, '1', 'First item should be apple')
        self.assertListEqual(apple[1], [(20, '5/$1.80', 7.2), (3, '3/$1.20', 1.2), (1, '$0.50 ea', 0.5)], 'The receipt items should be\n20 @ 5/$1.80    7.20\n3 @ 3/$1.20    1.20\n1 @ $0.5 ea    0.50')
        orange = receipt[1]
        self.assertEqual(orange[0].code, '2', 'Second item should be orange')
        self.assertListEqual(orange[1], [(12, '3/$1.40', 5.6), (2, '$0.80 ea', 1.6)], 'The receipt items should be\n12 @ 3/$1.40    5.60\n2 @ $0.80 ea    1.60')
        banana = receipt[2]
        self.assertEqual(banana[0].code, '3', 'Third item should be banana')
        self.assertListEqual(banana[1], [(2, '$0.40 ea', 0.8)], 'The receipt items should be\n2 @ $0.40 ea    0.80')

class PrintTest(TestCase):

    def test(self):
        items = ['3'] * 2 + ['2'] * 14 + ['1'] * 24
        shuffle(items)
        print_receipt(checkout(items, item_lookup, prices_lookup), 50)
