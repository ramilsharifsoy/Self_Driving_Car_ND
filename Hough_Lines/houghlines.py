#lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
#In this case, we are operating on the image edges (the output from Canny) and the output from HoughLinesP 
#will be lines, which will simply be an array containing the endpoints (x1, y1, x2, y2) of all line segments
#detected by the transform operation. The other parameters define just what kind of line segments we're looking for.

#First off, rho and theta are the distance and angular resolution of our grid in Hough space. Remember that, 
#in Hough space, we have a grid laid out along the (Θ, ρ) axis. You need to specify rho in units of pixels 
#and theta in units of radians.

#So, what are reasonable values? Well, rho takes a minimum value of 1, and a reasonable starting place for 
#theta is 1 degree (pi/180 in radians). Scale these values up to be more flexible in your definition of what 
#constitutes a line.

#The threshold parameter specifies the minimum number of votes (intersections in a given grid cell) a 
#candidate line needs to have to make it into the output. The empty np.array([]) is just a placeholder, 
#no need to change it. min_line_length is the minimum length of a line (in pixels) that you will accept 
#in the output, and max_line_gap is the maximum distance (again, in pixels) between segments that you will 
#allow to be connected into a single line. 

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


# Read in and grayscale the image
<<<<<<< Updated upstream
# Note: in the previous example we were reading a .jpg 
# Here we read a .png and convert to 0,255 bytescale
image = (mpimg.imread('exit_ramp.png')*255).astype('uint8')
=======
image = mpimg.imread('edges_exitramp.jpg')
>>>>>>> Stashed changes
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Define a kernel size and apply Gaussian smoothing
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

# Define our parameters for Canny and apply
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# Next we'll create a masked edges image using cv2.fillPoly()
mask = np.zeros_like(edges)   
ignore_mask_color = 255   

# This time we are defining a four sided polygon to mask
imshape = image.shape
vertices = np.array([[(0,imshape[0]),(470, 290), (480, 290), (imshape[1],imshape[0])]], dtype=np.int32)
cv2.fillPoly(mask, vertices, ignore_mask_color)
masked_edges = cv2.bitwise_and(edges, mask)

# Define the Hough transform parameters
# Make a blank the same size as our image to draw on
rho = 2 # distance resolution in pixels of the Hough grid
theta = np.pi/180 # angular resolution in radians of the Hough grid
threshold = 15     # minimum number of votes (intersections in Hough grid cell)
min_line_length = 50 #minimum number of pixels making up a line
max_line_gap = 30    # maximum gap in pixels between connectable line segments
line_image = np.copy(image)*0 # creating a blank to draw lines on

# Run Hough on edge detected image
# Output "lines" is an array containing endpoints of detected line segments
lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)

# Iterate over the output "lines" and draw lines on a blank image
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

# Create a "color" binary image to combine with line image
color_edges = np.dstack((edges, edges, edges)) 

# Draw the lines on the edge image
lines_edges = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0) 
plt.imshow(lines_edges)
