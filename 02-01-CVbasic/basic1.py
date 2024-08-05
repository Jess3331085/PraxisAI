# Accessing opencv module
import cv2
import imutils

# load the image
image = cv2.imread("//Users//jacyndharakhma//PraxisAI//astyy.webp")

# check image size 
height,width,depth = image.shape
print("image size: ", height,width,depth)

# show the image 
cv2.imshow("astyy", image)
cv2.waitKey(0)

#resize the image to 200x200px, ignoring aspect ratio
resize = cv2.resize(image, (200, 200))
cv2.imshow("fixed resizing", resize)
cv2.waitKey(0)

# crop the image 
cropped_image = image[160:280, 160:280]
cv2.imshow("cropped image", cropped_image)
cv2.waitKey(0)

# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output = image.copy()
cv2.line(output, (0, 0), (300, 300), (0, 255, 255), 5)
cv2.imshow("Line", output)

cv2.line(output, (300, 0), (0, 200), (255, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)


# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

# draw a 2px thick red rectangle surrounding the face
output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# draw green text on the image
output = image.copy()
cv2.putText(output, "sqiudward", (10, 25), 
cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)

# applying edge detection we can find the outlines of objects in
# images
edged = cv2.Canny(gray, 30, 150)
cv2.imshow("Edged", edged)
cv2.waitKey(0)




