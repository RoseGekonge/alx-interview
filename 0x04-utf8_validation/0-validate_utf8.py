#!/usr/bin/python3
"""
Method to determine if given data represents valid UTF-8 encoding
Prototype: def validUTF8(data)
Returns True if data is valid UTF-8 encoding, else return False
Dataset can contain multiple characters
Data will represent a list of integers
"""


def validUTF8(data):
    """
    Prototype: def validUTF8(data)
    Returns True if data is valid UTF-8 encoding
    else return False
    """
    for dec in data:
        bin_checker = int(bin(127)[2:])
        bin_value = int(bin(dec)[2:])
        if bin_value > bin_checker:
            return False
        else:
            continue
    return True
