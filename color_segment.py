import numpy as np
import argparse
import imutils
import cv2

#USAGE
#python color_segment3.py -i garbagebags2.jpg -o output.png -c rgb/hsv


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="garbagebags2.jpg",
    help="path to the input image")
ap.add_argument("-o", "--output", default="output.jpg",
    help="path to the output image")
ap.add_argument("-c", "--color", default="hsv",
    help="define the color space you want to use for segmentation, RGB,HSV,L*")
args = vars(ap.parse_args())
  
# dict to count
counter = {}
 
# load the image
image_orig = cv2.imread(args["image"])
height_orig, width_orig = image_orig.shape[:2]
Color=args['color']

if Color=='hsv':
    cv2.imshow("input",image_orig)
    image_orig=cv2.cvtColor(image_orig,cv2.COLOR_BGR2HSV)

# output image with contours
image_contours = image_orig.copy()
 
# colors to detect

colors = ['blue','yellow','red','green']

for color in colors:
 
    # copy of original image
    image_to_process = image_orig.copy()
 
    # initializes counter
    counter[color] = 0
 
    # define NumPy arrays of color boundaries (BGR/HSV vectors)
    if color == 'blue' and Color=='hsv':
        lower = np.array([101,50,38])
        upper = np.array([110,255,255])
    elif color == 'blue' and Color=='rgb':
        lower = np.array([ 86, 31,  4])
        upper = np.array([220, 88, 50])
   # elif color == 'white':
        # invert image colors
    #    image_to_process = (255-image_to_process)
     #   lower = np.array([ 50,  50,  40])
      #  upper = np.array([100, 120,  80])
    elif color=='yellow' and Color=='hsv':
        lower=np.array([20,100,100]) #110,238,219
        upper= np.array([30,255,255]) #130,238,219
    elif color == 'yellow' and Color=='rgb':
        lower = np.array([23,41,133 ]) #25,  146,  190
        upper = np.array([40,150,255]) #62, 174,  250
    elif color=='red' and Color=='hsv':
        lower = np.array([160,20,70]) #[30,150,50]
        upper = np.array([190,255,255])#[255,255,180]
    elif color == 'red' and Color=='rgb':
        lower = np.array([ 17,  15,  100])
        upper = np.array([50, 56,  200])
    elif color == 'green' and Color == 'hsv':
        lower=np.array([36,25,25])
        upper=np.array([70,255,255])
    elif color == 'green' and Color == 'rgb':
        lower=np.array([124,252,0])
        upper=np.array([107,142,35])
      # GREEN BOUNDARIES MISSING
      
##    elif color == 'black':
##        lower=np.array([0, 0, 0])
##        upper=np.array([180, 255, 30])    
    
    # find the colors within the specified boundaries
    image_mask = cv2.inRange(image_to_process, lower, upper)
    #cv2.imshow("mask",image_mask)
    # apply the mask
    image_res = cv2.bitwise_and(image_to_process, image_to_process, mask = image_mask)
    
    # PREVIEW THE MASKED IMAGE
    while True:
        #cv2.imshow(color,np.hstack([image_orig,image_res]))
        cv2.imshow(color,image_res)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    ## load the image, convert it to grayscale, and blur it slightly
    #image_gray = cv2.cvtColor(image_res, cv2.COLOR_HSV2GRAY) # BGR 2 GRY
    a,c,image_gray = cv2.split(image_res)
    image_gray = cv2.GaussianBlur(image_gray, (5, 5), 0)
    # MORPHOLOGICAL TRANSFORMATION
    # perform edge detection, then perform a dilation + erosion to close gaps in between object edges
    image_edged = cv2.Canny(image_gray, 50, 100)
    
    image_edged = cv2.dilate(image_edged, None, iterations=10)
    
    # it erodes away the boundaries of foreground object
    image_edged = cv2.erode(image_edged, None, iterations=10) 
 
    # find contours in the edge map
    cnts = cv2.findContours(image_edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    ### Understand..............
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
 
    # loop over the contours individually
    for c in cnts:
         
        # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 30:
            continue
         
        # compute the Convex Hull of the contour

        hull = cv2.convexHull(c)
        
        if color == 'blue':
            # prints contours in rgb blue color
            cv2.drawContours(image_contours,[hull],0,(0,0,255),1) 
            
        #elif color == 'white':
            # prints contours in green color
          #  cv2.drawContours(image_contours,[hull],0,(0,255,0),1)
          
        elif color == 'yellow':
            # prints contours in rgb red  color
            cv2.drawContours(image_contours,[hull],0,(255,0,0),1)
            
        elif color == 'red':
            # prints contours in rgb  green color
            cv2.drawContours(image_contours,[hull],0,(60, 100, 50),1) # Yellow 255,255,0
            
        elif color == 'green':
            # prints contours in rgb yellow color
            cv2.drawContours(image_contours,[hull],0,(255, 128, 0),1)
##        elif color == 'black':
##            # prints contours in yellow color
##            cv2.drawContours(image_contours,[hull],0,(0, 128, 255),1)

        counter[color] += 1
        
        #cv2.putText(image_contours, "{:.0f}".format(cv2.contourArea(c)), (int(hull[0][0][0]), int(hull[0][0][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
 
    # Print the number of colonies of each color
    print("{} {} Counts".format(counter[color],color))

if Color=='hsv':
    image_contours=cv2.cvtColor(image_contours,cv2.COLOR_HSV2BGR)

else:
    pass
# Writes the output image

cv2.imwrite(args["output"],image_contours)

cv2.imshow("output",image_contours)
