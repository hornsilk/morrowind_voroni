from colorized_voroni import voronoi_finite_polygons_2d
import numpy as np 
from scipy.spatial import Voronoi
import cv2
from seaborn import color_palette
import json
import regions

################################################################################################################################################

MOD_OPTIONS = ['Morrowind','Bloodmoon', 'Tribunal', 'GotY', 'TR_Mainland', 'Anthology_Solstheim', 'OpenMW', 'Improved_Temple_Experience','SHotN','Province_Cyrodiil']

# cell coordinates of the world map
GRID_XLIM = [-42,60]
GRID_YLIM = [-64,37]
# pixel scale of the world map grid in 'img'
GRID_SIZE = 40 


################################################################################################################################################






def parse_modlist(mod_list):
    # Check Modlist
    # remove mods not in supported MOD_OPTIONS
    mod_set = set(MOD_OPTIONS).intersection(set(mod_list))

    # add 'Morrowind'
    if 'Morrowind' not in mod_set:
        mod_set.add('Morrowind') 

    # goty = bloodmoon + tribunal
    if 'GotY' in mod_set:
        mod_set.add('Bloodmoon')
        mod_set.add('Tribunal')
    elif 'Bloodmoon' in mod_list and 'Tribunal' in mod_set:
        mod_set.add('GotY')

    # tr_mainland requires goty
    if 'TR_Mainland' in mod_set and 'GotY' not in mod_set:
        mod_set.remove('TR_Mainland')

    # anthology_solstheim requires bloodmoon
    if 'Anthology_Solstheim' in mod_set and 'Bloodmoon' not in mod_set:
        mod_set.remove('Anthology_Solstheim')

    mod_list = sorted(list(mod_set))

    return mod_list

def prune_locations(coord_dict, mod_list):
    # Build Location List
    locs = {}
    for name, tp in coord_dict.items():
        
        # always add Vvardenfell locations
        if 'Morrowind' in mod_list:
            if tp[2] == 'Vvardenfell':
                locs[name] = [tp[0], tp[1]]

        # Handle the Vos Node specially, as it is in both Improved_Temple_Experience and TR_Mainland
        if name == 'Vos':
            if 'Improved_Temple_Experience' in mod_list or 'TR_Mainland' in mod_list:
                locs[name] = [tp[0], tp[1]]
            continue

        # add modded in locations
        if tp[2] in mod_list:
            
            # adjust Solstheim position
            if tp[2] == 'Bloodmoon':
                if 'Anthology_Solstheim' in mod_list:
                    # Anthology Solstheim is shifted 7 cells to the east, 6 cells to the north 
                    locs[name] = [tp[0]+7, tp[1]+6]
                else:
                    locs[name] = [tp[0], tp[1]]

            # Mournhold intervention is inaccessible without OpenMW
            # and now, with TR_Preview dead, Mournhold is fully unlinked from the mainland. should not be included either way.
            elif tp[2] == 'Tribunal':
                if 'OpenMW' in mod_list:
                    # locs[name] = [tp[0], tp[1]]
                    foo=2
            
            # add the rest, if their mod is present
            else:
                locs[name] = [tp[0], tp[1]]

    return locs

def pixelize_location_points(locs):
    # Compute Points in img pixel coordinates
    pxl_points = []
    for name, loc in locs.items():
        px = (loc[0]-GRID_XLIM[0]) * GRID_SIZE + GRID_SIZE/2
        py = (GRID_YLIM[1]-loc[1]) * GRID_SIZE + GRID_SIZE/2

        # print(f'{name}: {loc} ==> {(px,py)}')
        pxl_points.append([px,py])
    
    return pxl_points

def compute_voroni_map(locs, pxl_points, colors, img_style):
    # Compute Voronoi Tesselation
    vor = Voronoi(pxl_points)
    
    # Plot
    regions, vertices = voronoi_finite_polygons_2d(vor)
    
    for i,region in enumerate(regions):
        polygon = vertices[region]
        contours = polygon.astype(int)

        c = np.array(colors[i])*255
        cv2.fillPoly(img_style, pts=[contours], color=c)
        cv2.drawContours(img_style, [contours], -1, (0,0,0), 2, lineType=cv2.LINE_AA)
        # print(i,':',colors[i] )
    return img_style

def compute_kings_map(locs, pxl_points, colors, img_style):
    node_locations = list(locs.values())

    # Sort Points
    # hypothesis: higher up (smaller y) has priority, then left to right
    node_locations = np.array(sorted(node_locations, key = lambda x: x[1]+x[0]/10000000))

    # Compute King's Walk Distance
    cells = -1*np.ones((GRID_YLIM[1] - GRID_YLIM[0]+1, GRID_XLIM[1] - GRID_XLIM[0]+1))
    for x in range(GRID_XLIM[0], GRID_XLIM[1]+1):
        for y in range(GRID_YLIM[0], GRID_YLIM[1]+1):
            node_idx = np.argmin(np.apply_along_axis(np.amax, 1, abs(node_locations - [x,y])))
            # print(x,y,node_idx)

            i = (x - GRID_XLIM[0])
            j = (GRID_YLIM[1] - y)
            cells[j,i] = node_idx

            # Draw
            pt1 = (i*GRID_SIZE, j*GRID_SIZE)
            pt2 = ((i+1)*GRID_SIZE, (j+1)*GRID_SIZE)
            c = np.array(colors[node_idx])*255
            cv2.rectangle(img_style, pt1, pt2, c, -1)

    
    # Detect Edges
    img_gray = cv2.cvtColor(img_style, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(image=img_gray, threshold1=0, threshold2=200)
    img_style = cv2.bitwise_and(img_style, img_style, mask=(255-edges))
    return img_style

def generate_custom_color_palette(locs, regionalPalette=False):

    if regionalPalette:
        with open('./region_colors.json') as fp:
            region_colors = json.load(fp)

        with open('./region_lookup_dict.json') as fp:
            region_lookup_dict = json.load(fp)

        colors = []
        dupe_colors = []
        for i,loc in enumerate(locs.items()):
        
            x = loc[1][0]
            y = loc[1][1]
            r = regions.check_region(x,y,region_lookup_dict)
            c = region_colors[r]

            myColor = (c[0]/255,c[1]/255,c[2]/255)

            if myColor in colors:
                # if color already taken, note it
                dupe_colors.append(i)

            colors.append(myColor)

        # fix placeholder colors
        backup_colors = color_palette("Paired", len(dupe_colors))
        for i,dupe_idx in enumerate(dupe_colors):
            colors[dupe_idx] = backup_colors[i]

    else:
        # generic palette
        colors = color_palette("Paired", len(locs))
        
    return colors


def draw_regions_map(img, locs, pxl_points, style):
    # Create Color Palette and Test Img
    colors = generate_custom_color_palette(locs)


    # Sort Points
    # hypothesis: higher up (smaller y) has priority, then left to right
    # pxl_points = sorted(pxl_points, key = lambda x: -x[1]+x[0]/10000000) 

    Z = zip(pxl_points, locs.keys(), locs.values(), colors)
    Z = sorted(Z, key = lambda triple: -triple[0][1]+triple[0][0]/10000000) 

    # unpack
    pxl_points = [_[0] for _ in Z]
    locs_k = [_[1] for _ in Z]
    locs_v = [_[2] for _ in Z]
    colors = [_[3] for _ in Z]
    locs = {}
    for i in range(len(locs_k)):
        locs[locs_k[i]] = locs_v[i]



    regions_map_img = img.copy()

    if style == 'Continuous':
        regions_map_img = compute_voroni_map(locs, pxl_points, colors, regions_map_img)
    
    elif style == 'Discrete':
        regions_map_img = compute_kings_map(locs, pxl_points, colors, regions_map_img)
        
    return regions_map_img

def create_release_mask(img, mod_list):
    mask = np.zeros(img.shape[:2], dtype="uint8")

    with open('./region_lookup_dict.json') as fp:
        region_lookup_dict = json.load(fp)

    # Scan through game cells
    cells = -1*np.ones((GRID_YLIM[1] - GRID_YLIM[0]+1, GRID_XLIM[1] - GRID_XLIM[0]+1))
    for x in range(GRID_XLIM[0], GRID_XLIM[1]+1):
        for y in range(GRID_YLIM[0], GRID_YLIM[1]+1):
            i = (x - GRID_XLIM[0])
            j = (GRID_YLIM[1] - y)

            # Check if the cell is within the TR_Mainland release
            inRelease = False

            if 'Anthology_Solstheim' in mod_list:
                regionName = regions.check_region(x,y,region_lookup_dict)
            else:
                regionName = regions.check_region_vanilla_solstheim(x,y,region_lookup_dict)

            if regions.isReleased(regionName, mod_list):
                inRelease = True

            # If inRelease, add to mask
            if inRelease:
                pt1 = (i*GRID_SIZE, j*GRID_SIZE)
                pt2 = ((i+1)*GRID_SIZE, (j+1)*GRID_SIZE)
                cv2.rectangle(mask, pt1, pt2, 255, -1)

    return mask


def merge_and_save(img, regions_map, pxl_points, mod_list, map_name):
    # Merge Colormap with Original Image
    alpha = 0.5
    alpha_map = 0.8

    mask = create_release_mask(img, mod_list)
    masked_map = cv2.bitwise_and(regions_map, regions_map, mask=mask)
    masked_map =  cv2.addWeighted(masked_map, alpha_map, regions_map, 1 - alpha_map, 0)

    img_comp =  cv2.addWeighted(masked_map, alpha, img, 1 - alpha, 0)

    # Draw Dots on Locations
    for p in pxl_points:
        cv2.circle(img_comp, (int(p[0]),int(p[1])), radius=10, color=(0,0,0), thickness=-1)

    # Write Title
    cv2.putText(img_comp, map_name.split('-')[0].replace('_',' '), (50,150), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,0), thickness=2)
    # Write Mods
    for i,s in enumerate(map_name.split('-')[1:]):
        cv2.putText(img_comp, s.replace('_',' '), (100, 220 + 60*i), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), thickness=2)


    # Save
    cv2.imwrite(f'./generated_maps/{map_name}.png',img_comp)

def produce_map(img, coord_dict, map_type, mod_list):
    
    mod_list = parse_modlist(mod_list)
    

    # Name the Map
    map_name = f'{map_type}_Intervention_Map'
    for mod in mod_list:
        if mod == 'OpenMW':
            map_name = 'OpenMW_' + map_name
        elif not mod == 'Morrowind':
            if 'GotY' in mod_list and (mod == 'Bloodmoon' or mod == 'Tribunal'):
                continue
            map_name = map_name + f'-{mod}'



    # if OpenMW, use Continuous style. Else use Discrete
    if 'OpenMW' in mod_list:
        style = 'Continuous'
    else:
        style = 'Discrete'


    locs = prune_locations(coord_dict, mod_list)
    pxl_points = pixelize_location_points(locs)
    regions_map = draw_regions_map(img, locs, pxl_points, style)


    print('Generating ' + map_type + ' map with mod list:')
    print(mod_list)
    print(map_name + '.png')
    print()
    merge_and_save(img, regions_map, pxl_points, mod_list, map_name)
   



if __name__ == "__main__":

    img = cv2.imread('./reference_maps/tr_map.png')
    
    with open('./coord.json') as fp:
        master_dict = json.load(fp)
    
    mod_list = ['OpenMW','GotY', 'TR_Mainland', 'Anthology_Solstheim', 'Improved_Temple_Experience']
  
    for map_type in ['Almsivi', 'Divine']:
        coord_dict = master_dict[map_type]
        produce_map(img, coord_dict, map_type, mod_list.copy())

