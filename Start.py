import cv2
import numpy as np
from time import sleep


class Start:
	net = 0
	classes = []
	output_layers = 0
	img = "test_image.jpeg"
	height = 0
	width  = 0
	channel = 0


	def __init__(self):
		self.net = cv2.dnn.readNet("yolov3.weights" , "yolov3.cfg")
		print("Net Read")

		with open("coco.names","r") as f:
			self.classes = [line.strip() for line in f.readlines()]

		print("classes -> {classes}")

		layer_names = self.net.getLayerNames()
		print("layer names {layer_names}")

		self.output_layers = [layer_names[i[0]-1] for i in self.net.getUnconnectedOutLayers()]
		print("output_layers {output_layers}")	



	def	image_load(self, path):
		self.img = cv2.imread(path)
		self.img = cv2.resize(self.img, None ,fx = 1 , fy=1)
		self.height,self.width,self.channel = self.img.shape
		#cv2.imshow("Test Image", self.img)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()


	def extract_features(self):
		blob = cv2.dnn.blobFromImage(self.img , 0.00392 , (416 , 416) ,(0,0,0) ,True ,crop =False)
		self.detect_Objects(blob)


	def detect_Objects(self,blob):
		self.net.setInput(blob)
		outs = self.net.forward(self.output_layers)
		print("output {outs}")

		boxes = []
		confidence_ = []
		class_id_ = []

		inde
		for out in outs:
			for detected in out:
				scores = detected[5:]
				class_id = np.argmax(scores)
				confidence = scores[class_id]
				indexes = self.net.NMS
				if confidence > 0.3:
					center_x = int(detected[0]* self.width)
					center_y = int(detected[1]* self.height)

					w = int(detected[2]* self.width)
					h = int(detected[3]* self.height)

					
					#cv2.circle(self.img ,(center_x , center_y) , 12 ,(0,255,0),1)
					x = int(center_x - w / 2)
					y = int(center_y - h / 2)
					boxes.append([x,y,w,h])
					confidence_.append(int(float(confidence)*100))
					class_id_.append(class_id)

					#cv2.rectangle(self.img ,(x,y),(x+w , y+h ),(0,255,0),1)

		for i in range(len(boxes)):
			x , y ,w, h = boxes[i]
			label = str(self.classes[class_id_[i]])
			print(f"labels {label}")
			cv2.rectangle(self.img ,(x,y),(x+w , y+h ),(0,255,0),1)
			cv2.putText(self.img , label , (x ,y+30 ), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0),2)

		cv2.imshow("Test Image", self.img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()





if __name__ == "__main__":
	s = Start()
	s.image_load("C:/Users/user/Desktop/Official_IMage.jpg")
	s.extract_features()