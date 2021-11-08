import matplotlib.pyplot as plt
from colorized_voroni import voronoi_finite_polygons_2d
import numpy as np 
from scipy.spatial import Voronoi
import cv2
from seaborn import color_palette
import json

point_matrix = []

def mousePoints(event,x,y,flags,params):
    global point_matrix
    # Left button mouse click event opencv
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(point_matrix) == 0:
            point_matrix = np.array([x,y]).reshape((1,2))
        else:
            point_matrix = np.vstack((point_matrix, np.array([x,y]).reshape((1,2))))


def pick_points(img_path):
    global point_matrix
    img = cv2.imread(img_path)
    resize_factor = 4
    img = cv2.resize(img, dsize=(int(img.shape[1]/resize_factor),int(img.shape[0]/resize_factor)),interpolation = cv2.INTER_AREA)
    
    while True:
        for x in range(len(point_matrix)):
            cv2.circle(img,(point_matrix[x][0],point_matrix[x][1]),3,(0,255,0),cv2.FILLED)
    
    
        # Showing original image
        cv2.imshow("Original Image ", img)
        # Mouse click event on original image
        cv2.setMouseCallback("Original Image ", mousePoints)
        # Printing updated point matrix
        # print(point_matrix)
        # Refreshing window all time
        cv2.waitKey(1)
        if cv2.waitKey(1) == ord('a'):
            break


    print(point_matrix * resize_factor)
    return point_matrix * resize_factor

if __name__ == "__main__":

    # points = pick_points('tr_map.png')

    img = cv2.imread('tr_map.png')
    
    grid_size = 40 # pixels
    grid_xlim = [-44,64]
    grid_ylim = [-64,34]

    with open('./coord.json') as fp:
        coord_dict = json.load(fp)

    # for i in range(grid_xlim[1]-grid_xlim[0]+1):
    #     for j in range(grid_ylim[1]-grid_ylim[0]+1):
    #         pt1 = (i*grid_size, j*grid_size)
    #         pt2 = ((i+1)*grid_size, (j+1)*grid_size)

    #         cv2.rectangle(img, pt1, pt2, (0,255,0), 3)
    
    for style, locs in coord_dict.items():
        print(style)
        img_style = img.copy()


        # compute points
        points = []
        for name, loc in locs.items():
            px = (loc[0]-grid_xlim[0]) * grid_size + grid_size/2
            py = (grid_ylim[1]-loc[1]) * grid_size + grid_size/2

            # print(f'{name}: {loc} ==> {(px,py)}')
            points.append([px,py])


        # compute Voronoi tesselation
        vor = Voronoi(points)
        
        # plot
        regions, vertices = voronoi_finite_polygons_2d(vor)
        colors = color_palette("cubehelix", len(regions))
        # colors = color_palette("icefire", len(regions))
        
        # Continuous
        for i,region in enumerate(regions):
            polygon = vertices[region]
            contours = polygon.astype(int)

            c = np.array(colors[i])*255
            cv2.fillPoly(img_style, pts=[contours], color=c)
            cv2.drawContours(img_style, [contours], -1, (0,0,0), 2, lineType=cv2.LINE_AA)
            # print(i,':',colors[i] )
            
        alpha = 0.5
        img_comp =  cv2.addWeighted(img_style, alpha, img, 1 - alpha, 0)

        for p in points:
            cv2.circle(img_comp, (int(p[0]),int(p[1])), radius=10, color=(0,0,0), thickness=-1)


        cv2.imwrite(f'test_{style}.png',img_comp)
   
