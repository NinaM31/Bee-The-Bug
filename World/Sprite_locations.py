'''
The pixel coordinates inside sprite file
'''
interactable = {
    'F': (
        60, 0, 
        (98, 98),
        ['Nice Fountain, Looks new.', 'Fresh and clear Water.', 'New fancy Fountain.']
    ),
    'H': (
        0, 0, 
        (32, 32),
        ['Narrow hole on the ground.', 'Some narrow hole.', 'Hidden hole beside tree.', "Can't get inside too narrow."]
    ),
    'DB': (
        0, 72, 
        (35, 58),
        ['Beeware the water.', 'Old bridge be careful.', 'Bank in the middle.', "Don't cut trees."]
    ),
    'D': (
        50, 106, 
        (36, 60),
        'Press Enter to get inside'
    ),
    'G': (
        8, 181, 
        (65, 60),
        'Press Enter to get inside'
    ),
    'b': (
        118, 136, 
        (32, 22),
        'Trip plans to Maldives'
    ),
    'J': (
        118, 104, 
        (32, 24),
        'Expensive Jewelry for such house'
    ),
    'CA': (
        1, 32, 
        (36, 36),
        'Press Enter to exit'
    ),
    'Bb': (
        170, 5, 
        (38, 64),
        ["You don't have time to sleep!", "Can't sleep now", "Who stole the bank? can't sleep now"]
    ),
    'L': (
        170, 107, 
        (20, 20),
        "Message: I'll make you regret leaving me. I will end you'r life!!!"
    ),
    'LS': (
        167, 135, 
        (30, 20),
        'Letters from Mr. Fly (ex husband of Ladybug)'
    ),
    'CH': (
        210, 120, 
        (30, 33),
        'inside: Old wedding ring... and rotten apple'
    ),
    'A': (
        217, 3, 
        (30, 32),
        ['Barrel of Apples', 'Fresh Apples']
    ),
}
Water_coordinates = {
    'W': (192, 36),
    'L': (160, 32),
    'R': (224, 32), 
    'T': (204, 0),
    'B': (204, 62),
    'LT': (160, 0),
    'LB': (160, 64),
    'RT': (224, 0),
    'RB': (224, 64),
    'LTC': (160, 126),
    'LBC': (160, 96),
    'RTC': (128, 126),
    'RBC': (128, 96)
}

Bridge_coordinates = {
    'SL': (0, 1056), #side left
    'SC': (32, 1056), #side center
    'SR': (64, 1056), #side right
    'FT': (103, 1056), #front top
    'FC': (103, 1087), #front center
    'FB': (103, 1119), #front bottom
}

Plant_coordinates = {
    'W': (128, 192), #white flower
    'F': (224, 3742), #flower in pot
    'P': (160, 192), #purple flower
    'G': (0, 192), #large grass
    'g': (34, 192), #small grass
    'T': (64, 32), #Tree
    'B': (32, 160), #Bush 
}

OnRoad_coordinates = {
    'F': (0, 3712), #fountain
    'W': (162, 160), #broken wood
    'S': (0, 256), #stone
    'B': (192, 896), #wodden board
    'DB': (159, 896), #direction board
    'H': (64, 254), #holes
    'A': (64, 3456), #axe on wood
    'SF': (128, 3615), #statue figure
    'WB': (96, 895), #well bucket
    'WW': (65, 895), #water well
    'G': (192, 3424), #golden chest
}

Home_accessories_coordinates = {
    'B': (0, 3456), #bucket of water
    'C': (64, 3424), #closed pot
    'CH': (192, 1087), #clothes hanger
    'BH': (192, 1027), #blanket hanger
    'EH': (192, 961), #empty hanger
    'BB': (128, 3531), #barrels
    'W': (0, 3531), #wheat
    'A': (161, 3488), #barrel of apples
    'M': (128, 895), #mail box
    'BS': (128, 2657), #bank sign
}

H1_coordinates = {
    'B': (32, 1536), #base wall
    'EL': (0, 1536), #wall left edge
    'ER': (64, 1536), #wall right edge
    'C': (4, 1536), #wall center
    'LW': (0, 1536), #wall left
    'RW': (64, 1536), #wall right
    'R': (32, 2240), #roof
    'CH': (228, 2240), #chimney
    'D': (224, 2048), #door
    'W': (160, 2376), #window
}

H2_coordinates = {
    'B': (32, 1472), #base wall
    'EL': (0, 1472), #wall left edge
    'ER': (64, 1472), #wall right edge
    'C': (4, 1472), #wall center
    'LW': (0, 1472), #wall left
    'RW': (64, 1472), #wall right
    'R': (0, 2240), #roof
    'CH': (228, 2240), #chimney
    'D': (224, 1472), #door
    'W': (36, 2376), #window
}

H3_coordinates = {
    'B': (32, 1856), #base wall
    'EL': (0, 1856), #wall left edge
    'ER': (64, 1856), #wall right edge
    'C': (4, 1856), #wall center
    'LW': (0, 1856), #wall left
    'RW': (64, 1856), #wall right
    'R': (64, 2240), #roof
    'CH': (228, 2240), #chimney
    'D': (224, 1856), #door
    'W': (192, 2376), #window
}

H4_coordinates = {
    'B': (32, 1408), #base wall
    'EL': (0, 1408), #wall left edge
    'ER': (64, 1408), #wall right edge
    'C': (4, 1408), #wall center
    'LW': (0, 1408), #wall left
    'RW': (64, 1408), #wall right
    'R': (192, 2240), #roof
    'CH': (228, 2240), #chimney
    'D': (224, 1408), #door
    'W': (32, 2376), #window
}

H5_coordinates = {
    'B': (32, 2112), #base wall
    'EL': (0, 2112), #wall left edge
    'ER': (64, 2112), #wall right edge
    'C': (4, 2112), #wall center
    'LW': (0, 2112), #wall left
    'RW': (64, 2112), #wall right
    'R': (96, 2240), #roof
    'CH': (228, 2240), #chimney
    'G': (128, 2562), #gate
    'W': (32, 2376), #window
}

#Ladybug
house_1 = {
    'V': (0, 2688), #vertical wall
    'H': (32, 2688), #horizontal wall 
    'Bb': (64, 3104), #bed
    'b': (0, 3808), #book
    'T': (128, 2816), #table
    'C': (128, 2880), #chair
    'BS': (96, 2848), #book shelf
    'CB': (64, 2848), #cupboard
    'NT': (96, 2976), #nice table
    'NC': (96, 3010), #nice chair
    'J': (0, 4030), #Jewelry
    'K': (96, 3072), #kitchen table
    'KS': (128, 3072), #kitchen sink
    'CA': (160, 1152), #carpet 
    'LS': (63, 3900), #letters
    'L':(38, 3903), #letter
    'CH': (130, 3424), #chest
    0: (14, 12), #width, height
    1: ((96, 2720), (0, 2688)), #wall border (front, side)
    2: (96, 1183), #floor
}

house_2 = {
    'V': (0, 2688), #vertical wall
    'H': (32, 2688), #horizontal wall 
    'Bb': (64, 3104), #bed
    'b': (96, 2848), #book
    'T': (128, 2816), #table
    'C': (128, 2880), #chair
    'BS': (96, 2848), #book shelf
    'CB': (64, 2848), #cupboard
    'NT': (96, 2976), #nice table
    'NC': (96, 3010), #nice chair
    'J': (0, 4030), #Jewelry
    'K': (96, 3072), #kitchen table
    'KS': (128, 3072), #kitchen sink
    0: (14, 12), #width, height
    1: ((96, 2720), (0, 2688)), #wall border (front, side)
}

# Ants House
house_3 = {
    'V': (224, 2752), #vertical wall
    'H': (64, 2784), #horizontal wall 
    'Bb': (64, 3104), #bed
    'CA': (128, 1312), #carpet 
    0: (16, 12), #width, height
    1: ((96, 2752), (224, 2806)), #wall border (front, side)
    2: (160, 1248), #floor
}

house_4 = {
    'V': (128, 2688), #vertical wall
    'H': (160, 2688), #horizontal wall 
    'CA': (0, 1152), #carpet 
    0: (10, 9), #width, height
    1: ((224, 2720), (128, 2741)), #wall border (front, side)
    2: (0, 1184), #floor
}

house_5 = {
    'TT': (2, 3397),
    'CA': (64, 1248),
    0: (7, 7), #width, height
    1: ((96, 2720), (0, 2688)), #wall border (front, side)
    2: (64, 1216), #floor
}