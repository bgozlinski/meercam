import cv2 as cv
import numpy as np


class VideoCapture:

    def __init__(self, index: int = 0):
        self.capture = cv.VideoCapture(index)
        self.show_image = True

    def convert_to_gray(self, frame):
        frame = cv.cvtColor(src=frame, code=cv.COLOR_BGR2RGB)
        gray_frame_convert = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray_frame_convert = cv.GaussianBlur(src=gray_frame_convert, ksize=(5, 5), sigmaX=0)
        if self.show_image:
            cv.imshow('frame', frame)
            cv.imshow('gray', gray_frame_convert)

        return gray_frame_convert

    def frame_difference(self, frame, previous_frame):
        diff_frame_calculate = cv.absdiff(src1=previous_frame, src2=frame)
        if self.show_image:
            cv.imshow('diff', diff_frame_calculate)
        return diff_frame_calculate

    def start(self):
        previous_frame = None

        while True:

            _, frame = self.capture.read()
            frame = self.convert_to_gray(frame)

            if previous_frame is not None:
                self.frame_difference(frame, previous_frame)

            previous_frame = frame

            if cv.waitKey(30) == 27:
                break

        self.stop()

    def stop(self):
        self.capture.release()
        cv.destroyAllWindows()
