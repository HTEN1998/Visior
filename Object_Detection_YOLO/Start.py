import cv2
import numpy as np
from time import sleep


class Start:
    net = 0
    classes = []
    output_layers = 0
    img = "test_image.jpeg"
    height = 0
    width = 0
    channel = 0

    def __init__(self):
        self.net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        print("Net Read")

        with open("coco.names", "r") as f:
            self.classes = [line.strip() for line in f.readlines()]

        print("classes -> {classes}")

        layer_names = self.net.getLayerNames()
        print("layer names {layer_names}")

        self.output_layers = [layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        print("output_layers {output_layers}")

    def image_load(self, path):
        self.img = cv2.imread(path)
        self.img = cv2.resize(self.img, None, fx=2, fy=2)
        self.height, self.width, self.channel = self.img.shape

    # cv2.imshow("Test Image", self.img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    def extract_features(self):
        blob = cv2.dnn.blobFromImage(self.img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.detect_Objects(blob)

    def detect_Objects(self, blob):
        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)
        print("output {outs}")

        boxes = []
        confidence_ = []
        class_id_ = []

        for out in outs:
            for detected in out:

                scores = detected[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.0:
                    center_x = int(detected[0] * self.width)
                    center_y = int(detected[1] * self.height)

                    w = int(detected[2] * self.width)
                    h = int(detected[3] * self.height)

                    # cv2.circle(self.img ,(center_x , center_y) , 12 ,(0,255,0),1)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidence_.append(int(float(confidence) * 100))
                    class_id_.append(class_id)

                # cv2.rectangle(self.img ,(x,y),(x+w , y+h ),(0,255,0),1)
        indexes = cv2.dnn.NMSBoxes(boxes, confidence_, 0.3, 0.2)
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(self.classes[class_id_[i]])
                print(f"labels {label}")
                cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 1)
                cv2.putText(self.img, label, (x, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        cv2.imshow("Test Image", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


class VideoObject:

    def detect_objects(self):
        net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        print("Nets read in video ...")

        classes = []
        with open("coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]
        print("Classes loaded ...")

        layer_names = net.getLayerNames()

        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        print("Fetched Output Layer names ...")

        cap = cv2.VideoCapture(0)

        print("Opencv Initalized ...")

        while True:
            ret, frame = cap.read()
            img = cv2.resize(frame, None, fx=1, fy=1)
            height, width, channel = img.shape

            blob = cv2.dnn.blobFromImage(img, 0.00392, (416,416), (0, 0, 0), True, crop=False)
            print("Blobs detected ...")

            net.setInput(blob)
            outs = net.forward(output_layers)

            boxes = []
            confidence_ = []
            class_id_ = []

            for out in outs:
                for detected in out:

                    scores = detected[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]

                    if confidence > 0.0:
                        center_x = int(detected[0] * width)
                        center_y = int(detected[1] * height)

                        w = int(detected[2] * width)
                        h = int(detected[3] * height)

                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)
                        boxes.append([x, y, w, h])
                        confidence_.append(int(float(confidence) * 100))
                        class_id_.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidence_, 0.3, 0.2)
            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    label = str(classes[class_id_[i]])
                   # print(f"labels {label}")
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
                    cv2.putText(img, label, (x, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            cv2.imshow("Test video  ", img)
            print("Showing image ")
            if cv2.waitKey(27) & 0XFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()



    def video_(self):
        cap = cv2.VideoCapture(0)
        print("Started video cap ")

        while True:
            ret, frame = cap.read()
            cv2.imshow("Test video  ", cv2.resize(frame, None, fx=1.5, fy=1.5))
            print("Showing image ")
            if cv2.waitKey(27) & 0XFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    vo = VideoObject()
    #vo.video_()
    vo.detect_objects()

    # s = Start()
    # s.image_load("test_image2.jpg")
    # s.image_load("test_image3.jpg")
    # s.image_load("test_image_blur.jpg")
    # s.extract_features()
