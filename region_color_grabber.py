import cv2
import numpy as np
import json
from colorthief import ColorThief

from main import GRID_XLIM, GRID_YLIM, GRID_SIZE
from regions import vanilla_regions, solstheim_regions, tr_released_regions


def grab_colors():
    tr_regions_img = cv2.imread('./reference_maps/tr_regions.png')

    region_imgs = {}
    for r in vanilla_regions + solstheim_regions + tr_released_regions:
        region_imgs[r] = []

        
    with open('./region_lookup_dict.json') as fp:
        region_lookup_dict = json.load(fp)

    for x in range(GRID_XLIM[0], GRID_XLIM[1]+1):
        for y in range(GRID_YLIM[0], GRID_YLIM[1]+1):

            if f'{x}_{y}' not in region_lookup_dict:
                continue

            region = region_lookup_dict[f'{x}_{y}']

            # grab img
            i = (x - GRID_XLIM[0])
            j = (GRID_YLIM[1] - y)
            pt1 = (i*GRID_SIZE, j*GRID_SIZE)
            pt2 = ((i+1)*GRID_SIZE, (j+1)*GRID_SIZE)
            region_img = tr_regions_img[pt1[1]:pt2[1],pt1[0]:pt2[0]]
            
            if len(region_imgs[region]) == 0:
                region_imgs[region] = region_img
            else:
                region_imgs[region] = cv2.hconcat([region_imgs[region],region_img])


    region_colors = {}

    for region in region_imgs:
        print(region, region_imgs[region].shape)
        cv2.imwrite(f'./tmp/{region}.png', region_imgs[region])

        ct = ColorThief(f'./tmp/{region}.png')
        region_color = ct.get_color(quality=1)
        foo=2

        region_colors[region] = (region_color[2],region_color[1],region_color[0])
        # cv2.imshow(region,region_imgs[region])
        # cv2.waitKey()

    with open('./region_colors.json', 'w') as fp:
        json.dump(region_colors, fp)

if __name__ == "__main__":
    # grab_colors()

    with open('./region_colors.json') as fp:
        region_colors = json.load(fp)

    for r,c in region_colors.items():
        img = np.zeros((300, 300, 3), dtype="uint8")
        img[:] = c

        cv2.imshow(r,img)
        cv2.waitKey()
        
