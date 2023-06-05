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

    def motion_detection(self, frame, prev_frame):
        diff = cv.absdiff(frame, prev_frame)
        cv.imshow('diff', diff)
        kernel = np.ones((5, 5))
        diff = cv.dilate(diff, kernel, 1)
        _, motion_mask = cv.threshold(src=diff,
                                      thresh=20,
                                      maxval=255,
                                      type=cv.THRESH_BINARY)

        contours, _ = cv.findContours(image=motion_mask.copy(),
                                      mode=cv.RETR_EXTERNAL,
                                      method=cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(image=frame,
                        contours=contours,
                        contourIdx=-1,
                        color=(0, 255, 0),
                        thickness=2,
                        lineType=cv.LINE_AA)
        return frame

    def threshold(self, frame):
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
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray_frame = cv.GaussianBlur(gray_frame, (5, 5), 0)
        _, gray_frame = cv.threshold(gray_frame, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

        return gray_frame

    def start(self):
        """
        Start the video capture loop.
        The loop continues until there are no more frames or the ESC key is pressed.
        After the loop ends, the stop method is automatically called.
        """
        prev_frame = None

        while True:

            ret, frame = self.capture.read()
            if frame is None:
                break

            gray_frame = self.threshold(frame)

            if prev_frame is not None:
                motion_frame = self.motion_detection(frame=gray_frame,
                                                     prev_frame=prev_frame)
                prev_frame = gray_frame
                cv.imshow('motion', motion_frame)

            keyboard = cv.waitKey(30)
            if keyboard == 27:
                break

            if prev_frame is None:
                prev_frame = gray_frame
                continue

        self.stop()

    def stop(self):
        """
        Start the video capture loop.
        The loop continues until there are no more frames or the ESC key is pressed.
        After the loop ends, the stop method is automatically called.
        """
        self.capture.release()
        cv.destroyAllWindows()