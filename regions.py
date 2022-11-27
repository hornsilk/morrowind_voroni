import json

vanilla_regions = ['West_Gash','Sheogorad','Ashlands','Red_Mountain','Bitter_Coast','Ascadian_Isles','Grazelands','Azuras_Coast','Molag_Amur']
solstheim_regions = ['Moespring_Mountains','Felsaad_Coast','Isinfier_Plains','Hirstaang_Forest']
tr_released_regions = ['Sea_of_Ghosts_E','Dagon_Urul','Molagreahd','Telvanni_Isles','Boethiahs_Spine','Molag_Ruhn','Mephalan_Vales','Sacred_Lands','Sundered_Scar','Lan_Orethan','Nedothril','Padomaic_Ocean_N','Aanthirin','Armun_Ashlands','Roth_Roryn','Velothi_Mountains_E','Alt_Orethan']
tr_unreleased_regions = ['Sea_of_Ghosts_W','Padomaic_Ocean_S','Almalexia','Amber_Forest','Deshaan_Plains','Mudflats','Salt_Washes','Arnesian_Basin','Velothi_Mountains_W','Coronati_Basin','Othreleth_Woods','Shipal_Shin','Clambering_Moor','Grey_Meadows','Julan_Shar','Uld_Vraech']

def check_region(cellX, cellY, region_lookup_dict):
    x = cellX
    y = cellY
    if f'{x}_{y}' not in region_lookup_dict:
        return 'unknown'

    region = region_lookup_dict[f'{x}_{y}']
    return region


def check_region_hardcoded(cellX, cellY):
    x = cellX
    y = cellY

    ## Vanilla
    # West_Gash
    if x == -17 and y in range(11,16 +1): return 'West_Gash'
    if x == -16 and y in range(10,17 +1): return 'West_Gash'
    if x == -15 and y in range(8,17 +1): return 'West_Gash'
    if x == -14 and y in range(8,17 +1): return 'West_Gash'
    if x == -13 and y in range(6,18 +1): return 'West_Gash'
    if x == -12 and y in range(6,20 +1): return 'West_Gash'
    if x == -11 and y in range(6,20 +1): return 'West_Gash'
    if x == -10 and y in range(6,20 +1): return 'West_Gash'
    if x == -9 and y in range(5,20 +1): return 'West_Gash'
    if x == -8 and y in range(5,17 +1): return 'West_Gash'
    if x == -7 and y in range(5,17 +1): return 'West_Gash'
    if x == -6 and y in range(4,14 +1): return 'West_Gash'
    if x == -5 and y in range(4,7 +1): return 'West_Gash'
    if x == -4 and y in range(0,5 +1): return 'West_Gash'
    if x == -4 and y in range(-3,-2 +1): return 'West_Gash'
    if x == -3 and y in range(-3,4 +1): return 'West_Gash'
    if x == -2 and y in range(-3,4 +1): return 'West_Gash'
    if x == -1 and y in range(-3,3 +1): return 'West_Gash'
    # Sheogorad
    if x == -8 and y in range(18,22 +1): return 'Sheogorad'
    if x == -7 and y in range(18,24 +1): return 'Sheogorad'
    if x == -6 and y in range(18,25 +1): return 'Sheogorad'
    if x == -5 and y in range(18,27 +1): return 'Sheogorad'
    if x in range(-4,0 +1) and y in range(19,27 +1): return 'Sheogorad'
    if x == 1 and y in range(18,27 +1): return 'Sheogorad'
    if x in range(2,8 +1) and y in range(17,26 +1): return 'Sheogorad'
    if x in range(5,7 +1) and y == 16: return 'Sheogorad'
    if x == 9 and y in range(20,26 +1): return 'Sheogorad'
    if x == 10 and y in range(23,24 +1): return 'Sheogorad'
    if x == 11 and y == 23: return 'Sheogorad'
    # Ashlands
    if x == -6 and y in range(15,17 +1): return 'Ashlands'
    if x == -5 and y in range(8,17 +1): return 'Ashlands'
    if x == -4 and y in range(6,18 +1): return 'Ashlands'
    if x == -3 and y in range(5,18 +1): return 'Ashlands'
    if x == -2 and y in range(11,18 +1): return 'Ashlands'
    if x in range(-1,0 +1) and y in range(12,18 +1): return 'Ashlands'
    if x == 1 and y in range(12,17 +1): return 'Ashlands'
    if x in range(2,4 +1) and y in range(12,16 +1): return 'Ashlands'
    if x == 5 and y in range(11,15 +1): return 'Ashlands'    
    if x == -2 and y in range(5,9 +1): return 'Ashlands'
    if x == -1 and y in range(4,8 +1): return 'Ashlands'
    if x == 0 and y in range(-1,8 +1): return 'Ashlands'
    if x == 1 and y in range(-1,4 +1): return 'Ashlands'
    if x in range(2,3 +1) and y in range(0,4 +1): return 'Ashlands'
    if x == 4 and y in range(1,5 +1): return 'Ashlands'
    if x == 5 and y in range(1,7 +1): return 'Ashlands'
    if x == 6 and y in range(2,15 +1): return 'Ashlands'
    if x == 7 and y in range(4,15 +1): return 'Ashlands'
    # Red_Mountain (ONLY WORKS BC IT'S AFTER ASHLANDS!)
    if x in range(-2,5 +1) and y in range(5,11 +1): return 'Red_Mountain'
    # Bitter_Coast
    if x == -13 and y in range(2,5 +1): return 'Bitter_Coast'
    if x == -12 and y in range(1,5 +1): return 'Bitter_Coast'
    if x == -11 and y in range(-5,5 +1): return 'Bitter_Coast'
    if x == -10 and y in range(-8,5 +1): return 'Bitter_Coast'
    if x in range(-9,-8 +1) and y in range(-8,4 +1): return 'Bitter_Coast'
    if x == -7 and y in range(-9,4 +1): return 'Bitter_Coast'
    if x in range(-6,-5 +1) and y in range(-11,4 +1): return 'Bitter_Coast'
    if x == -4 and y == -1: return 'Bitter_Coast'
    if x == -4 and y in range(-11,-6 +1): return 'Bitter_Coast'
    if x in range(-3,-2 +1) and y in range(-11,-8 +1): return 'Bitter_Coast'
    if x == -1 and y in range(-12,-9 +1): return 'Bitter_Coast'
    if x == 0 and y in range(-12,-10 +1): return 'Bitter_Coast'
    # Ascadian_Isles
    if x == -4 and y in range(-5,-4 +1): return 'Ascadian_Isles'
    if x in range(-3,-2 +1) and y in range(-7,-4 +1): return 'Ascadian_Isles'
    if x == -1 and y in range(-8,-4 +1): return 'Ascadian_Isles'
    if x == 0 and y in range(-9,-4 +1): return 'Ascadian_Isles'
    if x == 0 and y in range(-15,-13 +1): return 'Ascadian_Isles'
    if x in range(1,3 +1) and y in range(-15,-4 +1): return 'Ascadian_Isles'
    if x in range(4,5 +1) and y in range(-15,-5 +1): return 'Ascadian_Isles'
    if x == 6 and y in range(-15,-6 +1): return 'Ascadian_Isles'
    if x == 7 and y in range(-15,-9 +1): return 'Ascadian_Isles'
    if x == 8 and y in range(-12,-11 +1): return 'Ascadian_Isles'
    # Grazelands
    if x in range(8,9 +1) and y in range(5,16 +1): return 'Grazelands'
    if x in range(10,11 +1) and y in range(5,15 +1): return 'Grazelands'
    if x == 12 and y in range(5,12 +1): return 'Grazelands'
    if x == 13 and y in range(6,8 +1): return 'Grazelands'
    # Azuras_Coast
    if x == 9 and y in range(17,19 +1): return 'Azuras_Coast'
    if x in range(10,12 +1) and y in range(16,22 +1): return 'Azuras_Coast'
    if x in range(12,13 +1) and y in range(13,18 +1): return 'Azuras_Coast'
    if x in range(13,14 +1) and y in range(9,16 +1): return 'Azuras_Coast'
    if x == 14 and y in range(6,16 +1): return 'Azuras_Coast'
    if x == 15 and y in range(6,14 +1): return 'Azuras_Coast'
    if x == 16 and y in range(6,13 +1): return 'Azuras_Coast'
    if x == 17 and y in range(6,12 +1): return 'Azuras_Coast'
    if x == 18 and y in range(6,12 +1): return 'Azuras_Coast'
    if x == 19 and y in range(6,11 +1): return 'Azuras_Coast'
    if x == 20 and y in range(6,10 +1): return 'Azuras_Coast'
    if x == 21 and y in range(6,7 +1): return 'Azuras_Coast'
    if x in range(13,21 +1) and y == 5: return 'Azuras_Coast'
    if x in range(11,21 +1) and y == 4: return 'Azuras_Coast'
    if x in range(12,22 +1) and y == 3: return 'Azuras_Coast'
    if x in range(13,22 +1) and y == 2: return 'Azuras_Coast'
    if x in range(14,22 +1) and y == 1: return 'Azuras_Coast'
    if x in range(15,22 +1) and y == 0: return 'Azuras_Coast'
    if x in range(16,20 +1) and y in range(-3,-1 +1): return 'Azuras_Coast'
    if x in range(16,21 +1) and y in range(-7,-4 +1): return 'Azuras_Coast'
    if x in range(14,21 +1) and y == -8: return 'Azuras_Coast'
    if x in range(9,11 +1) and y == -8: return 'Azuras_Coast'
    if x in range(8,21 +1) and y == -9: return 'Azuras_Coast'
    if x in range(8,19 +1) and y == -10: return 'Azuras_Coast'
    if x in range(9,19 +1) and y == -11: return 'Azuras_Coast'
    if x in range(9,17 +1) and y == -12: return 'Azuras_Coast'
    if x in range(8,17 +1) and y == -13: return 'Azuras_Coast'
    if x in range(8,17 +1) and y == -14: return 'Azuras_Coast'
    if x in range(8,16 +1) and y == -15: return 'Azuras_Coast'
    # Molag_Amur (ONLY WORKS BC LAST VANILLA REGION)
    if x in range(0,15 +1) and y in range(-8,4 +1): return 'Molag_Amur'


    ## Anthology Solstheim 
    # Moespring_Mountains
    if x == -21 and y == 29: return 'Moespring_Mountains'
    if x == -20 and y in range(29,33 +1): return 'Moespring_Mountains'
    if x == -19 and y in range(29,34 +1): return 'Moespring_Mountains'
    if x == -18 and y in range(30,34 +1): return 'Moespring_Mountains'
    if x == -17 and y in range(30,33 +1): return 'Moespring_Mountains'
    if x in range(-16,-15 +1) and y in range(31,33 +1): return 'Moespring_Mountains'
    # Felsaad_Coast
    if x in range(-14,-13 +1) and y in range(29,33 +1): return 'Felsaad_Coast'
    if x in range(-12,-11 +1) and y in range(28,34 +1): return 'Felsaad_Coast'
    if x == -10 and y in range(28,32 +1): return 'Felsaad_Coast'
    # Isinfier_Plains
    if x in range(-21,-19 +1) and y in range(27,28 +1): return 'Isinfier_Plains'
    if x in range(-18,-17 +1) and y in range(27,29 +1): return 'Isinfier_Plains'
    if x == -16 and y in range(27,30 +1): return 'Isinfier_Plains'
    if x == -15 and y in range(26,30 +1): return 'Isinfier_Plains'
    if x in range(-14,-13 +1) and y in range(25,28 +1): return 'Isinfier_Plains'
    if x in range(-12,-10 +1) and y in range(25,27 +1): return 'Isinfier_Plains'
    # Hirstaang_Forest
    if x == -20 and y in range(25,26 +1): return 'Hirstaang_Forest'
    if x == -19 and y in range(23,26 +1): return 'Hirstaang_Forest'
    if x in range(-18,-16 +1) and y in range(21,26 +1): return 'Hirstaang_Forest'
    if x == -15 and y in range(21,25 +1): return 'Hirstaang_Forest'
    if x == -14 and y in range(21,24 +1): return 'Hirstaang_Forest'
    if x in range(-13,-11 +1) and y in range(22,24 +1): return 'Hirstaang_Forest'
    if x == -10 and y in range(23,24 +1): return 'Hirstaang_Forest'

    ## TR_Mainland (released)
    # Sea_of_Ghosts_E
    if x == 10 and y in range(25,29 +1): return 'Sea_of_Ghosts_E'
    if x == 11 and y in range(24,29 +1): return 'Sea_of_Ghosts_E'
    if x == 12 and y in range(23,29 +1): return 'Sea_of_Ghosts_E'
    if x in range(13,18 +1) and y in range(21,29 +1): return 'Sea_of_Ghosts_E'
    if x == 19 and y in range(23,29 +1): return 'Sea_of_Ghosts_E'
    # if x == 19 and y in range(30,32 +1): return 'Sea_of_Ghosts_E'
    if x == 20 and y in range(23,29 +1): return 'Sea_of_Ghosts_E'
    # if x == 20 and y in range(30,33 +1): return 'Sea_of_Ghosts_E'
    # if x in range(21,22 +1) and y in range(29,33 +1): return 'Sea_of_Ghosts_E'
    if x == 21 and y in range(23,24 +1): return 'Sea_of_Ghosts_E'
    if x == 22 and y in range(22,24 +1): return 'Sea_of_Ghosts_E'
    if x == 23 and y in range(21,24 +1): return 'Sea_of_Ghosts_E'
    if x == 24 and y in range(21,23 +1): return 'Sea_of_Ghosts_E'
    if x in range(25,26 +1) and y in range(22,23 +1): return 'Sea_of_Ghosts_E'
    if x == 27 and y in range(21,23 +1): return 'Sea_of_Ghosts_E'
    if x == 28 and y in range(20,23 +1): return 'Sea_of_Ghosts_E'
    if x in range(29,30 +1) and y in range(19,23 +1): return 'Sea_of_Ghosts_E'
    if x == 31 and y in range(22,23 +1): return 'Sea_of_Ghosts_E'
    if x in range(32,40 +1) and y == 22: return 'Sea_of_Ghosts_E'
    if x in range(36,39 +1) and y == 21: return 'Sea_of_Ghosts_E'
    if x in range(37,38 +1) and y == 20: return 'Sea_of_Ghosts_E'
    # Molagreahd
    if x == 19 and y in range(19,22 +1): return 'Molagreahd'
    if x == 20 and y in range(17,22 +1): return 'Molagreahd'
    if x == 21 and y in range(16,22 +1): return 'Molagreahd'
    if x == 22 and y in range(13,21 +1): return 'Molagreahd'
    if x == 23 and y in range(12,20 +1): return 'Molagreahd'
    if x == 24 and y in range(11,20 +1): return 'Molagreahd'
    if x == 25 and y in range(10,21 +1): return 'Molagreahd'
    if x == 26 and y in range(8,21 +1): return 'Molagreahd'
    if x == 27 and y in range(6,20 +1): return 'Molagreahd'
    if x == 28 and y in range(6,19 +1): return 'Molagreahd'
    if x == 29 and y in range(5,18 +1): return 'Molagreahd'
    if x == 30 and y in range(5,16 +1): return 'Molagreahd'
    if x == 31 and y in range(5,15 +1): return 'Molagreahd'
    if x == 32 and y in range(5,15 +1): return 'Molagreahd'
    if x == 33 and y in range(5,15 +1): return 'Molagreahd'
    if x == 34 and y in range(5,15 +1): return 'Molagreahd'
    if x == 35 and y in range(6,13 +1): return 'Molagreahd'
    if x == 36 and y in range(6,10 +1): return 'Molagreahd'
    if x == 37 and y in range(7,8 +1): return 'Molagreahd'
    # Telvanni_Isles (must be after Molagreahd and Sea_of_Ghosts_E)
    if x in range(30,40 +1) and y in range(14,22 +1): return 'Telvanni_Isles'
    if x in range(41,46 +1) and y in range(12,22 +1): return 'Telvanni_Isles'
    if x in range(47,48 +1) and y in range(13,22 +1): return 'Telvanni_Isles'
    # if x == 49 and y in range(13,22 +1): return 'Telvanni_Isles'
    if x in range(42,44 +1) and y in range(10,11 +1): return 'Telvanni_Isles'
    if x == 45 and y == 11: return 'Telvanni_Isles'
    # if x in range(53,56 +1) and y in range(13,17 +1): return 'Telvanni_Isles'
    # if x == 57 and y in range(14,16 +1): return 'Telvanni_Isles'
    # if x in range(54,56 +1) and y == 18: return 'Telvanni_Isles'
    # Dagon_Urul
    if x in range(13,26 +1) and y in range(6,20 +1): return 'Dagon_Urul'
    if x == 22 and y in range(4,5 +1): return 'Dagon_Urul'
    if x in range(23,24 +1) and y in range(0,5 +1): return 'Dagon_Urul'
    if x == 25 and y in range(1,3 +1): return 'Dagon_Urul'
    if x == 26 and y in range(2,3 +1): return 'Dagon_Urul'
    # Boethiahs_Spine
    if x in range(25,26 +1) and y in range(4,5 +1): return 'Boethiahs_Spine'
    if x in range(27,28 +1) and y in range(3,5 +1): return 'Boethiahs_Spine'
    if x == 29 and y in range(-3,4 +1): return 'Boethiahs_Spine'
    if x == 30 and y in range(-4,4 +1): return 'Boethiahs_Spine'
    if x == 31 and y in range(-5,4 +1): return 'Boethiahs_Spine'
    if x == 32 and y in range(-5,4 +1): return 'Boethiahs_Spine'
    if x == 33 and y in range(-5,4 +1): return 'Boethiahs_Spine'
    if x == 34 and y in range(-5,4 +1): return 'Boethiahs_Spine'
    if x == 35 and y in range(-5,5 +1): return 'Boethiahs_Spine'
    if x == 36 and y in range(-5,5 +1): return 'Boethiahs_Spine'
    if x == 37 and y in range(-5,2 +1): return 'Boethiahs_Spine'
    if x == 38 and y in range(-5,0 +1): return 'Boethiahs_Spine'
    if x == 39 and y in range(-5,-3 +1): return 'Boethiahs_Spine'
    if x == 40 and y in range(-5,-4 +1): return 'Boethiahs_Spine'
    # Padomaic_Ocean_N (-31 lowest cell)
    if x == 39 and y == 13: return 'Padomaic_Ocean_N'
    if x == 40 and y in range(11,13 +1): return 'Padomaic_Ocean_N'
    if x == 41 and y in range(10,11 +1): return 'Padomaic_Ocean_N'
    if x in range(36,38 +1) and y in range(8,13 +1): return 'Padomaic_Ocean_N'
    if x in range(37,40 +1) and y in range(-3,7 +1): return 'Padomaic_Ocean_N'
    if x in range(41,44 +1) and y in range(-5,-3 +1): return 'Padomaic_Ocean_N'
    if x in range(41,45 +1) and y in range(-6,-5 +1): return 'Padomaic_Ocean_N'
    if x in range(41,42 +1) and y == -7: return 'Padomaic_Ocean_N'
    if x in range(45,47 +1) and y == -7: return 'Padomaic_Ocean_N'
    if x in range(46,47 +1) and y == -8: return 'Padomaic_Ocean_N'
    if x in range(46,47 +1) and y == -9: return 'Padomaic_Ocean_N'
    if x in range(47,48 +1) and y == -10: return 'Padomaic_Ocean_N'
    if x == 48 and y in range(-14,-11 +1): return 'Padomaic_Ocean_N'
    if x in range(47,48 +1) and y == -18: return 'Padomaic_Ocean_N'
    if x in range(41,44 +1) and y in range(-18,-17 +1): return 'Padomaic_Ocean_N'
    if x in range(40,45 +1) and y in range(-20,-19 +1): return 'Padomaic_Ocean_N'
    if x == 40 and y in range(-26,-21 +1): return 'Padomaic_Ocean_N'
    if x == 39 and y in range(-26,-24 +1): return 'Padomaic_Ocean_N'
    if x in range(39,42 +1) and y in range(-31,-27 +1): return 'Padomaic_Ocean_N'
    # Molag_Ruhn
    if x in range(24,32 +1) and y in range(-7,2 +1): return 'Molag_Ruhn'
    if x in range(21,23 +1) and y in range(-4,-1 +1): return 'Molag_Ruhn'
    if x in range(31,32 +1) and y in range(-9,-8 +1): return 'Molag_Ruhn'
    # Mephalan_Vales
    if x in range(22,40 +1) and y in range(-9,-5 +1): return 'Mephalan_Vales'
    if x in range(24,35 +1) and y == -10: return 'Mephalan_Vales'
    if x in range(25,35 +1) and y in range(-12,-11 +1): return 'Mephalan_Vales'
    if x in range(25,32 +1) and y in range(-14,-13 +1): return 'Mephalan_Vales'
    if x in range(28,32 +1) and y in range(-18,-15 +1): return 'Mephalan_Vales'
    if x in range(29,30 +1) and y == -19: return 'Mephalan_Vales'
    if x in range(33,36 +1) and y in range(-18,-16 +1): return 'Mephalan_Vales'
    if x in range(34,36 +1) and y == -19: return 'Mephalan_Vales'
    if x in range(34,35 +1) and y == -20: return 'Mephalan_Vales'
    # Lan_Orethan
    if x in range(31,33 +1) and y in range(-31,-19 +1): return 'Lan_Orethan'
    if x in range(29,30 +1) and y in range(-31,-20 +1): return 'Lan_Orethan'
    if x in range(27,28 +1) and y in range(-31,-29 +1): return 'Lan_Orethan'
    if x == 28 and y == -28: return 'Lan_Orethan'
    if x == 34 and y in range(-31,-28 +1): return 'Lan_Orethan'
    if x == 35 and y in range(-31,-29 +1): return 'Lan_Orethan'
    if x == 36 and y in range(-31,-30 +1): return 'Lan_Orethan'
    # Sacred_Lands
    if x in range(33,45 +1) and y in range(-19,-7 +1): return 'Sacred_Lands'
    if x in range(46,48 +1) and y in range(-18,-10 +1): return 'Sacred_Lands'
    # Nedothril
    if x in range(34,39 +1) and y in range(-31,-20 +1): return 'Nedothril'
    # Alt_Orethan
    if x in range(27,28 +1) and y in range(-28,-22 +1): return 'Alt_Orethan'
    if x in range(19,26 +1) and y in range(-23,-22 +1): return 'Alt_Orethan'
    if x ==14 and y == -32: return 'Alt_Orethan'
    # Sundered_Scar
    if x in range(14,18 +1) and y in range(-23,-22 +1): return 'Sundered_Scar'
    if x ==13 and y == -22: return 'Sundered_Scar'
    if x in range(13,28 +1) and y in range(-21,-10 +1): return 'Sundered_Scar'
    if x ==12 and y in range(-20,-16 +1): return 'Sundered_Scar'
    if x ==11 and y in range(-18,-16 +1): return 'Sundered_Scar'
    if x ==10 and y in range(-18,-16 +1): return 'Sundered_Scar'
    if x ==9 and y in range(-17,-16 +1): return 'Sundered_Scar'
    # Aanthirin
    if x in range(7,13 +1) and y == -34: return 'Aanthirin'
    if x in range(6,13 +1) and y in range(-33,-32 +1): return 'Aanthirin'
    if x in range(0,13 +1) and y in range(-31,-23 +1): return 'Aanthirin'
    if x in range(1,12 +1) and y in range(-22,-20 +1): return 'Aanthirin'
    if x in range(3,11 +1) and y in range(-19,-16 +1): return 'Aanthirin'
    if x == 2 and y in range(-17,-16 +1): return 'Aanthirin'
    # Armun_Ashlands
    if x in range(-9,-6 +1) and y ==-31: return 'Armun_Ashlands'
    if x in range(-10,-1 +1) and y in range(-30,-23 +1): return 'Armun_Ashlands'
    if x in range(-10,-3 +1) and y == -22: return 'Armun_Ashlands'
    if x in range(-13,-11 +1) and y in range(-28,-23 +1): return 'Armun_Ashlands'
    if x in range(-14,-13 +1) and y in range(-27,-22 +1): return 'Armun_Ashlands'
    if x == -15 and y in range(-25,-21 +1): return 'Armun_Ashlands'
    # Roth_Roryn
    if x == -15 and y in range(-20,-18 +1): return 'Roth_Roryn'
    if x in range(-14,2 +1) and y in range(-22,-15 +1): return 'Roth_Roryn'
    if x in range(-8,-1 +1) and y in range(-14,-9 +1): return 'Roth_Roryn'
    if x ==-9 and y in range(-11,-9 +1): return 'Roth_Roryn'
    # Velothi_Mountains_E
    if x in range(-16,-15 +1) and y in range(-16,-15 +1): return 'Velothi_Mountains_E'
    if x in range(-18,-15 +1) and y == -17: return 'Velothi_Mountains_E'
    if x in range(-18,-16 +1) and y in range(-26,-18 +1): return 'Velothi_Mountains_E'
    if x == -19 and y in range(-26,-20 +1): return 'Velothi_Mountains_E'
    if x == -20 and y in range(-26,-21 +1): return 'Velothi_Mountains_E'
    if x == -21 and y in range(-25,-22 +1): return 'Velothi_Mountains_E'
    if x == -15 and y == -26: return 'Velothi_Mountains_E'


    return 'unknown'

def check_region_vanilla_solstheim(cellX, cellY, region_lookup_dict):
    # Anthology Solstheim is shifted 7 cells to the east, 6 cells to the north 
    # Anthology Solstheim lies inside of [-21,-10]x, [21,34]y
    anthSolsRange = [-21,-10,21,34]
    xShift = 7
    yShift = 6
    vanillaSolsRange = [anthSolsRange[0]-xShift,anthSolsRange[1]-xShift,anthSolsRange[2]-yShift,anthSolsRange[3]-yShift]

    if cellX in range(vanillaSolsRange[0],vanillaSolsRange[1]+1) and cellY in range(vanillaSolsRange[2],vanillaSolsRange[3]+1):
        return check_region(cellX+xShift, cellY+yShift)
    elif cellX in range(anthSolsRange[0],anthSolsRange[1]+1) and cellY in range(anthSolsRange[2],anthSolsRange[3]+1):
        return check_region(cellX+xShift, cellY+yShift)
    else:
        return check_region(cellX,cellY)

def isReleased(region_name, mod_list):
    game_regions = []

    ## Add vanilla regions
    game_regions += vanilla_regions

    ## Add expansion regions
    if 'Anthology_Solstheim' in mod_list or 'Bloodmoon' in mod_list:
        game_regions += solstheim_regions
    # if 'Tribunal' in mod_list:
    #     game_regions.append('Mournhold')


    ## Add tr regions
    if 'TR_Mainland' in mod_list:
        game_regions += tr_released_regions


    if region_name in game_regions:
        return True
    else:
        return False

def writeRegionLookupTable(grid_xlim, grid_ylim):
    region_dict = {}

    for x in range(grid_xlim[0], grid_xlim[1]+1):
        for y in range(grid_ylim[0], grid_ylim[1]+1):
            region = check_region(x,y)
            if region != 'unknown':
                region_dict[f'{x}_{y}'] = region

    with open('./region_lookup_dict.json', 'w') as fp:
        json.dump(region_dict, fp)

if __name__ == "__main__":
    grid_xlim = [-42,60]
    grid_ylim = [-64,37]
    grid_size = 40

    # writeRegionLookupTable(grid_xlim, grid_ylim)
