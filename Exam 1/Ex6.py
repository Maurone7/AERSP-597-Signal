import cv2
import numpy as np
import matplotlib.pyplot as plt

# Lists to store the points
listPoints = []

POINT_SIZE = 5
TEXT_RATIO = 1.5
LINE_THICKNESS = 5
 
def drawCoordinates(action, x, y, flags, userdata):
  global listPoints

  # Action to be taken when left mouse button is released
  if action==cv2.EVENT_LBUTTONUP:
    # Mark the vertex
    listPoints.append((x,y))
    cv2.circle(source, (x,y), 1, (0,0,255), POINT_SIZE, cv2.LINE_AA )
 
  if len(listPoints) >=2:
    p1 = listPoints[-1]
    p2 = listPoints[-2]
    cv2.line(source, p1, p2 , (0,0,255), LINE_THICKNESS)

source = cv2.imread("/Users/mauro/Library/CloudStorage/OneDrive-ThePennsylvaniaStateUniversity/597-Signal/Exam 1/Im8.png", 1)
img_copy = source.copy()
img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawCoordinates)

cv2.putText(source,"Select the Points and press 'Space' to complete the last line",
              (50, 50),  cv2.FONT_HERSHEY_SIMPLEX, TEXT_RATIO, (0,0,255), 4)

k = 0
# loop until escape character is pressed
while k!=27 :
  
  cv2.imshow("Window", source)
#   cv2.putText(source,'''Click on the image to get the coordinates, press ESC to exit''' ,
#               (10,30), cv2.FONT_HERSHEY_SIMPLEX, 
#               0.7,(255,255,255), 2 );
  k = cv2.waitKey(20) & 0xFF

  if k == 32:
    p1 = listPoints[-1]
    p2 = listPoints[0]

    cv2.line(source, p1, p2 , (0,0,0), LINE_THICKNESS)

  if k==99:
    source = dummy.copy()
 
cv2.destroyAllWindows()

listPoints = sorted(listPoints, key=lambda x: x[0])
width_AD = np.sqrt((listPoints[0][0] - listPoints[1][0])**2 + (listPoints[0][1] - listPoints[1][1])**2)
width_BC = np.sqrt((listPoints[2][0] - listPoints[3][0])**2 + (listPoints[2][1] - listPoints[3][1])**2)
max_height = max(int(width_AD), int(width_BC))

height_AB = np.sqrt((listPoints[0][0] - listPoints[2][0])**2 + (listPoints[0][1] - listPoints[2][1])**2)
height_CD = np.sqrt((listPoints[1][0] - listPoints[3][0])**2 + (listPoints[1][1] - listPoints[3][1])**2)
max_width = max(int(height_AB), int(height_CD))

input_points = np.array([listPoints[0], listPoints[1], listPoints[2], listPoints[3]], dtype='float32')
output_points = np.array([[0,0], [0, max_height-1], [max_width-1,max_height-1], [max_width-1,0]], dtype='float32')

warped = cv2.getPerspectiveTransform(input_points, output_points)
warped = cv2.warpPerspective(source, warped, (max_width, max_height), flags=cv2.INTER_LINEAR)

cv2.imshow("Warped", warped)
cv2.waitKey(0)

warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
# Apply adaptive thresholding to the cropped image
binary_image = cv2.adaptiveThreshold(warped, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("Binary Image", binary_image)
cv2.waitKey(0)
