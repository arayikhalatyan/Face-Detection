import cv2 as cv
import utils as ut

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

class Detector:
    
    def __init__(self, frame):
        self.frame = frame
        self.gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
    def detect_face(self,file):
        faces = face_cascade.detectMultiScale(self.gray, 1.3, 10)
        for (x,y,w,h) in faces:
            #cv.rectangle(self.frame,(x,y),(x+w,y+h),(255,0,0),2)
            if file == 'Aram.png':
                x = int(x - 70)
                y = int(y - 100)
                w = int(w + 130)
                h= int(h + 200)
            ut.overlay_sunglasses(self.frame,x,y,w,h,file)

   
    def detect_eyes(self):
        faces = face_cascade.detectMultiScale(self.gray, 1.3, 10)
        l = 0
        for (x,y,w,h) in faces:
            roi_gray = self.gray[y:y+h, x:x+w]
            roi_color = self.frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            #overlay_sunglasses(self.frame,int(x),int(y),int(w),int(h),'sunglasses.png')
            for (ex,ey,ew,eh) in eyes:
                if l >= 2:
                    break
                else:
                    cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    ut.overlay_sunglasses(self.frame,int(x),int(y),int(w),int(h),'filter.jpg')
                    l += 1
       