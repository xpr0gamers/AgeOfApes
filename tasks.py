from re import S
import cv2
import numpy as np


class Task():

    def __init__(self):
        pass

    def calculate_center_of_image(self):
        image = cv2.imread('assets/alvins-schatzsuche-1.png')
        nHeight = np.size(image, 0)
        nWidth = np.size(image, 1)
        nX1 = (int)(nWidth / 2)
        nX2 = (int)(nWidth / 2)
        nY1 = 0
        nY2 = nHeight
        nLineThickness = 3
        cv2.line(image, (nX1, nY1), (nX2, nY2), (0, 255, 0), nLineThickness)
        # show the images
        cv2.imshow("", image)
        cv2.waitKey(0)


class Nebel(Task):

    def __init__(self):
        super(Task, self).__init__()

    def is_nebel_main(self):
        #https://stackoverflow.com/questions/7853628/how-do-i-find-an-image-contained-within-an-image
        #search image in image
        oImage = cv2.imread('assets/nebel-racketenwrack-weiter.png')
        oImageTemplate = cv2.imread('assets/nebel-main.png')
        a_Res = cv2.matchTemplate(oImage, oImageTemplate, cv2.TM_CCOEFF_NORMED)
        n_Threshold = 0.8
        a_Loc = np.where(a_Res >= n_Threshold)
        n_count_matches = 0
        for a_Pt in zip(*a_Loc[::-1]):  # Switch collumns and rows
            n_count_matches += 1
        return n_count_matches >= 1

    def is_job_possible(self, oCropImage):
        #prüben ob die Farbe Rot in einem bestimmten Bereich vorhanden ist
        aRedLower = np.array([0, 0, 128])
        aRedUpper = np.array([60, 60, 255])
        oMask = cv2.inRange(oCropImage, aRedLower, aRedUpper)
        if np.sum(oMask) > 0:
            return True
        else:
            return False

    def is_racketenwrack_possible(self):
        #prüben ob die Farbe Rot in einem bestimmten Bereich vorhanden ist
        oImage = cv2.imread('assets/nebel-main.png')
        #oImage = cv2.imread('assets/nebel-main-rackenwrack-not-possible.png')
        nHeight = np.size(oImage, 0)
        nWidth = np.size(oImage, 1)
        nXCenter = (int)(nWidth / 2)
        nYCenter = (int)(nHeight / 2)
        oCropImage = oImage[nYCenter - 50:nYCenter + 30,
                            (int)(nXCenter + (nXCenter / 2)):nWidth - 300]
        return self.is_job_possible(oCropImage)

    def is_ubahn_eingang_possible(self):
        #prüben ob die Farbe Rot in einem bestimmten Bereich vorhanden ist
        oImage = cv2.imread('assets/nebel-main.png')
        nHeight = np.size(oImage, 0)
        nWidth = np.size(oImage, 1)
        nXCenter = (int)(nWidth / 2)
        nYCenter = (int)(nHeight / 2)
        oCropImage = oImage[nYCenter + 100:nYCenter + 350,
                            (int)(nXCenter + (nXCenter / 2)):nWidth - 300]
        return self.is_job_possible(oCropImage)


class AlvinsSchatzsuche(Task):

    def __init__(self):
        super(Task, self).__init__()

    def ropes_to_array(self, oRangeRopes):
        #unendliche Zeilen, 5 Spalten
        #aResult = [0][0, 0, 0, 0, 0]
        pass

    def recognize_ropes_of_image(self):
        oImage = cv2.imread('assets/alvins-schatzsuche-1.png')

        def helper_recognize(aLower, aUpper):
            oMask = cv2.inRange(oImage, np.array(aLower, dtype="uint8"),
                                np.array(aUpper, dtype="uint8"))
            return cv2.bitwise_and(oImage, oImage, mask=oMask)

        oRanges = {
            "red": ([0, 0, 128], [60, 60, 255]),  # B G R
            "yellow": ([30, 100, 140], [70, 200, 220]),  # B G R
            "blue": ([90, 0, 0], [255, 50, 50]),  # B G R
        }
        oResult = {
            "oImageRed":
            helper_recognize(oRanges["red"][0], oRanges["red"][1]),
            "oImageBlue":
            helper_recognize(oRanges["blue"][0], oRanges["blue"][1]),
            "oImageYellow":
            helper_recognize(oRanges["yellow"][0], oRanges["yellow"][1])
        }
        # show the images
        cv2.imshow("fef", oResult["oImageRed"])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return oResult
