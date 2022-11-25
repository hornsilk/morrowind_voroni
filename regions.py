def check_region(cellX, cellY):
    x = cellX
    y = cellY

    ## Solstheim
    # Moespring_Mountains
    if x == -21 and y == 29:
        return 'Moespring_Mountains'
    if x == -20 and y in range(29,33 +1):
        return 'Moespring_Mountains'
    if x == -19 and y in range(29,34 +1):
        return 'Moespring_Mountains'
    if x == -18 and y in range(30,34 +1):
        return 'Moespring_Mountains'
    if x == -17 and y in range(30,33 +1):
        return 'Moespring_Mountains'
    if x in range(-16,-15 +1) and y in range(31,33 +1):
        return 'Moespring_Mountains'
    # Felsaad_Coast
    if x in range(-14,-13 +1) and y in range(29,33 +1):
        return 'Felsaad_Coast'
    if x in range(-12,-11 +1) and y in range(28,34 +1):
        return 'Felsaad_Coast'
    if x == -10 and y in range(28,32 +1):
        return 'Felsaad_Coast'
    # Isinfier_Plains
    if x in range(-21,-19 +1) and y in range(27,28 +1):
        return 'Isinfier_Plains'
    if x in range(-18,-17 +1) and y in range(27,29 +1):
        return 'Isinfier_Plains'
    if x == -16 and y in range(27,30 +1):
        return 'Isinfier_Plains'
    if x == -15 and y in range(26,30 +1):
        return 'Isinfier_Plains'
    if x in range(-14,-13 +1) and y in range(25,28 +1):
        return 'Isinfier_Plains'
    if x in range(-12,-10 +1) and y in range(25,27 +1):
        return 'Isinfier_Plains'
    # Hirstaang_Forest
    if x == -20 and y in range(25,26 +1):
        return 'Hirstaang_Forest'
    if x == -19 and y in range(23,26 +1):
        return 'Hirstaang_Forest'
    if x in range(-18,-16 +1) and y in range(21,26 +1):
        return 'Hirstaang_Forest'
    if x == -15 and y in range(21,25 +1):
        return 'Hirstaang_Forest'
    if x == -14 and y in range(21,24 +1):
        return 'Hirstaang_Forest'
    if x in range(-13,-11 +1) and y in range(22,24 +1):
        return 'Hirstaang_Forest'
    if x == -10 and y in range(23,24 +1):
        return 'Hirstaang_Forest'

    # # Vvardenfell
    # if x in range(-9,13 +1) and y in range(-6,19 +1):
    #     return 'Vvardenfell'
    
    # if x in range(-8,-6 +1) and y == 20:
    #     return 'Vvardenfell'
    # if x in range(-6,13 +1) and y in range(20,21 +1):
    #     return 'Vvardenfell'
    # if x in range(-6,12 +1) and y == 22:
    #     return 'Vvardenfell'
    # if x in range(-6,10 +1) and y == 23:
    #     return 'Vvardenfell'
    # if x in range(-6,9 +1) and y == 24:
    #     return 'Vvardenfell'
    # if x in range(-5,8 +1) and y == 25:
    #     return 'Vvardenfell'
    # if x == -10 and y in range(-7,19 +1):
    #     return 'Vvardenfell'
    # if x == -11 and y in range(-4,19 +1):
    #     return 'Vvardenfell'
    # if x == -12 and y in range(1,17 +1):
    #     return 'Vvardenfell'
    # if x == -13 and y in range(4,17 +1):
    #     return 'Vvardenfell'
    # if x == -14 and y in range(7,16 +1):
    #     return 'Vvardenfell'
    # if x == -15 and y in range(9,16 +1):
    #     return 'Vvardenfell'
    # if x == -16 and y in range(10,16 +1):
    #     return 'Vvardenfell'
    # if x == -17 and y in range(11,15 +1):
    #     return 'Vvardenfell'

    return 'unknown'


def isReleased(region_name, mod_list):
    game_regions = []

    if 'Tribunal' in mod_list:
        game_regions.append('Mournhold')

    
    if 'Anthology_Solstheim' in mod_list:
        game_regions += ['Moespring_Mountains','Felsaad_Coast','Isinfier_Plains','Hirstaang_Forest']
    # elif 'Bloodmoon' in mod_list:
    #     game_regions.append('Vanilla_Solstheim')



    tr_released_regions = []


    if region_name in game_regions:
        return True
    elif region_name in tr_released_regions:
        return True

    else:
        return False
