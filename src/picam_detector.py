import pi_camera_stream
from ObjectDetector import ObjectDetector
import time

camera = pi_camera_stream.setup_camera()
detector = ObjectDetector()
# allow the camera to warmup
time.sleep(0.1)
for frame in pi_camera_stream.start_stream(camera):
    output = detector.process_image(frame)
    print(output)