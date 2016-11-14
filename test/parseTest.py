import re

value = ' 267.43元/克'
v2 = '267.43'

matches = re.match(r'\D*(\d+(\.?\d+)?)', value)
if matches:
    print(matches.group())
    print(matches.group(1))
    print(matches.group(2))
