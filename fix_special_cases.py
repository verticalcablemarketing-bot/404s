#!/usr/bin/env python3
"""
Fix special case redirects that don't follow the standard /product/XXX-... pattern.
"""

import csv

# Special case URL mappings
SPECIAL_CASES = {
    '/product/CAT5e Patch Cord 26 AWG F/UTP ETL/': 'https://verticalcable.com/patch-cords/',
    '/product/LGX Adapter Plates - Flanged (264-LAP Series)/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/Optical Fiber 2-mm Duplex Patch Cords/': 'https://verticalcable.com/patch-cords/',
    '/product/CAT3 Keystone Jacks - 350 Series/': 'https://verticalcable.com/keystones/',
    '/product/CAT5e Data Grade V-Max Keystone Jacks - 351 Series/': 'https://verticalcable.com/product/cat5e-v-max-keystone-jacks-351-series/',
    '/product/CAT6 UTP CMR - 161 Series/': 'https://verticalcable.com/keystones/',
    '/product/CAT6 UTP CMR - 060 Series/': 'https://verticalcable.com/product/cat6-utp-cmr-060-series-2/',
    '/product/LGX Cassettes 8 Fiber/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/CAT5e CMP F/UTP Cable - 057 Series/': 'https://verticalcable.com/product/cat5e-cmr-f-utp-cable-057-series/',
    '/product/CAT6A UTP CMR – 064-200s Series/': 'https://verticalcable.com/twisted-pair-systems/cat6a-cable/',
    '/product/CAT6 UTP CMP (Slim Type) - 166 Series/': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
    '/product/Keystone Module Panels (24-port) -266-PKM Series/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/Keystone Module Panels (48-port) - 266-PKM Series/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/Keystone Module Panels (266-PKM04 Series)/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/CAT5E UTP CMP (Plenum Rated) - 156 & 157 Series/': 'https://verticalcable.com/twisted-pair-systems/cat5e-cable/',
    '/product/Optical Fiber Splice Trays/Cassettes/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/CAT5e UTP CMP - 055 Series/': 'https://verticalcable.com/twisted-pair-systems/cat5e-cable/',
    '/product/CAT6A F/UTP CMP Cable - 165 Series/': 'https://verticalcable.com/twisted-pair-systems/cat6a-cable/',
    '/product/CAT6 F/UTP CMP (Plenum-Rated) - 168-400 Series/': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
    '/product/CAT5E Patch Cords, F/UTP with Boot & Protector - 071 Series/': 'https://verticalcable.com/patch-cords/',
    '/product/Outlet Module, OF Adapter, Panel Mounting, IP68/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/Outside Plant Loose Tube Optical Fiber Cable (Non-Armored)/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/Keystone Module Panels - 266-PKM04 Series/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/Keystone Module Panels (24-Port Medium Density) - 266-PKM Series/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/Keystone Module Panels (48-Port High Density) - 266-PKM Series/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/Optical Fiber Plenum Cable - Tight Buffer Singlemode (275-Series)/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/Optical Fiber Plenum Cable - Tight Buffer Multimode (271-274-Series)/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/CAT6 F/UTP Plenum-Rated (Shielded) - 168-300 Series/': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
    '/product/CAT5E 25 Pair UTP - 054 Series/': 'https://www.verticalcable.com/product-category/category-cable/cat5e-cable/cat5e-multipair/',
    '/product/Blank Adapter Plates (264-MAP Series)/': 'https://verticalcable.com/fiber-optic-systems/',
    '/product/CAT5E 50 Pair UTP - 054 Series/': 'https://www.verticalcable.com/product-category/category-cable/cat5e-cable/cat5e-multipair/',
    '/product/CAT5E 25 Pair (F/UTP) - 057 Series/': 'https://verticalcable.com/product/cat5e-cmr-f-utp-cable-057-series/',
    '/product/CAT6A Slim Type Patch Cords - 077 Series/': 'https://verticalcable.com/patch-cords/',
}

def main():
    # Read the UPDATED redirects
    redirects = []
    with open('rankmath-redirects-UPDATED.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            redirects.append(row)

    # Apply special case fixes
    updated_count = 0
    for redirect in redirects:
        if redirect['source'] in SPECIAL_CASES:
            new_dest = SPECIAL_CASES[redirect['source']]
            if new_dest != redirect['destination']:
                print(f"\nUpdating {redirect['source']}:")
                print(f"  OLD: {redirect['destination']}")
                print(f"  NEW: {new_dest}")
                redirect['destination'] = new_dest
                updated_count += 1

    print(f"\n{'='*60}")
    print(f"Special cases updated: {updated_count}")

    # Write back to file
    with open('rankmath-redirects-UPDATED.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['source', 'destination', 'type'])
        writer.writeheader()
        writer.writerows(redirects)

    print("Updated file saved: rankmath-redirects-UPDATED.csv")

if __name__ == '__main__':
    main()
