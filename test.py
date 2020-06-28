import cv2
import numpy as np
import pickle

with open('shapes.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
    [heartContour,circle,plusInCircle] = pickle.load(f)

img = cv2.imread("./images/20.PNG")
print('Original Dimensions : ', img.shape)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red0 = np.array([0, 150, 180])
upper_red0 = np.array([10, 255, 255])
lower_red1 = np.array([170, 150, 180])
upper_red1 = np.array([180, 255, 255])

mask0 = cv2.inRange(hsv, lower_red0, upper_red0)
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
res = cv2.bitwise_and(img, img, mask=mask0 | mask1)
imgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
contours, hierarchy = cv2.findContours(
    imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
newcontour = []
print('contours',len(contours))
for i,n in enumerate(contours):
    area = cv2.contourArea(n)
    if area > 100:
        print(i,area)
        newcontour.append(n)
        ret = cv2.matchShapes(n, heartContour, 1, 0.0)
        if ret < 0.02:
            print('heartContour', ret)
            continue

        ret = cv2.matchShapes(n, circle, 1, 0.0)
        if ret < 0.02:
            childArea = cv2.contourArea(contours[i+1])
            if hierarchy[0][i][2] == i+1 and childArea < area/2:
                ret = cv2.matchShapes(contours[hierarchy[0][i][2]], plusInCircle, 1, 0.0)
                if ret < 0.15:
                    print('plus',ret)
                

img = cv2.drawContours(img, newcontour, -1, (0, 255, 0), 1)


# with open('shapes.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
#     pickle.dump([newcontour[1], newcontour[2], newcontour[3]], f)
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imshow('output', img)
# print(hierarchy)
cv2.waitKey(0)
cv2.destroyAllWindows()
