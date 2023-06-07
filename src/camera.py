import cv2 as cv
import numpy as np


class VideoCapture:
    """
    A class used to capture video using OpenCV

    ...

    Attributes
    ----------
    capture : cv2.VideoCapture
        a OpenCV video capture object

    Methods
    -------
    start():
        Begins the video capture loop, displaying each frame until the video ends or ESC key is pressed.

    stop():
        Releases the video capture object and destroys all windows.
    """

    def __init__(self, index: int = 0):
        """
        Constructs all the necessary attributes for the VideoCapture object.

        Parameters
        ----------
        index : int, optional
            Index of the camera to use for video capture (default is 0, which usually corresponds to the default webcam).
        """
        self.capture = cv.VideoCapture(index)
        self.show_image = True

    def convert_to_gray(self, frame):
        """
        Applies Gaussian Blur and Otsu's thresholding to the input frame.

        Parameters
        ----------
        frame : np.ndarray
            The frame to threshold.

        Returns
        -------
        black_and_white_frame : np.ndarray
            The threshold frame.
        """
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
        """
        Start the video capture loop.
        The loop continues until there are no more frames or the ESC key is pressed.
        After the loop ends, the stop method is automatically called.
        """
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
        """
        Start the video capture loop.
        The loop continues until there are no more frames or the ESC key is pressed.
        After the loop ends, the stop method is automatically called.
        """
        self.capture.release()
        cv.destroyAllWindows()
