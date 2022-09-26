import cv2
import numpy as np
from tasks import AlvinsSchatzsuche


def main():
    oAlvinsSchatzsuche = AlvinsSchatzsuche()
    #oAlvinsSchatzsuche.calculate_center()
    oAlvinsSchatzsuche.recognize_ropes_of_image()


    # ranges = {
    #     "red": ([0, 0, 128], [60, 60, 255]),  # B G R
    #     "yellow": ([30, 100, 140], [70, 200, 220]),  # B G R
    #     "blue": ([90, 0, 0], [255, 50, 50]),  # B G R
    # }
    # image = cv2.imread('assets/alvins-schatzsuche-1.png')
    
    # for key in ranges.keys():
    #     lowerRange = np.array(ranges[key][0], dtype="uint8")
    #     upperRange = np.array(ranges[key][1], dtype="uint8")
 
 
    #     mask = cv2.inRange(image, lowerRange, upperRange)
    #     output = cv2.bitwise_and(image, image, mask=mask)
 
    #     # show the images
    #     cv2.imshow(key, output)
    #     cv2.waitKey(0)

    # cv2.destroyAllWindows()

    
    # cv2.imshow('Original Image', image)
    # cv2.waitKey(0)


if __name__ == "__main__":
    main()
