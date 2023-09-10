Indain_states = (
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu & Kashmir", "Jammu & Kashmir"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttar Pradesh"),
    ("West Bengal", "West Bengal"),
    ("Andaman & Nicobar Islands", "Andaman & Nicobar Islands"),
    ("Chandigarh", "Chandigarh"),
    ("Dadra & Nagar Haveli", "Dadra & Nagar Haveli"),
    ("Daman & Diu", "Daman & Diu"),
    ("Lakshadweep", "Lakshadweep"),
    ("National Capital Territory of Delhi", "National Capital Territory of Delhi"),
    ("Puducherry", "Puducherry"),
)

categories = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),)

status_choices = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)

filter_options_m = {
    None: {'category': 'M'},
    'Apple': {'category': 'M', 'brand': 'Apple'},
    'REDMI': {'category': 'M', 'brand': 'REDMI'},
    'Samsung': {'category': 'M', 'brand': 'Samsung'},
    'MOTOROLA': {'category': 'M', 'brand': 'MOTOROLA'},
    'Oneplus': {'category': 'M', 'brand': 'Oneplus'},
    'POCO': {'category': 'M', 'brand': 'POCO'},
    'Below': {'category': 'M', 'discounted_price__lt': 10000},
    'Above': {'category': 'M', 'discounted_price__gt': 10000},
}

filter_options_l = {
    None: {'category': 'L'},
    'ASUS': {'category': 'L', 'brand': 'ASUS'},
    'HP': {'category': 'L', 'brand': 'HP'},
    'Lenovo': {'category': 'L', 'brand': 'Lenovo'},
    'Apple': {'category': 'L', 'brand': 'Apple'},
    'MSI': {'category': 'L', 'brand': 'MSI'},
    'Below': {'category': 'L', 'discounted_price__lt': 50000},
    'Above': {'category': 'L', 'discounted_price__gt': 50000}
}

filter_options_bw = {
    None: {'category': 'BW'},
    'KOTTY': {'category': 'BW', 'brand': 'KOTTY'},
    'TokyoTalkies': {'category': 'BW', 'brand': 'TokyoTalkies'},
    'LEVIS': {'category': 'BW', 'brand': 'LEVIS'},
    'AllenMartin': {'category': 'BW', 'brand': 'AllenMartin'},
    'Highlander': {'category': 'BW', 'brand': 'Highlander'},
    'UrbanoPlus': {'category': 'BW', 'brand': 'UrbanoPlus'},
    'Below': {'category': 'BW', 'discounted_price__lt': 500},
    'Above': {'category': 'BW', 'discounted_price__gt': 500}
}

filter_options_tw = {
    None: {'category': 'TW'},
    'METRONAUT': {'category': 'TW', 'brand': 'METRONAUT'},
    'PUMA': {'category': 'TW', 'brand': 'PUMA'},
    'ADIDAS': {'category': 'TW', 'brand': 'ADIDAS'},
    'PARKAVENUE': {'category': 'TW', 'brand': 'PARKAVENUE'},
    'DennisLingo': {'category': 'TW', 'brand': 'DennisLingo'},
    'JaiTextiles': {'category': 'TW', 'brand': 'JaiTextiles'},
    'Below': {'category': 'TW', 'discounted_price__lt': 500},
    'Above': {'category': 'TW', 'discounted_price__gt': 500},
}
