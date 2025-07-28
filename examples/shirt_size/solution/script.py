#!/usr/bin/env python3

def get_size(circumference):
    if circumference < 80 or circumference > 124:
        size = "N/A"
    elif circumference <= 90:
        size = "XS"
    elif circumference <= 98:
        size = "S"
    elif circumference <= 104:
        size = "M"
    elif circumference <= 111:
        size = "L"
    else:
        size = "XL"
    return size

