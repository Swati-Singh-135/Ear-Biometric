import cv2
import numpy as np

def resizeImage(img,size):
    '''
    This funtion will resize the image while maintaining the proportionality of the image.\n
    After applying this funtion \n
    \t max(img.width,img.height)=size \n
    '''
    w = int(img.shape[1])
    h = int(img.shape[0])
    if w>h:
        h = int(min(h,size*h/w))
        w = int(min(size,w))
    else:
        w = int(min(w,size*w/h))
        h = int(min(size,h))
    img = cv2.resize(img,(w,h))
    return img



if __name__=='__main__':
    img_path = "img/195_.jpg"
    img = cv2.imread(img_path)
    # resizing the image while maintaining the proportionnality
    img = resizeImage(img,700)
    # applying gaussian blur to reduce noise
    img = cv2.GaussianBlur(img,(9,9),0) # odd size matrix is used
    # applying canny edge detection
    canny = cv2.Canny(img,60,120)

    # saving the canny image
    # cv2.imwrite('canny/'+img_path, canny)
    cv2.imshow("Original", img)
    cv2.imshow("Gaussian Blur", img)
    cv2.imshow("canny", canny)
    cv2.waitKey(0)