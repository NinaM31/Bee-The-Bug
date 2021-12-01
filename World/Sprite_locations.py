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
    'GA': (
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
    'BbF': (
        261, 90, 
        (33, 66),
        ["You don't have time to sleep!", "Can't sleep now", "Who stole the bank? can't sleep now"]
    ),
    'BbA': (
        261, 6, 
        (70, 69),
        ["You don't have time to sleep!", "Can't sleep now", "Who stole the bank? can't sleep now"]
    ),
    'L': (
        170, 107, 
        (20, 20),
        "Message: I'll make you regret leaving me. I will end your life!!!"
    ),
    'LS': (
        167, 135, 
        (30, 20),
        'Letters from Mr. Fly (ex husband of Ladybug)'
    ),
    'CHH': (
        210, 120, 
        (30, 33),
        'Inside: Old wedding ring... and Fresh apple'
    ),
    'AA': (
        217, 3, 
        (30, 32),
        ['Barrel of Apples', 'Fresh Apples', 'Fresh Apples']
    ),
    'LA': (
        170, 107, 
        (20, 20),
        "Message: Dear Mr. Ant you need more investors, or your company dies."
    ),
    'LA2': (
        170, 107, 
        (20, 20),
        "Message: Dear Mr. Ant Why didn't you come to my bday?"
    ),
    'LSA': (
        167, 135, 
        (30, 20),
        'Urgent letters of company bankruptcy'
    ),
    'LF': (
        170, 107, 
        (20, 20),
        ["Draft: I hate you !!!", 'Draft: I will save enough money and sue you', 'Draft: I will save enough money and sue you', 'Draft: You owe me half of your property!']
    ),
    'CHF': (
        210, 120, 
        (30, 33),
        'Inside: Money... enough to fix this house -_-'
    ),
    'WI': (
        213, 208, 
        (29, 20),
        'Ink for writing'
    ),
    'BW': (
        95, 166, 
        (64, 35),
        'Bag of Wheat'
    ),
    'GT': (
        172, 172, 
        (35, 64),
        'Gardening tools: Shovel and Axe '
    ),
    'GC': (
        211, 158, 
        (29, 32),
        'Inside: Empty...'
    ),
    'DK': (
        18, 146, 
        (15, 17),
        'Door Key ...'
    ),
    'SG': (
        216, 88, 
        (19, 20),
        'Birthday Gift'
    ),
    'BCK': (
        216, 60, 
        (32, 22),
        'Party Cake ... looks like someone ate it'
    ),
    'bH': (
        118, 136, 
        (32, 22),
        'Coding 101: by uncle bob'
    ),
    'bF': (
        118, 136, 
        (32, 22),
        'Gardning: be an expert'
    ),
    'LSH': (
        167, 135, 
        (30, 20),
        'Letters from Mr. Ant about the company '
    ),
    'LH': (
        170, 107, 
        (20, 20),
        "Dear Hopper I'll save the company.. I'm smart bussiness man"
    ),
    'END': (
        24, 254, 
        (32, 64),
        "Press Enter to expose the real criminal. No turning back!"
    ),
    'Ant': (
        133, 207, 
        (32, 32),
        ['Ant: Nice day today...', 'Ant: Have you heard the news?', 'Ant: Poor Lady bug', 'Ant: The bank was robbed! can you believe that', 'Ant: Poor Lady bug', 'Ant: Poor Lady bug']
    ),
    'LadyBug': (
        91, 208, 
        (32, 32),
        ['LadyBug: Please help detective', "LadyBug: I didn't do this!", "LadyBug: They'll take me soon ...", 'LadyBug: Please help', 'LadyBug: Who will take care of my kids??']
    ),
    'Fly': (
        93, 235, 
        (30, 30),
        ["Fly: ... get away I'm busy", "Fly: you need something?", "Fly: Private property get out!", "Can't you read? this is private property"]
    ),
    'Hopper': (
        131, 237, 
        (32, 32),
        ['Hopper: Hello detective', 'Hopper: Yestarday was awesome!', 'Hopper: I am an excellent swimmer']
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

#loc_x. loc_y, x, y
character = {
    'Ant': (43, 0, 1500, 228), 
    'LadyBug': (0, 0, 40, 232),
    'Hopper': (132, 0, 92, 1100), 
    'Fly': (86, 0, 1200, 1200),
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
    'AA': (161, 3488), #barrel of apples
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
    'GA': (128, 2562), #gate
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
    'CHH': (130, 3424), #chest
    'BCK': (128, 3903), #bday cake
    0: (14, 12), #width, height
    1: ((96, 2720), (0, 2688)), #wall border (front, side)
    2: (96, 1183), #floor
}

# Hopper
house_2 = {
    'V': (128, 2688), #vertical wall
    'H': (160, 2688), #horizontal wall 
    'CA': (160, 1184), #carpet 
    'Bb': (64, 3104), #bed
    'T': (128, 2816), #table
    'C': (128, 2880), #chair
    'SG': (5, 3965), #small gift
    'LT': (160, 2912), #large table
    'P': (224, 3742), #plant
    'bH': (0, 3808), #book
    'LSH': (63, 3900), #letters
    'LH':(38, 3903), #letter
    0: (10, 7), #width, height
    1: ((224, 2720), (128, 2741)), #wall border (front, side)
    2: (0, 1248), #floor
}

# Ants House
house_3 = {
    'V': (224, 2752), #vertical wall
    'H': (64, 2784), #horizontal wall 
    'BbA': (96, 3104), #bed
    'CA': (128, 1312), #carpet 
    'T': (64, 2976), #table
    'C': (128, 2880), #chair
    'CB': (0, 2912), #cupboard
    'SC': (64, 2938), #small cupboard
    'FU': (0, 3326), #furnace
    'GT': (32, 4192), #guradning tools
    'P': (35, 3995), #plant
    'DK': (234, 4192), #door key
    'K': (96, 3072), #kitchen table
    'KS': (128, 3072), #kitchen sink
    'O': (32, 3040), #oven
    'LT': (160, 3136), #large table
    'LSA': (63, 3900), #letters
    'LA':(38, 3903), #letter
    'LA2':(38, 3903), #letter2
    'GC': (224, 3424), #golden chest
    0: (16, 12), #width, height
    1: ((96, 2752), (224, 2806)), #wall border (front, side)
    2: (160, 1248), #floor
}
# Fly
house_4 = {
    'V': (128, 2688), #vertical wall
    'H': (160, 2688), #horizontal wall 
    'BbF': (32, 3104), #bed
    'CA': (0, 1152), #carpet 
    'T': (128, 2848), #round table
    'C': (128, 2880), #chair
    'BW': (0, 3487), #Wheat
    'CD': (68, 3996), #candle dim
    'LF': (38, 3903), #letter
    'WI': (99, 3903), #writing ink
    'CHF': (130, 3424), #chest
    'bF': (0, 3808), #book
    0: (9, 9), #width, height
    1: ((224, 2720), (128, 2741)), #wall border (front, side)
    2: (0, 1184), #floor
}

# Bank
house_5 = {
    'TT': (2, 3397),
    'CA': (64, 1248),
    'END': (130, 3618),
    0: (8, 10), #width, height
    1: ((96, 2720), (0, 2688)), #wall border (front, side)
    2: (64, 1216), #floor
}