world_map = [
    ['LTE', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'L.', 'WF', 'WF', 'WF', 'R.', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F','RTE'],
    ['VE' , '.', '.', '.', '.', '.', '.', '.', '.', 'L.', 'W', 'W', 'W', 'R.', '.', '.', 'T', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.','VE'],
    ['VE' , '.', '.', '.', '.', '.', 'FW', '.', '.', 'L.', 'W', 'W', 'W', 'R.', '.', '.', '.', 'FW', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.','VE'],
    ['VE' , '.', 'T', '.', '.', '.', '.', '.', '.', '.', 'LT.', 'W', 'RT.', '.', '.T', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.','VE'],
    ['VE' , '.', '.', '.', '.', '.', '.', '.', '.', '.', 'SB', 'W', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'VE'],
    ['VE' , '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'VE'],
    ['VE' , '.', '.', '.', '.', '.', '.', '.', '.', 'FM', '.', 'W', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B.', 'B.'],
    ['VE' , '.', '.', '.', '.', '.', '.', 'ST', '.', '.', 'LB.', 'W', 'RB.', '.', '.', '.', 'ST', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'LB.', 'W','W'],
    ['VE' , '.', '.', '.', '.', '.', '.', '.', '.', 'LB.', 'W', 'W', 'W', 'RB.', '.', '.', '.', '.', 'FM', 'T', '.', '.', '.', '.', '.', '.', '.', 'B.', 'LB.', 'W', 'W','W'],
    ['VE' , '.', '.', '.', '.', '.', '.', '.', 'L.', 'W', 'W', 'W', 'W', 'W', 'RB.', '.', '.', 'FM', '.', '.', '.', '.', 'FW', 'FT', '.', 'B.', 'LB.', 'W', 'W', 'W', 'W','W'],
    ['VE' , '.', 'FM', '.', 'FW', '.', '.', '.', 'LB.', 'W', 'W', 'W', 'W', 'W', 'W', 'RB.', '.', '.', '.', '.', 'FW', '.', '.', '.', 'L.', 'W',  'W', 'W', 'W', 'W', 'W','W'],
    ['VE' , '.', '.', 'T', '.', '.', '.', 'LB.', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'R.', '.', '.', '.', '.', '.', 'B.', 'B.', 'LB.', 'W', 'W', 'W', 'W', 'W', 'W','W'],
    ['VE' , '.', '.', '.', 'FW', '.', 'L.', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'RB.', '.', '.', '.', '.', 'LB.', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W','W'],
    ['B.', 'B.', 'B.', '.', '.', '.', 'LB.', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'RB.', 'B.', 'B.', 'LB.', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'RT.', 'T.', 'T.','T.'],
    ['W' , 'W', 'W', 'R.', '.', 'L.', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'R.', '.', '.','.'],
    ['W' , 'W', 'W', 'FB', '.', 'B.', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'R.', '.', '.','.'],
    ['W' , 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'RT.', 'T.', '.', '.', 'T','.'],
    ['W' , 'W', 'W', 'R.', '.', 'L.', 'W', 'W', 'W', 'W', 'W', 'W', 'RT.', 'T.', 'LT.', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'RT.', '.', '.', '.', '.', '.','VE'],
    ['W' , 'W', 'W', 'R.', '.', 'L.', 'W', 'W', 'T.', 'T.', 'T.', 'T.', '.', '.', '.', 'LT.', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'RT.', '.', '.', '.', '.', '.', '.','VE'],
    ['T.', 'T.', 'T.', '.', ',', '.', 'T.', 'T.', '.', '.', '.', '.', '.', '.', '.', '.', 'LT.', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'R.', '.', '.', '.', '.', '.', '.','VE'],
    ['VE' , '.', 'FM', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'T.', 'T.', 'T.', 'LT.', 'W', 'RT.', 'T.', '.', '.', '.', '.', '.', '.', '.','VE'],
    ['VE' , '.', '.', '.', '.', '.', 'T', '.', '.', '.', '.', 'FW', '.', '.', '.', '.', '.', '.', '.', '.', 'L.', 'W', 'R.', '.', '.', '.', '.', '.', '.', '.', '.','VE'],
    ['VE' , '.', '.', '.', 'FM', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'SB', 'W', '.', '.', 'FW', '.', '.', '.', '.', '.', '.','VE'],
    ['VE' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'VE'],
    ['VE' , '.', '.', 'ST', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'LB.', 'W', 'RB.', '.', '.', '.', '.', '.', '.', '.', '.','VE'],
    ['VE' , '.', '.', '.', '.', '.', 'FW', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'T', '.', '.', 'LB.', 'W', 'W', 'W', 'RB.', 'FM', '.', '.', '.', '.', '.', '.','VE'],
    ['VE' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'FW', '.', '.', '.', 'L.', 'W', 'W', 'W', 'W', 'W', 'R.', '.', 'FT', '.', '.', 'FM', '.','VE'],
    ['VE' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'L.', 'W', 'W', 'W', 'W', 'W', 'R.', '.', '.', '.', '.', '.', '.','VE'],
    ['LBE', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'L.', 'WU', 'WU', 'WU', 'WU', 'WU', 'R.', 'F', 'F', 'F', 'F', 'F', 'F', 'RBE'],
]

house1 = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

house2 = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

house3 = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

house4 = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

house5 = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]