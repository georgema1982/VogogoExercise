from itertools import groupby

def checkout(codes, item_lookup, prices_lookup):
    receipt = []
    codes.sort()
    for code, group in groupby(codes):
        prices = prices_lookup(code)
        remainder = sum(1 for _ in group)
        itemized_list = []
        for price in prices:
            quotient, remainder = divmod(remainder, price.quantity)
            if quotient: itemized_list.append((quotient * price.quantity, unicode(price), quotient * price.price))
        receipt.append((item_lookup(code), itemized_list))
    return receipt

def print_line(line, width, amount):
    line += ('%.2f' % amount).rjust(width - len(line))
    print line

def print_receipt(receipt, width):
    total = 0
    for item in receipt:
        print '%s%s%s' % (item[0].code, ' ' * 4, item[0].name)
        for receipt_item in item[1]:
            total += receipt_item[2]
            print_line('%s%s @ %s' % (' ' * 2, receipt_item[0], receipt_item[1]), width, receipt_item[2])
    print ''
    print_line('TOTAL', width, total)
