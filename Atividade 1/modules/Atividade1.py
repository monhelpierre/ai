import cv2
from matplotlib import pyplot as plt

def histogram(img, method = 0):
    if method == 0:
        plt.hist(img.ravel(), 256, [0, 256])
    if method == 1:
        histg = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(histg)
    plt.show()
