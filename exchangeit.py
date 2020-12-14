"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Charles Smith
Date:   03 December 2020
"""

import currency

src = input('3-letter code for original currency: ')
dst = input('3-letter code for the new currency: ')
amt = input('Amount of the original currency: ')
exchange_amt = currency.exchange(src,dst,amt)
result = round(exchange_amt,3)
print('You can exchange ' + amt + ' ' + src + ' for ' + str(result) + ' ' +
dst + '.')
