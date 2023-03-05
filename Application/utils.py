import cv2

def overlay_sunglasses(img,x,y,w,h,file):
    try:
        imgMustache = cv2.imread(file,-1)
        mustache = cv2.resize(imgMustache, (w,h))
        orig_mask = mustache[:,:,3]
        orig_mask_inv = cv2.bitwise_not(orig_mask)
        mustache = mustache[:,:,0:3]
        tam = mustache.shape
        roi = img[y:y+tam[0], x:x+tam[1]]
        roi_bg = cv2.bitwise_and(roi,roi,mask = orig_mask_inv)
        roi_fg = cv2.bitwise_and(mustache,mustache,mask = orig_mask)
        dst = cv2.add(roi_bg,roi_fg)
        img[y:y+tam[0], x:x+tam[1]] = dst
        return dst
    except:
        return 0