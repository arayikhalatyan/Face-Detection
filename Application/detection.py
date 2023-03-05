import cv2
import classdetection as det
import utils as ut1


def nothing(x):
    pass


cap = cv2.VideoCapture(0)
image = cv2.imread('image.jpg')
image2 = cv2.imread('war.png')
image2=cv2.resize(image2, (720, 1230))

cv2.namedWindow('camera')



#switch = '0 : OFF \n1 : ON'
cv2.createTrackbar('face', 'camera' ,0,3,nothing)
cv2.createTrackbar('eyes', 'camera' ,0,1,nothing)
#cv2.createTrackbar('mouth', 'camera' ,0,1,nothing)
cv2.createTrackbar('thres', 'camera' ,0,2,nothing)
#cv2.createTrackbar('canny', 'camera' ,0,1,nothing)
cv2.createTrackbar('blend', 'camera' ,0,255,nothing)
cv2.createTrackbar('blend2', 'camera' ,0,1,nothing)
cv2.createTrackbar('aim', 'camera' ,0,1470,nothing)

while True:
        
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    th = cv2.getTrackbarPos('thres','camera')
    face = det.Detector(frame)
    f = cv2.getTrackbarPos('face','camera')
    e = cv2.getTrackbarPos('eyes','camera')
    #m = cv2.getTrackbarPos('mouth','camera')
    #can = cv2.getTrackbarPos('canny','camera')
    blend = cv2.getTrackbarPos('blend','camera')
    blend2 = cv2.getTrackbarPos('blend2','camera')
    aim = cv2.getTrackbarPos('aim','camera')
    #img = cv2.add(frame, image)
    
    
    if f==1:
        face.detect_face('Aram.png')
    elif f==2:
        face.detect_face('filter3.png')
    elif f==3:
        face.detect_face('mask.png')
        
    if e==1: 
        face.detect_eyes()
        
    #if m==1: 
    #    face.detect_mouth()
        
    if th == 1:
        frame = cv2.adaptiveThreshold(gray ,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)
    
    if th == 2:
        frame = cv2.Canny(frame,150,100)

    if blend != 0 and th == 0:
        frame = cv2.addWeighted(frame, 1-blend/100, image, blend/100, 0)
    if blend2 == 1 and th == 0:
        ut1.overlay_sunglasses(frame,0,0,1280,720,'war.png')
    if aim != 0 and th == 0:
        ut1.overlay_sunglasses(frame,aim,210,350,350,'target2.png')
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cv2.imshow('camera',frame)

cap.release()
cv2.destroyAllWindows()