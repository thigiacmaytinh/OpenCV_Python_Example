import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time

## Make canvas and set the color
emptyMat = np.zeros((200, 700,3), np.uint8)

background = 73, 73, 73
cv2.rectangle(emptyMat, (0,0), (700, 200), background, -1)

## Use cv2.FONT_HERSHEY_XXX to write English.
text = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime()) 

color = 204, 204, 204
cv2.putText(emptyMat,  text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 1, cv2.LINE_AA)

## load font
fontpath = "./Exo Soft W05 Medium.otf"
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(emptyMat)
draw = ImageDraw.Draw(img_pil)
draw.text((50, 100),  "THE FALCON HEAVY FLIGHT", font = font, fill = (204, 204, 204, 0))
img = np.array(img_pil)

## Display 
cv2.imshow("result", img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("result.png", img)