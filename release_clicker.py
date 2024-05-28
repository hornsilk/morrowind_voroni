import cv2, math
import json

from main import GRID_XLIM, GRID_YLIM, GRID_SIZE
from main import create_release_mask

CROP_W = 21
CROP_H = 15

# RELEASE_LIST = []
with open('./release_lookup_list.json') as fp:
    RELEASE_LIST = json.load(fp)


def click_event(event,x,y,flags,param):
    global cropped_map, left_cell, top_cell
    if event == cv2.EVENT_LBUTTONDOWN:
        # mouseX,mouseY = x,y
        [x_grid, y_grid] = pxl_to_grid(x,y, left_cell, top_cell)
        print(f'{x},{y} --> {x_grid}, {y_grid}')

        RELEASE_LIST.append(f'{x_grid}_{y_grid}')
    elif event == cv2.EVENT_RBUTTONDOWN:
        # mouseX,mouseY = x,y
        [x_grid, y_grid] = pxl_to_grid(x,y, left_cell, top_cell)
        print(f'REMOVED {x_grid}, {y_grid}')

        RELEASE_LIST.remove(f'{x_grid}_{y_grid}')
    elif event == cv2.EVENT_MBUTTONDOWN:
        for x_grid in range(left_cell, right_cell):
            for y_grid in range(bottom_cell, top_cell):
                RELEASE_LIST.append(f'{x_grid}_{y_grid}')



def grid_to_pxl(x_grid,y_grid):
    x_pxl = (x_grid - GRID_XLIM[0]) * GRID_SIZE
    y_pxl = (GRID_YLIM[1] - y_grid) * GRID_SIZE
    return [x_pxl,y_pxl]

def pxl_to_grid(x_pxl, y_pxl, grid_left, grid_top):
    x_grid = math.floor(x_pxl/GRID_SIZE) + grid_left
    y_grid = grid_top - math.floor(y_pxl/GRID_SIZE)
    return [x_grid, y_grid]

def click_regions():
    tr_regions_unmasked = cv2.imread('./reference_maps/tr_map.png')

    mask = create_release_mask(tr_regions_unmasked)
    alpha = 0.5
    alpha_map = 0.8
    masked_map = cv2.bitwise_and(tr_regions_unmasked, tr_regions_unmasked, mask=mask)
    masked_map =  cv2.addWeighted(masked_map, alpha_map, tr_regions_unmasked, 1 - alpha_map, 0)
    tr_regions_img =  cv2.addWeighted(masked_map, alpha, tr_regions_unmasked, 1 - alpha, 0)

    for j in range(math.ceil((GRID_YLIM[1] - GRID_YLIM[0])/CROP_H)):
        for i in range(math.ceil((GRID_XLIM[1] - GRID_XLIM[0])/CROP_W)):
            global left_cell, right_cell, top_cell, bottom_cell
            left_cell = GRID_XLIM[0] + CROP_W*i
            right_cell = min(left_cell + CROP_W, GRID_XLIM[1])
            top_cell = GRID_YLIM[1] - CROP_H * j
            bottom_cell = max(top_cell - CROP_H, GRID_YLIM[0])

            [lp, tp] = grid_to_pxl(left_cell,top_cell)
            [rp, bp] = grid_to_pxl(right_cell,bottom_cell)

            global cropped_map
            cropped_map = tr_regions_img[tp:bp,lp:rp]

            cv2.namedWindow('cropped_map')
            cv2.setMouseCallback('cropped_map',click_event)

            while(1):
                cv2.imshow('cropped_map', cropped_map)
                k = cv2.waitKey(20) & 0xFF
                if k == 27: # esc key
                    break


    with open('./release_lookup_list.json', 'w') as fp:
        json.dump(sorted(RELEASE_LIST), fp)

if __name__ == "__main__":
    click_regions()
