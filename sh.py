import cv2
import numpy as np


paper = np.zeros([640, 640, 1], dtype = np.uint8)

paper[300:340, 200:280] =255
paper[350:400, 190:210] = 255
paper[350:370, 270:290] = 255
paper[400:440, 200:280] = 255
paper[440:490, 270:290] = 255
paper[470:490, 190:210] = 255
paper[490:530, 200:280] = 255
paper[340:530, 320:340] = 255
paper[400:440, 340:390] = 255
paper[440:530, 380:400] = 255

cv2.imshow('Paper', paper)
cv2.waitKey()
cv2.destroyAllWindows()

