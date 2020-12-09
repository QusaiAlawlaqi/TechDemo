#Name: Qusai Alawlaqi
# Technical Demostration

import picamera
from datetime import datetime
from time import sleep

# Setting The File Name
filePath = "/home/pi/Desktop/TechDemo/Videos/"
currentTime = datetime.now()
pictureTime = currentTime.strftime("%Y-%m-%d-%H-%M-%S")
pictureName = pictureTime + '.h264'
pictureFullName = filePath + pictureName

# Setup The Camera
print("Starting Recording")
with picamera.PiCamera() as camera:
    camera.start_recording(pictureFullName)
    sleep(5)
    camera.stop_recording()
    
print("Stopped Recording")