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
        _, thresh = cv.threshold(diff_frame_calculate, 25, 255, cv.THRESH_BINARY)
        if self.show_image:
            cv.imshow('diff', diff_frame_calculate)
        return diff_frame_calculate

    def threshold(self, frame_delta):
        _, thresh = cv.threshold(frame_delta, 25, 255, cv.THRESH_BINARY)
        thresh = cv.dilate(thresh, None, iterations=2)
        if self.show_image:
            cv.imshow('thresh', thresh)
        return thresh

    def draw_dot(self, frame, raw_frame):
        contours, _ = cv.findContours(image=frame.copy(), mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv.contourArea(contour) < 3500:
                continue
            x, y, w, h = cv.boundingRect(contour)
            # cv.rectangle(img=raw_frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=1)
            cv.circle(img=raw_frame, center=(x + w // 2, y + h // 2), radius=5, color=(0, 0, 255), thickness=-1)
        if self.show_image:
            cv.imshow('drawing', raw_frame)

    def start(self):
        previous_frame = None

        while True:

            _, raw_frame = self.capture.read()
            frame = self.convert_to_gray(raw_frame)

            if previous_frame is not None:
                frame_delta = self.frame_difference(frame, previous_frame)
                thresh = self.threshold(frame_delta)
                self.draw_dot(thresh, raw_frame)

            previous_frame = frame

            if cv.waitKey(30) == 27:
                break

        self.stop()

    def stop(self):
        self.capture.release()
        cv.destroyAllWindows()
