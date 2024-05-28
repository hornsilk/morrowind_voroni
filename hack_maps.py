import cv2
# cell coordinates of the future world map
F_GRID_XLIM = [-42,62]
F_GRID_YLIM = [-64,41]
# cell coordinates of the present world map
P_GRID_XLIM = [-42,60]
P_GRID_YLIM = [-64,37]

X_BOUNDARY = [18,59]
Y_BOUNDARY = [-41,33]

# pixel scale of the world map grid in 'img'
GRID_SIZE = 40 

map_future = cv2.imread('./reference_maps/tr_map_future.png')
map_present = cv2.imread('./reference_maps/tr_map_present.png')


def grid_to_pxl(x_grid,y_grid, grid_x_min, grid_y_max):
    x_pxl = (x_grid - grid_x_min) * GRID_SIZE
    y_pxl = (grid_y_max - y_grid) * GRID_SIZE
    return [x_pxl,y_pxl]

[l,t] = grid_to_pxl(X_BOUNDARY[0],Y_BOUNDARY[1],P_GRID_XLIM[0],P_GRID_YLIM[1])
[r,b] = grid_to_pxl(X_BOUNDARY[1],Y_BOUNDARY[0],P_GRID_XLIM[0],P_GRID_YLIM[1])
present_crop = map_present[t:b,l:r]
cv2.imwrite(f'./reference_maps/present_crop.png',present_crop)

[l,t] = grid_to_pxl(X_BOUNDARY[0],Y_BOUNDARY[1],F_GRID_XLIM[0],F_GRID_YLIM[1])
[r,b] = grid_to_pxl(X_BOUNDARY[1],Y_BOUNDARY[0],F_GRID_XLIM[0],F_GRID_YLIM[1])
future_crop = map_future[t:b,l:r]
cv2.imwrite(f'./reference_maps/future_crop_crop.png',future_crop)

map_spliced = map_future.copy()
map_spliced[t:b,l:r] = present_crop.copy()
cv2.imwrite(f'./reference_maps/tr_map_spliced.png',map_spliced)
