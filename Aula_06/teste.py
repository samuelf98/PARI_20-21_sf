import cv2
import numpy as np

drawing = False  # True when mouse down
mode = True  # Draw rectangle when True
ix, iy = -1, -1


# Mouse response function
def OnMouseAction(event, x, y, flags, param):
    global ix, iy, drawing, mode
    # img1 = img.copy() #Image deep copy
    # event indicates whether the mouse moves
    # flags indicates whether the mouse is pressed
    if event == cv2.EVENT_LBUTTONDOWN:  # Click the left key to return to the starting position coordinate
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:  # Draw a graph when the left key is pressed and moved
        if drawing == True:
            if mode == True:  # Draw a solid green rectangle
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 20, (255, 0, 0), 3)  # Circle, blue
    elif event == cv2.EVENT_LBUTTONUP:  # Release left key
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)  # Draw a white red rectangle
        cv2.circle(img, (x, y), 34, (255, 255, 255), 3)  # Circle, white
    elif event == cv2.EVENT_LBUTTONDBLCLK:  # Double click the left mouse button to trigger the event
        cv2.circle(img, (x, y), 100, (255, 255, 0), 3)  # Circle, green


# Create window and bind mouse response function
# img = cv2.imread('image.jpg')
img = np.ones((512, 512, 3), np.uint8)  # Create a black background
cv2.namedWindow('image')
cv2.setMouseCallback('image', OnMouseAction)
print('done')
while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('s'):  # s key preservation
        cv2.imwrite('new_image.png', img)
        print("Picture saved!")
    elif k == ord('r'):
        mode = True
    elif k == ord('c'):
        mode = False
    elif k == ord('q'):  # q key exit
        break
