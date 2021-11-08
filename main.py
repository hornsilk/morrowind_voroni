import matplotlib.pyplot as plt
from colorized_voroni import voronoi_finite_polygons_2d
import numpy as np 
from scipy.spatial import Voronoi
import cv2
from seaborn import color_palette

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
    img_copy = img.copy()
    



    points = np.array(
        [[2492,  420],
        [1692 ,1196],
        [2860 ,1588],
        [1844 ,1896],
        [2476 , 784],
        [ 896 , 704],
        [3272 ,2064],
        [1368 , 952],
        [2780 ,1344],
        [1736 ,1484],
        [2700 ,2504],
        [2044 ,2128],
        [1776 ,1676],
        [3180 ,1660],
        [2488 ,1260],
    ])

    # compute Voronoi tesselation
    vor = Voronoi(points)

    # plot
    regions, vertices = voronoi_finite_polygons_2d(vor)
    # colors = color_palette("cubehelix", len(regions))
    colors = color_palette("icefire", len(regions))

    for i,region in enumerate(regions):

        polygon = vertices[region]
        contours = polygon.astype(int)
        
        c = np.array(colors[i])*255

        # if i == 14:
        #     c = c + np.array([100,100,0])

        cv2.fillPoly(img, pts =[contours], color=c)
        # print(i,':',colors[i] )



    alpha = 0.5
    img_comp =  cv2.addWeighted(img, alpha, img_copy, 1 - alpha, 0)

    for p in points:
        cv2.circle(img_comp, p, radius=10, color=(0,0,0), thickness=-1)

    cv2.imwrite("test.png",img_comp)

