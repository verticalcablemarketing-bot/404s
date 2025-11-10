#!/usr/bin/env python3
"""
Script to find accurate redirect destinations for VerticalCable products
based on product family codes.
"""

import csv
import re
import time
from urllib.parse import urlparse

# Read the current redirects
redirects = []
with open('rankmath-redirects.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        redirects.append(row)

print(f"Total redirects to process: {len(redirects)}")

# Extract product family from source URL
def get_product_family(url):
    """Extract the 3-digit product family code from /product/XXX-... URLs"""
    match = re.search(r'/product/(\d{3})', url)
    return match.group(1) if match else None

# Analyze product families
families = {}
for redirect in redirects:
    family = get_product_family(redirect['source'])
    if family:
        if family not in families:
            families[family] = {
                'products': [],
                'current_destinations': set()
            }
        families[family]['products'].append(redirect['source'])
        families[family]['current_destinations'].add(redirect['destination'])

print(f"\nFound {len(families)} unique product families")
print("\nSample of families with current redirect patterns:")
for family in sorted(families.keys())[:10]:
    print(f"\nFamily {family}:")
    print(f"  Products: {len(families[family]['products'])}")
    print(f"  Current destinations: {families[family]['current_destinations']}")
    print(f"  Sample products: {families[family]['products'][:3]}")
