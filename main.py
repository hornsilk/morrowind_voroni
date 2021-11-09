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
    
    for map, locs in coord_dict.items():
        print(map)
        
        colors = color_palette("Paired", len(locs))

        for style in ['continuous', 'discrete']:
            print(style)
            img_style = img.copy()


            # compute points
            points = []
            for name, loc in locs.items():
                px = (loc[0]-grid_xlim[0]) * grid_size + grid_size/2
                py = (grid_ylim[1]-loc[1]) * grid_size + grid_size/2

                # print(f'{name}: {loc} ==> {(px,py)}')
                points.append([px,py])

            # hypothesis: higher up (smaller y) has priority, then left to right
            points = sorted(points, key = lambda x: -x[1]+x[0]/10000000) 

            if style == 'continuous':
                # compute Voronoi tesselation
                vor = Voronoi(points)
                
                # plot
                regions, vertices = voronoi_finite_polygons_2d(vor)
                
                # Continuous
                for i,region in enumerate(regions):
                    polygon = vertices[region]
                    contours = polygon.astype(int)

                    c = np.array(colors[i])*255
                    cv2.fillPoly(img_style, pts=[contours], color=c)
                    cv2.drawContours(img_style, [contours], -1, (0,0,0), 2, lineType=cv2.LINE_AA)
                    # print(i,':',colors[i] )
            
            elif style == 'discrete':
                node_locations = list(locs.values())

                # hypothesis: higher up (smaller y) has priority, then left to right
                node_locations = np.array(sorted(node_locations, key = lambda x: x[1]+x[0]/10000000))

                cells = -1*np.ones((grid_ylim[1] - grid_ylim[0]+1, grid_xlim[1] - grid_xlim[0]+1))
                for x in range(grid_xlim[0], grid_xlim[1]+1):
                    for y in range(grid_ylim[0], grid_ylim[1]+1):
                        node_idx = np.argmin(np.apply_along_axis(np.amax, 1, abs(node_locations - [x,y])))
                        # print(x,y,node_idx)

                        i = (x - grid_xlim[0])
                        j = (grid_ylim[1] - y)
                        cells[j,i] = node_idx


                        pt1 = (i*grid_size, j*grid_size)
                        pt2 = ((i+1)*grid_size, (j+1)*grid_size)
                        c = np.array(colors[node_idx])*255

                        cv2.rectangle(img_style, pt1, pt2, c, -1)
                
                # detect edges
                img_gray = cv2.cvtColor(img_style, cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(image=img_gray, threshold1=0, threshold2=200)
                img_style = cv2.bitwise_and(img_style, img_style, mask=(255-edges))


            alpha = 0.5
            img_comp =  cv2.addWeighted(img_style, alpha, img, 1 - alpha, 0)

            for p in points:
                cv2.circle(img_comp, (int(p[0]),int(p[1])), radius=10, color=(0,0,0), thickness=-1)

            cv2.putText(img_comp, f'{map}_{style}_map', (50,150), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,0), thickness=2)

            cv2.imwrite(f'{map}_{style}.png',img_comp)
   
