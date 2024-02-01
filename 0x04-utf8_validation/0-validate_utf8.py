#!/usr/bin/python3
"""determining UTF-8 encoding"""


def validUTF8(data):
    """method to determine UTF-8 representation"""

    bytes = 0

    a1 = 1 << 7
    a2 = 1 << 6

    for i in data:
        a = 1 << 7
        if bytes == 0:
            while a & i:
                bytes += 1
                a = a >> 1
            if bytes == 0:
                continue
            if bytes == 1 or bytes > 4:
                return False
        else:
            if not (i & a1 and not (i & a2)):
                return False
        bytes -= 1
    return bytes == 0
