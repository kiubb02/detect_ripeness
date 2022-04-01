# Program detecting ripeness based on the fruits color hue

# %matplotlib inline
###############################################
#                    IMPORTS                  #
###############################################
from __future__ import division
import numpy as np
# import opencv module
import cv2
import matplotlib
from matplotlib import colors
from matplotlib import pyplot as plt
import pandas as pd


###############################################
#                  FUNCTIONS                  #
###############################################

def find_biggest_contour(image):
    # Copy to prevent modification
    image = image.copy()
    _, contours, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    print
    len(contours)

    # Isolate largest contour
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]

    mask = np.zeros(image.shape, np.uint8)
    cv2.drawContours(mask, [biggest_contour], -1, 255, -1)
    return biggest_contour, mask


# most of those functions are HELPER FUNCTIONS and not needed in further implementations
def show(image):
    # Figure size in inches
    plt.figure(figsize=(15, 15))

    # Show image, with nearest neighbour interpolation
    plt.imshow(image, interpolation='nearest')


def show_hsv(hsv):
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    show(rgb)


def show_mask(mask):
    plt.figure(figsize=(10, 10))
    plt.imshow(mask, cmap='gray')


def overlay_mask(mask, image):
    rgb_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    img = cv2.addWeighted(rgb_mask, 0.5, image, 0.5, 0)
    show(img)


###############################################
#                   PROGRAM                   #
###############################################

# define a video capture object
vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    print(frame.shape)
    m, n, r = frame.shape
    arr = frame.reshape(m * n, -1)
    df = pd.DataFrame(arr, columns=['b', 'g', 'r'])
    print(df)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # resize
    frame = cv2.resize(frame, None, fx=1 / 3, fy=1 / 3)
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    images = []
    for i in [0, 1, 2]:
         colour = hsv.copy()
         if i != 0: colour[:, :, 0] = 0
         if i != 1: colour[:, :, 1] = 255
         if i != 2: colour[:, :, 2] = 255
         images.append(colour)
    hsv_stack = np.vstack(images)
    rgb_stack = cv2.cvtColor(hsv_stack, cv2.COLOR_HSV2RGB)
    image_blur = cv2.GaussianBlur(frame, (7, 7), 0)
    image_blur_hsv = cv2.cvtColor(image_blur, cv2.COLOR_RGB2HSV)
    # 0-10 hue
    min_red = np.array([0, 100, 80])
    max_red = np.array([10, 256, 256])
    image_red1 = cv2.inRange(image_blur_hsv, min_red, max_red)
    #
    # # 170-180 hue
    min_red2 = np.array([170, 100, 80])
    max_red2 = np.array([180, 256, 256])
    image_red2 = cv2.inRange(image_blur_hsv, min_red2, max_red2)

    # how will we quit it in the actual application?

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

#
# show_rgb_hist(image)
#
# # Convert from RGB to HSV
# hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
#
# images = []
# for i in [0, 1, 2]:
#     colour = hsv.copy()
#     if i != 0: colour[:, :, 0] = 0
#     if i != 1: colour[:, :, 1] = 255
#     if i != 2: colour[:, :, 2] = 255
#     images.append(colour)
#
# hsv_stack = np.vstack(images)
# rgb_stack = cv2.cvtColor(hsv_stack, cv2.COLOR_HSV2RGB)
# show(rgb_stack)
#
# matplotlib.rcParams.update({'font.size': 16})
#
# show_hsv_hist(hsv)
#
# # Blur image slightly
# image_blur = cv2.GaussianBlur(image, (7, 7), 0)
# show(image_blur)
#
# image_cropped = image[100:300, 200:500]
# show(image_cropped)
# # image_rect_hsv = cv2.cvtColor(image_rect, cv2.COLOR_RGB2HSV)
# # show_hsv_hist(image_rect_hsv)
#
# image_blur_hsv = cv2.cvtColor(image_blur, cv2.COLOR_RGB2HSV)
#
# # 0-10 hue
# min_red = np.array([0, 100, 80])
# max_red = np.array([10, 256, 256])
# image_red1 = cv2.inRange(image_blur_hsv, min_red, max_red)
#
# # 170-180 hue
# min_red2 = np.array([170, 100, 80])
# max_red2 = np.array([180, 256, 256])
# image_red2 = cv2.inRange(image_blur_hsv, min_red2, max_red2)
#
# show_mask(image_red1)
# show_mask(image_red2)
# image_red = image_red1 + image_red2
# show_mask(image_red)
#
# # Clean up
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
#
# # image_red_eroded = cv2.morphologyEx(image_red, cv2.MORPH_ERODE, kernel)
# # show_mask(image_red_eroded)
#
# # image_red_dilated = cv2.morphologyEx(image_red, cv2.MORPH_DILATE, kernel)
# # show_mask(image_red_dilated)
#
# # image_red_opened = cv2.morphologyEx(image_red, cv2.MORPH_OPEN, kernel)
# # show_mask(image_red_opened)
#
# # Fill small gaps
# image_red_closed = cv2.morphologyEx(image_red, cv2.MORPH_CLOSE, kernel)
# show_mask(image_red_closed)
#
# # Remove specks
# image_red_closed_then_opened = cv2.morphologyEx(image_red_closed, cv2.MORPH_OPEN, kernel)
# show_mask(image_red_closed_then_opened)
#
# big_contour, red_mask = find_biggest_contour(image_red_closed_then_opened)
# show_mask(red_mask)
#
# # Centre of mass
# moments = cv2.moments(red_mask)
# centre_of_mass = int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00'])
# image_with_com = image.copy()
# cv2.circle(image_with_com, centre_of_mass, 10, (0, 255, 0), -1, cv2.LINE_AA)
# show(image_with_com)
#
# # Bounding ellipse
# image_with_ellipse = image.copy()
# ellipse = cv2.fitEllipse(big_contour)
# cv2.ellipse(image_with_ellipse, ellipse, (0,255,0), 2)
# show(image_with_ellipse)
#
#