#Name: Qusai Alawlaqi
# Technical Demostration

import picamera
from datetime import datetime

# Setting The File Name
filePath = "/home/pi/Desktop/TechDemo/Images/"
currentTime = datetime.now()
pictureTime = currentTime.strftime("%Y-%m-%d-%H-%M-%S")
pictureName = pictureTime + '.jpg'
pictureFullName = filePath + pictureName

# Setup The Camera

with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture(pictureFullName)
    
print("Picture taken")
