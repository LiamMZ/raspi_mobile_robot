from ObjectDetector import ObjectDetector
import cv2
import numpy as np
import pi_camera_stream
from pid_controller import PIController
from robot import Robot
import time

class ChaseCatBehavior:
    def __init__(self, robot):
        self.robot = robot
        self.center_x = 160
        self.center_y = 120
        self.min_size = 20
        self.pan_pid = PIController(proportional_constant=0.1, integral_constant=0.03)
        self.tilt_pid = PIController(proportional_constant=-0.1, integral_constant=-0.03)
        # current state
        self.running = False
        self.detector = ObjectDetector()
    
    def process_control(self):
        instruction = get_control_instruction()
        if instruction == 'start':
            self.running = True
        elif instruction == 'stop':
            self.running = False
        if instruction == 'exit':
            print("Stopping")
            exit()
    
    def find_object(self, original_frame):
        objects = self.detector.process_image(original_frame)
        largest = 0, (0,0,0,0) # area, x, y, w, h
        for (x,y,w,h) in objects[cat]:
            item_area = (w-x)*(h-y)
            if item_area> largest[0]:
                largest = item_area, (x,y,w,h)
        return largest[1] 

    def make_display(self, display_frame):
        """ Create display output, and put it on the queue"""
        encoded_bytes = pi_camera_stream.get_encoded_bytes_for_frame(display_frame)
        put_output_image(encoded_bytes)
    
    def process_frame(self, frame):
        # find the largest matching object
        (x,y,w,h) = self.find_object(frame)
        # draw a rect on original frame, then display new frame
        cv2.rectangle(frame, (x,y), (w,h), [255,0,0])
        self.make_display(frame)
        # yield the object details
        return x,y,w,h

    def run(self):
        # start camera
        camera = pi_camera_stream.setup_camera()
        # warm up time
        time.sleep(0.1)
        print("Setup COmplete")
        # Main loop
        for frame in pi_camera_stream.start_stream(camera):
            (x,y,w,h) = self.process_frame(frame)
            width = w-x
            height = h-y
            self.process_control()
            if self.running and h > self.min_size:
                # Pan
                pan_error = self.center_x - (x + (width/2))
                pan_value = self.pan_pid.get_value(pan_error)
                self.robot.set_pan(int(pan_value))
                # Tilt
                tilt_error = self.center_y - (y+(height/2))
                tilt_value = self.tilt_pid.get_value(tilt_error)
                self.robot.set_tilt(int(tilt_value))
                print("x: %d, y: %d, pan_error: %d, tilt_error: %d, pan_value: %.2f, tilt_value: %.2f" % (x, y, pan_error, tilt_error, pan_value, tilt_value))

if __name__ == "__main__":
    print("Setting up")
    behavior = ChaseCatBehavior(Robot())
    # process = start_server_process('color_track_behavior.html')
    try:
        behavior.run()
    finally:
        process.terminate()

