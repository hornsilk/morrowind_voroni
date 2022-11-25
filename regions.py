def check_region(cellX, cellY):
    x = cellX
    y = cellY

    ## Vanilla
    # West_Gash
    if x == -17 and y in range(11,16 +1):
        return 'West_Gash'
    if x == -16 and y in range(10,17 +1):
        return 'West_Gash'
    if x == -15 and y in range(8,17 +1):
        return 'West_Gash'
    if x == -14 and y in range(8,17 +1):
        return 'West_Gash'
    if x == -13 and y in range(6,18 +1):
        return 'West_Gash'
    if x == -12 and y in range(6,20 +1):
        return 'West_Gash'
    if x == -11 and y in range(6,20 +1):
        return 'West_Gash'
    if x == -10 and y in range(6,20 +1):
        return 'West_Gash'
    if x == -9 and y in range(5,20 +1):
        return 'West_Gash'
    if x == -8 and y in range(5,17 +1):
        return 'West_Gash'
    if x == -7 and y in range(5,17 +1):
        return 'West_Gash'
    if x == -6 and y in range(4,14 +1):
        return 'West_Gash'
    if x == -5 and y in range(4,7 +1):
        return 'West_Gash'
    if x == -4 and y in range(0,5 +1):
        return 'West_Gash'
    if x == -4 and y in range(-3,-2 +1):
        return 'West_Gash'
    if x == -3 and y in range(-3,4 +1):
        return 'West_Gash'
    if x == -2 and y in range(-3,4 +1):
        return 'West_Gash'
    if x == -1 and y in range(-3,3 +1):
        return 'West_Gash'
    # Sheogorad
    if x == -8 and y in range(18,22 +1):
        return 'Sheogorad'
    if x == -7 and y in range(18,24 +1):
        return 'Sheogorad'
    if x == -6 and y in range(18,25 +1):
        return 'Sheogorad'
    if x == -5 and y in range(18,27 +1):
        return 'Sheogorad'
    if x in range(-4,0 +1) and y in range(19,27 +1):
        return 'Sheogorad'
    if x == 1 and y in range(18,27 +1):
        return 'Sheogorad'
    if x in range(2,8 +1) and y in range(17,26 +1):
        return 'Sheogorad'
    if x in range(5,7 +1) and y == 16:
        return 'Sheogorad'
    if x == 9 and y in range(20,26 +1):
        return 'Sheogorad'
    if x == 10 and y in range(23,24 +1):
        return 'Sheogorad'
    if x == 11 and y == 23:
        return 'Sheogorad'
    # Ashlands
    if x == -6 and y in range(15,17 +1):
        return 'Ashlands'
    if x == -5 and y in range(8,17 +1):
        return 'Ashlands'
    if x == -4 and y in range(6,18 +1):
        return 'Ashlands'
    if x == -3 and y in range(5,18 +1):
        return 'Ashlands'
    if x == -2 and y in range(11,18 +1): 
        return 'Ashlands'
    if x in range(-1,0 +1) and y in range(12,18 +1):
        return 'Ashlands'
    if x == 1 and y in range(12,17 +1):
        return 'Ashlands'
    if x in range(2,4 +1) and y in range(12,16 +1):
        return 'Ashlands'
    if x == 5 and y in range(11,15 +1): 
        return 'Ashlands'    
    if x == -2 and y in range(5,9 +1): #####
        return 'Ashlands'
    if x == -1 and y in range(4,8 +1):
        return 'Ashlands'
    if x == 0 and y in range(-1,8 +1):
        return 'Ashlands'
    if x == 1 and y in range(-1,4 +1):
        return 'Ashlands'
    if x in range(2,3 +1) and y in range(0,4 +1):
        return 'Ashlands'
    if x == 4 and y in range(1,5 +1):
        return 'Ashlands'
    if x == 5 and y in range(1,7 +1): ####
        return 'Ashlands'
    if x == 6 and y in range(2,15 +1):
        return 'Ashlands'
    if x == 7 and y in range(4,15 +1):
        return 'Ashlands'
    # Red_Mountain (ONLY WORKS BC IT'S AFTER ASHLANDS!)
    if x in range(-2,5 +1) and y in range(5,11 +1):
        return 'Red_Mountain'
    # Bitter_Coast
    if x == -13 and y in range(2,5 +1):
        return 'Bitter_Coast'
    if x == -12 and y in range(1,5 +1):
        return 'Bitter_Coast'
    if x == -11 and y in range(-5,5 +1):
        return 'Bitter_Coast'
    if x == -10 and y in range(-8,5 +1):
        return 'Bitter_Coast'
    if x in range(-9,-8 +1) and y in range(-8,4 +1):
        return 'Bitter_Coast'
    if x == -7 and y in range(-9,4 +1):
        return 'Bitter_Coast'
    if x in range(-6,-5 +1) and y in range(-11,4 +1):
        return 'Bitter_Coast'
    if x == -4 and y == -1:
        return 'Bitter_Coast'
    if x == -4 and y in range(-11,-6 +1):
        return 'Bitter_Coast'
    if x in range(-3,-2 +1) and y in range(-11,-8 +1):
        return 'Bitter_Coast'
    if x == -1 and y in range(-12,-9 +1):
        return 'Bitter_Coast'
    if x == 0 and y in range(-12,-10 +1):
        return 'Bitter_Coast'
    # Ascadian_Isles
    if x == -4 and y in range(-5,-4 +1):
        return 'Ascadian_Isles'
    if x in range(-3,-2 +1) and y in range(-7,-4 +1):
        return 'Ascadian_Isles'
    if x == -1 and y in range(-8,-4 +1):
        return 'Ascadian_Isles'
    if x == 0 and y in range(-9,-4 +1):
        return 'Ascadian_Isles'
    if x == 0 and y in range(-15,-13 +1):
        return 'Ascadian_Isles'
    if x in range(1,3 +1) and y in range(-15,-4 +1):
        return 'Ascadian_Isles'
    if x in range(4,5 +1) and y in range(-15,-5 +1):
        return 'Ascadian_Isles'
    if x == 6 and y in range(-15,-6 +1):
        return 'Ascadian_Isles'
    if x == 7 and y in range(-15,-9 +1):
        return 'Ascadian_Isles'
    if x == 8 and y in range(-12,-11 +1):
        return 'Ascadian_Isles'
    # Grazelands
    if x in range(8,9 +1) and y in range(5,16 +1):
        return 'Grazelands'
    if x in range(10,11 +1) and y in range(5,15 +1):
        return 'Grazelands'
    if x == 12 and y in range(5,12 +1):
        return 'Grazelands'
    if x == 13 and y in range(6,8 +1):
        return 'Grazelands'
    # Azuras_Coast
    if x == 9 and y in range(17,19 +1):
        return 'Azuras_Coast'
    if x in range(10,12 +1) and y in range(16,22 +1):
        return 'Azuras_Coast'
    if x in range(12,13 +1) and y in range(13,18 +1):
        return 'Azuras_Coast'
    if x in range(13,14 +1) and y in range(9,16 +1):
        return 'Azuras_Coast'
    if x == 14 and y in range(6,16 +1):
        return 'Azuras_Coast'
    if x == 15 and y in range(6,14 +1):
        return 'Azuras_Coast'
    if x == 16 and y in range(6,13 +1):
        return 'Azuras_Coast'
    if x == 17 and y in range(6,12 +1):
        return 'Azuras_Coast'
    if x == 18 and y in range(6,12 +1):
        return 'Azuras_Coast'
    if x == 19 and y in range(6,11 +1):
        return 'Azuras_Coast'
    if x == 20 and y in range(6,10 +1):
        return 'Azuras_Coast'
    if x == 21 and y in range(6,7 +1):
        return 'Azuras_Coast'
    if x in range(13,21 +1) and y == 5:
        return 'Azuras_Coast'
    if x in range(11,21 +1) and y == 4:
        return 'Azuras_Coast'
    if x in range(12,22 +1) and y == 3:
        return 'Azuras_Coast'
    if x in range(13,22 +1) and y == 2:
        return 'Azuras_Coast'
    if x in range(14,22 +1) and y == 1:
        return 'Azuras_Coast'
    if x in range(15,22 +1) and y == 0:
        return 'Azuras_Coast'
    if x in range(16,20 +1) and y in range(-3,-1 +1):
        return 'Azuras_Coast'
    if x in range(16,21 +1) and y in range(-7,-4 +1):
        return 'Azuras_Coast'
    if x in range(14,21 +1) and y == -8:
        return 'Azuras_Coast'
    if x in range(9,11 +1) and y == -8:
        return 'Azuras_Coast'
    if x in range(8,21 +1) and y == -9:
        return 'Azuras_Coast'
    if x in range(8,19 +1) and y == -10:
        return 'Azuras_Coast'
    if x in range(9,19 +1) and y == -11:
        return 'Azuras_Coast'
    if x in range(9,17 +1) and y == -12:
        return 'Azuras_Coast'
    if x in range(8,17 +1) and y == -13:
        return 'Azuras_Coast'
    if x in range(8,17 +1) and y == -14:
        return 'Azuras_Coast'
    if x in range(8,16 +1) and y == -15:
        return 'Azuras_Coast'
    # Molag_Amur (ONLY WORKS BC LAST VANILLA REGION)
    if x in range(0,15 +1) and y in range(-8,4 +1):
        return 'Molag_Amur'


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


    return 'unknown'


def isReleased(region_name, mod_list):
    game_regions = []

    # Add vanilla regions
    game_regions += ['West_Gash','Sheogorad','Ashlands','Red_Mountain','Bitter_Coast','Ascadian_Isles','Grazelands','Azuras_Coast','Molag_Amur']


    ## Add expansion regions
    if 'Anthology_Solstheim' in mod_list:
        game_regions += ['Moespring_Mountains','Felsaad_Coast','Isinfier_Plains','Hirstaang_Forest']
    # elif 'Bloodmoon' in mod_list:
    #     game_regions.append('Vanilla_Solstheim')
    # if 'Tribunal' in mod_list:
    #     game_regions.append('Mournhold')



    tr_released_regions = []


    if region_name in game_regions:
        return True
    elif region_name in tr_released_regions:
        return True

    else:
        return False
