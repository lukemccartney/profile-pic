import cv2
import numpy as np
import math

def main():
    count = 0
    vid = cv2.VideoCapture(0)
    while(True):
        ret, frame = vid.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        edged = cv2.Canny(frame, 0, 255)
        cv2.imshow('frame', edged)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()