# # -*- coding: utf-8 -*-
# """
# Created on Wed Jan 18 00:35:08 2023
#
# @author: sethy
# """
#
# import cv2
#
# # Load an image
# img = cv2.imread("demo.jpg")
#
# # Create a window to display the image
# cv2.namedWindow("image")
#
# # Set a variable to store the previous point clicked
# prev_pt = (-1,-1)
#
# def click_event(event, x, y, flags, param):
#     global prev_pt
#     if event == cv2.EVENT_LBUTTONDOWN:
#         # Clear the previous point by drawing a white circle over it
#         if prev_pt[0] != -1 and prev_pt[1] != -1:
#             pass
#             # cv2.circle(img, prev_pt, 5, (255, 255, 255), -1)
#         # Draw a red circle at the current point clicked
#         # cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
#         prev_pt = (x, y)
#
# # Set the mouse callback function to handle clicks
# cv2.setMouseCallback("image", click_event)
#
# # Show the image and wait for user input
# while True:
#     cv2.imshow("image", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Close the window and exit
# cv2.destroyAllWindows()
import cv2
import  numpy as np
# Create a blank image
img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("Image", img)

# Define the starting and ending points for the line
start_point = (0, 0)
end_point = (0, 0)

# Create a function to handle mouse events
def draw_line(event, x, y, flags, param):
    global start_point, end_point

    # Check if the left mouse button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Remove the previous line
        img[:] = 0
        start_point = (x, y)
        end_point = (x+100, y-100)
        # Draw the new line
        cv2.line(img, start_point, end_point, (255, 0, 0), 2)
        cv2.imshow("Image", img)

# Set the mouse event callback
cv2.setMouseCallback("Image", draw_line)

# Wait for user input
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()