import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

phoneNumRegex = re.compile(r'\d\d \d\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 41 5555-4242.')
print('Phone number found: ' + mo.group())
