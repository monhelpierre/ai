import cv2
import modules.Atividade1 as a1

def main():
    img = cv2.imread('./ressources/5.jpg', 0)
    a1.histogram(img)
    a1.histogram(img, 1)

if __name__ == '__main__':
    main()
    cv2.waitKey(0)