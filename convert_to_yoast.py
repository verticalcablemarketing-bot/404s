#!/usr/bin/env python3
"""
Convert updated redirects to Yoast SEO Premium format.
"""

import csv

def main():
    # Read the updated redirects
    redirects = []
    with open('rankmath-redirects-UPDATED.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            redirects.append(row)

    print(f"Converting {len(redirects)} redirects to Yoast SEO format...")

    # Convert to Yoast format
    yoast_redirects = []
    for redirect in redirects:
        yoast_redirect = {
            'Origin': redirect['source'],
            'Target': redirect['destination'],
            'Type': redirect['type'],
            'Format': 'plain'
        }
        yoast_redirects.append(yoast_redirect)

    # Write to Yoast format CSV
    with open('wordpress-seo-redirects.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Origin', 'Target', 'Type', 'Format'])
        writer.writeheader()
        writer.writerows(yoast_redirects)

    print(f"✓ Yoast SEO redirects saved to: wordpress-seo-redirects.csv")
    print(f"  Total redirects: {len(yoast_redirects)}")

    # Generate summary statistics
    destinations = {}
    for redirect in redirects:
        dest = redirect['destination']
        if dest not in destinations:
            destinations[dest] = 0
        destinations[dest] += 1

    print(f"\n{'='*60}")
    print("Top 15 Redirect Destinations:")
    sorted_destinations = sorted(destinations.items(), key=lambda x: x[1], reverse=True)
    for dest, count in sorted_destinations[:15]:
        print(f"  {count:4d} -> {dest}")

if __name__ == '__main__':
    main()
