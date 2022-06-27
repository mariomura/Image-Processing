import cv2
import numpy as np

def get_filtered_image(image, filter):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    filtered = None
    if filter == 'NO_FILTER':
        filtered = image
    elif filter == 'COLORIZED':
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif filter == 'GRAYSCALE':
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif filter == 'GAUSSIAN_BLUR':
        width, height = img.shape[:2]
        if width > 500:
            k = (30, 30)
        elif width > 200 and width <=500:
            k = (15,15)
        else:
            k = (5,5)
        blur = cv2.blur(img, k)
        filtered = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
    elif filter == 'SHARPEN':
        kernel = np.array([[-1 , -1 , -1] , [-1 , 9 , -1] ,[-1 , -1 , -1]])
        sharpen = cv2.filter2D(img , -1 , kernel = kernel)
        filtered = cv2.cvtColor(sharpen, cv2.COLOR_BGR2RGB)
    elif filter == 'NOISE_REDUCTION':
        smoothing = cv2.medianBlur(img,3)
        filtered = cv2.cvtColor(smoothing, cv2.COLOR_BGR2RGB)
    elif filter == 'BILATERAL_FILTER':
        kernel = np.ones((5,5),np.float32)/25  
        bilateralFilter = cv2.bilateralFilter(img,9,75,75)
        filtered = cv2.cvtColor(bilateralFilter, cv2.COLOR_BGR2RGB)
    elif filter == 'THRESHOLD':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, filtered = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    

    return filtered
    