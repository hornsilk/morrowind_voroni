from colorized_voroni import voronoi_finite_polygons_2d
import numpy as np 
from scipy.spatial import Voronoi
import cv2
from seaborn import color_palette
import json


def produce_map(img, coord_dict, map_type, mod_list):
    mod_options = ['Bloodmoon', 'Tribunal', 'GotY', 'TR_Mainland', 'TR_Preview', 'TR_Travels', 'Anthology_Solstheim', 'OpenMW']
    # Check Modlist
    mod_set = set(mod_list)

    # goty = bloodmoon + tribunal
    if 'GotY' in mod_set:
        mod_set.add('Bloodmoon')
        mod_set.add('Tribunal')
    elif 'Bloodmoon' in mod_list and 'Tribunal' in mod_set:
        mod_set.add('GotY')

    # tr_mainland requires goty
    if 'TR_Mainland' in mod_set and 'GotY' not in mod_set:
        mod_set.remove('TR_Mainland')

    # tr_preview and tr_travels require tr_mainland
    for tr_ext in ['TR_Preview', 'TR_Travels']:
        if tr_ext in mod_set and 'TR_Mainland' not in mod_set:
            mod_set.remove(tr_ext)

    # anthology_solstheim requires bloodmoon
    if 'Anthology_Solstheim' in mod_set and 'Bloodmoon' not in mod_set:
        mod_set.remove('Anthology_Solstheim')

    mod_list = sorted(list(mod_set))

    
    # cell coordinates of the world map
    grid_xlim = [-44,59]
    grid_ylim = [-63,36]
    # pixel scale of the world map grid in 'img'
    grid_size = 40 


    # Name the Map
    map_name = f'{map_type}_Intervention_Map'
    for mod in mod_list:
        if mod == 'OpenMW':
            map_name = 'OpenMW_' + map_name
        elif not mod == 'Morrowind':
            if 'GotY' in mod_list and (mod == 'Bloodmoon' or mod == 'Tribunal'):
                continue
            map_name = map_name + f'-{mod}'
    print(map_name)
    print(mod_list)


    # if OpenMW, use Continuous style. Else use Discrete
    if 'OpenMW' in mod_list:
        style = 'Continuous'
    else:
        style = 'Discrete'

    # Build Location List
    locs = {}
    for name, tp in coord_dict.items():
        
        # always add Vvardenfell locations
        if 'Morrowind' in mod_list:
            if tp[2] == 'Vvardenfell':
                locs[name] = [tp[0], tp[1]]

        # Handle the Vos Node specially, as it is in both Improved_Temple_Experience and TR_Travels
        if name == 'Vos':
            if 'Improved_Temple_Experience' in mod_list or 'TR_Travels' in mod_list:
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
            elif tp[2] == 'Tribunal':
                if 'OpenMW' in mod_list:
                    locs[name] = [tp[0], tp[1]]
            
            # add the rest, if their mod is present
            else:
                locs[name] = [tp[0], tp[1]]


    # Create Color Palette and Test Img
    colors = color_palette("Paired", len(locs))
    img_style = img.copy()


    # Compute Points in img pixel coordinates
    pxl_points = []
    for name, loc in locs.items():
        px = (loc[0]-grid_xlim[0]) * grid_size + grid_size/2
        py = (grid_ylim[1]-loc[1]) * grid_size + grid_size/2

        # print(f'{name}: {loc} ==> {(px,py)}')
        pxl_points.append([px,py])

    # Sort Points
    # hypothesis: higher up (smaller y) has priority, then left to right
    pxl_points = sorted(pxl_points, key = lambda x: -x[1]+x[0]/10000000) 

    if style == 'Continuous':
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
    
    elif style == 'Discrete':
        node_locations = list(locs.values())

        # Sort Points
        # hypothesis: higher up (smaller y) has priority, then left to right
        node_locations = np.array(sorted(node_locations, key = lambda x: x[1]+x[0]/10000000))

        # Compute King's Walk Distance
        cells = -1*np.ones((grid_ylim[1] - grid_ylim[0]+1, grid_xlim[1] - grid_xlim[0]+1))
        for x in range(grid_xlim[0], grid_xlim[1]+1):
            for y in range(grid_ylim[0], grid_ylim[1]+1):
                node_idx = np.argmin(np.apply_along_axis(np.amax, 1, abs(node_locations - [x,y])))
                # print(x,y,node_idx)

                i = (x - grid_xlim[0])
                j = (grid_ylim[1] - y)
                cells[j,i] = node_idx

                # Draw
                pt1 = (i*grid_size, j*grid_size)
                pt2 = ((i+1)*grid_size, (j+1)*grid_size)
                c = np.array(colors[node_idx])*255
                cv2.rectangle(img_style, pt1, pt2, c, -1)
        
        # Detect Edges
        img_gray = cv2.cvtColor(img_style, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(image=img_gray, threshold1=0, threshold2=200)
        img_style = cv2.bitwise_and(img_style, img_style, mask=(255-edges))

    # Merge Colormap with Original Image
    alpha = 0.5
    img_comp =  cv2.addWeighted(img_style, alpha, img, 1 - alpha, 0)

    # Draw Dots on Locations
    for p in pxl_points:
        cv2.circle(img_comp, (int(p[0]),int(p[1])), radius=10, color=(0,0,0), thickness=-1)

    # Write Title
    cv2.putText(img_comp, map_name, (50,150), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,0), thickness=2)

    # Save
    cv2.imwrite(f'./generated_maps/{map_name}.png',img_comp)
   



if __name__ == "__main__":

    img = cv2.imread('tr_map.png')
    
    with open('./coord.json') as fp:
        master_dict = json.load(fp)
    
    mod_options = ['Bloodmoon', 'Tribunal', 'GotY', 'TR_Mainland', 'TR_Preview', 'TR_Travels', 'Anthology_Solstheim', 'OpenMW', 'Improved_Temple_Experience']

    mod_list = ['Morrowind', 'GotY', 'TR_Mainland', 'TR_Preview', 'TR_Travels', 'Anthology_Solstheim', 'OpenMW', 'Improved_Temple_Experience']

    for map_type in ['Almsivi', 'Divine']:
        coord_dict = master_dict[map_type]
        produce_map(img, coord_dict, map_type, mod_list.copy())

