import cv2

class ObjectDetector:
    def __init__(self, weights = '/home/pi/workspace/overwatch/object_detection/src/models/frozen_inference_graph.pb', 
                        config = '/home/pi/workspace/overwatch/object_detection/src/models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt',
                        size = (300,300), classes = '/home/pi/workspace/overwatch/object_detection/src/models/mobilenet_classnames.txt'):
        self.net = cv2.dnn.readNetFromTensorflow(weights, config)
        self.size = size
        self.classes = {}
        with open(classes) as f:
            lines = f.readlines()
            self.classes = {int(line.split(" ", 1)[0]):line.split(" ", 1)[1] for line in lines}


    def id_class_name(self, class_id):
        return self.classes.get(class_id)

    def process_image(self, image):
        # image =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_height, image_width, _ = image.shape

        self.net.setInput(cv2.dnn.blobFromImage(image, size=self.size, swapRB=True))

        output = self.net.forward()
        detections = {}
        for detection in output[0, 0, :, :]:
            confidence = detection[2]
            if confidence > 0.5:
                class_id = int(detection[1])
                class_name = self.id_class_name(class_id)
                center_x = ((detection[3] * image_width) + (detection[5] * image_width))/2
                center_y = ((detection[4] * image_height) + (detection[6] * image_height))/2
                if detections.get(class_name, None) is None:
                    detections[class_name] = [(center_x, center_y)]
                else:
                    detections[class_name].append((center_x, center_y))
        
        return detections