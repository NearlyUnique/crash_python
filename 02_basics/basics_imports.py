#!/usr/bin/env python3

# first we install "dateparser" which can help use interpret human style date text and turn it into a real python date.
# Enter the following command in the command terminal
#
# pip install dateparser

from datetime import datetime # standard library
import dateparser # https://github.com/scrapinghub/dateparser
# use the my_function from the file sibling.py
from sibling import my_function
# use the other_function from ./custom/other.py
from custom import other

my_function()
other.other_function()

print(f"Today is {datetime.now()}")
future_date = dateparser.parse('In two months')
print(f"Two months from now is {future_date}")
