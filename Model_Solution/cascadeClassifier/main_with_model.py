# Once you have trained the model using the cascade trainger and providing all the positive and negative images then
# Use this for using the trained model

# testing model on static image
# since not enough data => model is rlly bad

import cv2
import cap as cap

# Capturing video through webcam
webcam = cv2.VideoCapture(0)

# load the required model
model_cascade = cv2.CascadeClassifier('data/images/classifier/cascade.xml')

# Start a while loop
while (1):
    # Reading the video from the
    # webcam in image frames
    _, imageFrame = webcam.read()

    # Converting image to grayscale
    gray_img = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2GRAY)

    strawberry = model_cascade.detectMultiScale(gray_img, 1.1, 9)

    for (x, y, w, h) in strawberry:
        cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Program Termination
    cv2.imshow("Strawberry detection by Cascade Model", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break



# Reading the image
# img = cv2.imread('data/images/p/How-Many-Strawberries-Do-Strawberry-Plants-Produce-3.jpg')

# Converting image to grayscale
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Loading the required haar-cascade xml classifier file
# haar_cascade = cv2.CascadeClassifier('data/images/classifier/cascade.xml')

# Applying the face detection method on the grayscale image
# faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

# Iterating through rectangles of detected faces
# for (x, y, w, h) in faces_rect:
#    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
