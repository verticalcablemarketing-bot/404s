#!/usr/bin/env python3
"""
Product family mapping for VerticalCable redirects.
Maps 3-digit product family codes to their most specific redirect destinations.
"""

# Comprehensive product family mapping based on research
PRODUCT_FAMILY_MAPPING = {
    # CAT5E Cable Products - Series Pages Available
    '057': 'https://verticalcable.com/product/cat5e-cmr-f-utp-cable-057-series/',
    '151': 'https://verticalcable.com/product/cat5e-utp-cmr-151-series/',

    # CAT6 Cable Products
    '060': 'https://verticalcable.com/product/cat6-utp-cmr-060-series-2/',
    '062': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
    '063': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
    '067': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
    '068': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
    '069': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
    '094': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
    '095': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
    '166': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
    '168': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
    '302': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
    '352': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',

    # CAT6A Cable Products
    '064': 'https://verticalcable.com/twisted-pair-systems/cat6a-cable/',
    '065': 'https://verticalcable.com/twisted-pair-systems/cat6a-cable/',
    '165': 'https://verticalcable.com/twisted-pair-systems/cat6a-cable/',
    '176': 'https://verticalcable.com/twisted-pair-systems/cat6a-cable/',
    '303': 'https://verticalcable.com/twisted-pair-systems/cat6a-cable/',
    '353': 'https://verticalcable.com/twisted-pair-systems/cat6a-cable/',

    # CAT5E Cable Products - Category Pages
    '033': 'https://verticalcable.com/twisted-pair-systems/cat5e-cable/',
    '051': 'https://verticalcable.com/twisted-pair-systems/cat5e-cable/',
    '054': 'https://www.verticalcable.com/product-category/category-cable/cat5e-cable/cat5e-multipair/',
    '056': 'https://verticalcable.com/twisted-pair-systems/cat5e-cable/',
    '058': 'https://verticalcable.com/product-category/category-cable/cat5e-cable/cat5e-riser/',
    '059': 'https://verticalcable.com/twisted-pair-systems/cat5e-cable/',
    '071': 'https://verticalcable.com/twisted-pair-systems/cat5e-cable/',
    '078': 'https://verticalcable.com/twisted-pair-systems/cat5e-cable/',
    '092': 'https://verticalcable.com/twisted-pair-systems/cat5e-cable/',
    '093': 'https://verticalcable.com/twisted-pair-systems/cat5e-cable/',
    '156': 'https://verticalcable.com/twisted-pair-systems/cat5e-cable/',
    '157': 'https://verticalcable.com/twisted-pair-systems/cat5e-cable/',
    '301': 'https://verticalcable.com/twisted-pair-systems/cat5e-cable/',

    # CAT3 Cable Products
    '300': 'https://verticalcable.com/twisted-pair-systems/cat3-cable/',

    # Keystone Products
    '037': 'https://verticalcable.com/twisted-pair-systems/work-area/keystone-inserts/',
    '070': 'https://verticalcable.com/keystones/',
    '161': 'https://verticalcable.com/keystones/',
    '210': 'https://verticalcable.com/keystones/',
    '211': 'https://verticalcable.com/keystones/',
    '212': 'https://verticalcable.com/keystones/',
    '294': 'https://verticalcable.com/keystones/',
    '304': 'https://verticalcable.com/keystones/',
    '305': 'https://verticalcable.com/keystones/',
    '306': 'https://verticalcable.com/keystones/',
    '308': 'https://verticalcable.com/keystones/',
    '351': 'https://verticalcable.com/product/cat5e-v-max-keystone-jacks-351-series/',

    # Patch Panels
    '042': 'https://verticalcable.com/product-category/patch-panels/cat6-patch-panels/',
    '043': 'https://verticalcable.com/product-category/twisted-pair-systems/patch-panels/',

    # Patch Cords
    '076': 'https://verticalcable.com/patch-cords/',
    '077': 'https://verticalcable.com/patch-cords/',
    '261': 'https://verticalcable.com/patch-cords/',
    '263': 'https://verticalcable.com/patch-cords/',

    # RJ45 Boots and Accessories
    '015': 'https://verticalcable.com/product/rj45-slip-on-boots-cat6-cat6a-016-series/',
    '016': 'https://verticalcable.com/product/rj45-slip-on-boots-cat6-cat6a-016-series/',

    # Cable Management
    '044': 'https://verticalcable.com/product-category/cabling-support-infrastructure/',
    '045': 'https://verticalcable.com/product/standard-cable-ties-045-ct-50-series/',
    '048': 'https://www.verticalcable.com/product-category/cable-management/j-hooks/',

    # Mounting and Wall Plates
    '022': 'https://verticalcable.com/product/022-mb-series-mounting-bracket/',
    '028': 'https://www.verticalcable.com/product-category/connectivity/wall-plates/',
    '038': 'https://verticalcable.com/product/surface-mount-boxes-038-jack-series/',
    '040': 'https://www.verticalcable.com/product-category/connectivity/junction-boxes/',

    # Racks and Enclosures
    '047': 'https://verticalcable.com/product-category/racks-accessories/wall-mounts/',
    '049': 'https://verticalcable.com/products/',

    # Audio/Video Cable
    '107': 'https://verticalcable.com/audio-visual-cable/audio-cable/',
    '209': 'https://verticalcable.com/audio-visual-cable/audio-cable/',
    '214': 'https://verticalcable.com/audio-visual-cable/audio-cable/',
    '241': 'https://verticalcable.com/audio-visual-cable/video-cable/',
    '242': 'https://verticalcable.com/audio-visual-cable/video-cable/',
    '245': 'https://verticalcable.com/audio-visual-cable/video-cable/',
    '309': 'https://verticalcable.com/audio-visual-cable/audio-cable/',
    '315': 'https://verticalcable.com/audio-visual-cable/audio-cable/',

    # Fiber Optic Products
    '250': 'https://verticalcable.com/fiber-optic-systems/',
    '251': 'https://verticalcable.com/fiber-optic-systems/',
    '260': 'https://verticalcable.com/fiber-optic-systems/',
    '264': 'https://verticalcable.com/fiber-optic-systems/',
    '265': 'https://verticalcable.com/fiber-optic-systems/',
    '266': 'https://verticalcable.com/fiber-optic-systems/',
    '268': 'https://verticalcable.com/fiber-optic-systems/',
    '269': 'https://verticalcable.com/fiber-optic-systems/',

    # Coaxial
    '083': 'https://verticalcable.com/coaxial-cable/',

    # Connectors
    '252': 'https://verticalcable.com/connectors/',

    # Panels/Blocks
    '307': 'https://verticalcable.com/panels-blocks/',

    # General Products (families with no specific category)
    '066': 'https://verticalcable.com/products/',
    '167': 'https://verticalcable.com/products/',
    '254': 'https://verticalcable.com/products/',

    # Additional families from earlier analysis
    '012': 'https://verticalcable.com/twisted-pair-systems/cat6-cable/',
}

def get_redirect_for_family(family_code):
    """Get the redirect URL for a product family code."""
    return PRODUCT_FAMILY_MAPPING.get(family_code)

if __name__ == '__main__':
    print("Product Family Mapping")
    print(f"Total families mapped: {len(PRODUCT_FAMILY_MAPPING)}")
    print("\nSample mappings:")
    for family, url in list(PRODUCT_FAMILY_MAPPING.items())[:10]:
        print(f"  {family} -> {url}")
