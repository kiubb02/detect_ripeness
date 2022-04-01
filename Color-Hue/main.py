# Python code for Color Detetction ==> Ripe Strawberries are red
import cap as cap
import numpy as np
import cv2

# Capturing video through webcam
webcam = cv2.VideoCapture(0)

# Start a while loop
while (1):

    # Reading the video from the
    # webcam in image frames
    _, imageFrame = webcam.read()

    # Convert the imageFrame in
    # BGR(RGB color space) to
    # HSV(hue-saturation-value)
    # color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # images = []
    # for i in [0, 1, 2]:
     #   colour = hsvFrame.copy()
     #   if i != 0: colour[:, :, 0] = 0
     #   if i != 1: colour[:, :, 1] = 255
     #   if i != 2: colour[:, :, 2] = 255
     #   images.append(colour)

    # hsv_stack = np.vstack(images)
    # rgb_stack = cv2.cvtColor(hsv_stack, cv2.COLOR_HSV2RGB)

    # image_blur = cv2.GaussianBlur(imageFrame, (7, 7), 0)
    # image_blur_hsv = cv2.cvtColor(image_blur, cv2.COLOR_RGB2HSV)

    # Set range for red color and
    # define mask
    # 0-10 hue
    # min_red = np.array([0, 100, 80])
    # max_red = np.array([10, 256, 256])
    # image_red1 = cv2.inRange(image_blur_hsv, min_red, max_red)

    # 170-180 hue
    # min_red2 = np.array([170, 100, 80])
    # max_red2 = np.array([180, 256, 256])
    # image_red2 = cv2.inRange(image_blur_hsv, min_red2, max_red2)

    # we want it to be pure red and not only a bit of a hue of red
    # red_mask = image_red1 + image_red2

    # more sensitive
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)


    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
    # image_red_closed = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)
    # image_red_closed_then_opened = cv2.morphologyEx(image_red_closed, cv2.MORPH_OPEN, kernel)

    kernal = np.ones((5, 5), "uint8")

    # For red color
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame,
                              mask=red_mask)

    # Creating contour to track red color
    contours, hierarchy = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (0, 0, 255), 2)

            cv2.putText(imageFrame, "Ripe Strawberry", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))

    # Program Termination
    cv2.imshow("Strawberry detection by Color", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
