#!/usr/bin/env python3
"""
Update redirect destinations based on product family mapping.
"""

import csv
import re
from product_family_mapping import PRODUCT_FAMILY_MAPPING

def get_product_family(url):
    """Extract the 3-digit product family code from /product/XXX-... URLs"""
    match = re.search(r'/product/(\d{3})', url)
    return match.group(1) if match else None

def main():
    # Read current redirects
    redirects = []
    with open('rankmath-redirects.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            redirects.append(row)

    print(f"Total redirects to process: {len(redirects)}")

    # Update redirects based on family mapping
    updated_count = 0
    unchanged_count = 0
    no_mapping_count = 0

    updated_redirects = []

    for redirect in redirects:
        family = get_product_family(redirect['source'])

        if family and family in PRODUCT_FAMILY_MAPPING:
            new_destination = PRODUCT_FAMILY_MAPPING[family]

            if new_destination != redirect['destination']:
                old_dest = redirect['destination']
                redirect['destination'] = new_destination
                updated_count += 1

                # Show first 10 updates as examples
                if updated_count <= 10:
                    print(f"\nUpdating {redirect['source']}:")
                    print(f"  OLD: {old_dest}")
                    print(f"  NEW: {new_destination}")
            else:
                unchanged_count += 1
        else:
            no_mapping_count += 1
            if no_mapping_count <= 5:
                print(f"\nNo mapping found for: {redirect['source']} (family: {family})")

        updated_redirects.append(redirect)

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Updated: {updated_count}")
    print(f"  Unchanged (already correct): {unchanged_count}")
    print(f"  No mapping found: {no_mapping_count}")
    print(f"  Total: {len(updated_redirects)}")

    # Write updated redirects to new file
    with open('rankmath-redirects-UPDATED.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['source', 'destination', 'type'])
        writer.writeheader()
        writer.writerows(updated_redirects)

    print(f"\nUpdated redirects saved to: rankmath-redirects-UPDATED.csv")

    # Generate statistics by product family
    family_stats = {}
    for redirect in updated_redirects:
        family = get_product_family(redirect['source'])
        if family:
            if family not in family_stats:
                family_stats[family] = {
                    'count': 0,
                    'destination': redirect['destination']
                }
            family_stats[family]['count'] += 1

    print(f"\n{'='*60}")
    print("Top 10 Product Families by Redirect Count:")
    sorted_families = sorted(family_stats.items(), key=lambda x: x[1]['count'], reverse=True)
    for family, stats in sorted_families[:10]:
        print(f"  {family}: {stats['count']} redirects -> {stats['destination']}")

if __name__ == '__main__':
    main()
