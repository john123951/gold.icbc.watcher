import re


def getAmount(str):
    matches = re.match(r'\D*(\d+(\.?\d+)?)', str)
    if matches:
        return float(matches.group(1))
    return
