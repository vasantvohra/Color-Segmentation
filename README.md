# Color-Segmentation  [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://github.com/vasantvohra/Color-Segmentation/blob/master/color_segment.py) [![forthebadge](https://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://forthebadge.com) ![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)

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
Corner Edge Detection
- Canny edge detection
Morphological Transformations
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
![input](https://raw.githubusercontent.com/vasantvohra/Color-Segmentation/master/garbagebags2.jpg) 
### Output
![output](https://raw.githubusercontent.com/vasantvohra/Color-Segmentation/master/output.jpg)

---
### Result Screenshot
![Demo](https://raw.githubusercontent.com/vasantvohra/Color-Segmentation/master/counting.png)

---

## Other Example

![input](https://raw.githubusercontent.com/vasantvohra/Color-Segmentation/master/coloredimage.jpeg) ![output](https://raw.githubusercontent.com/vasantvohra/Color-Segmentation/master/out.png)
![result](https://raw.githubusercontent.com/vasantvohra/Color-Segmentation/master/thumbpin%20count.png)
---
### Next steps:
#### Try Panoptic / Instance segmentation
![input](https://raw.githubusercontent.com/vasantvohra/Color-Segmentation/master/count%20people.png)

---

## Applications
[Automatic Color Segmentation of Images with
Application to Detection of Variegated
Coloring in Skin Tumors](http://groups.inf.ed.ac.uk/vision/MCDONAGH/related%20work/literature/Automatic%20color%20segmentation%20of%20images%20with%20application%20todetection%20of%20variegated%20coloring%20in%20skin%20tumors.pdf)

[Color Image Segmentation for Multimedia Applications](https://link.springer.com/article/10.1023/A:1008163913937)

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
