# Color-Segmentation  [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://github.com/vasantvohra/Color-Segmentation/blob/master/color_segment.py) [![forthebadge](https://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://forthebadge.com)

[Color_Segment.py](https://github.com/vasantvohra/Color-Segmentation/blob/master/color_segment.py)
### TASK
 > * Count the number of segregated colored trash bags
---
### Algorithm
```
Step 1
- Input image 
- convert BGR to HSV
- finding fixed colors, Blue, Yellow , Red, Green
- Specifying RGB/HSV Boundaries : lower / upper
Step 2
- creating mask of image by cv2.inRange(image, lower, upper)
- Applying the masking to residual img by cv2.bitwise_and

Step 3
- RGB Channels split & convert HSV 2 Gray
- Gaussian Blur
Step 4
Morphological Transformations
- Canny edge detection
- Dilation
- Erosion

Step 5
- find and count countours on edged image
- Defining Countour AREA
- Convex hull boundaries
- Draw contours i.e. mark all findings with different colors
```
#### Usage
---
```sh
python color_segment.py -i garbagebags2.jpg -o output.png -c hsv
python color_segment.py -i garbagebags2.jpg -o output.png -c rgb
```
---
### Input
![input](https://github.com/vasantvohra/Color-Segmentation/blob/master/garbagebags2.jpg) 
### Output
![output](https://github.com/vasantvohra/Color-Segmentation/blob/master/output.jpg)

---
### Result Screenshot
![Demo](https://github.com/vasantvohra/Color-Segmentation/blob/master/counting.png)
---
## Other Example

![input](https://github.com/vasantvohra/Color-Segmentation/blob/master/coloredimage.jpeg) ![output](https://github.com/vasantvohra/Color-Segmentation/blob/master/out.png)
![result](https://github.com/vasantvohra/Color-Segmentation/blob/master/thumbpin%20count.png)

### Next step do:
#### Pantopic Instance segmentation
![input](https://github.com/vasantvohra/Color-Segmentation/blob/master/count%20people.png)
---
## Applications
[Automatic Color Segmentation of Images with
Application to Detection of Variegated
Coloring in Skin Tumors](http://groups.inf.ed.ac.uk/vision/MCDONAGH/related%20work/literature/Automatic%20color%20segmentation%20of%20images%20with%20application%20todetection%20of%20variegated%20coloring%20in%20skin%20tumors.pdf)

[Color Image Segmentation for Multimedia Applications](https://link.springer.com/article/10.1023/A:1008163913937)
