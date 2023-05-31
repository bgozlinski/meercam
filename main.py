import cv2 as cv


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
    def __init__(self, index=0):
        """
        Constructs all the necessary attributes for the VideoCapture object.

        Parameters
        ----------
        index : int, optional
            Index of the camera to use for video capture (default is 0, which usually corresponds to the default webcam).
        """
        self.capture = cv.VideoCapture(index)

    def start(self):
        """
        Start the video capture loop.
        The loop continues until there are no more frames or the ESC key is pressed.
        After the loop ends, the stop method is automatically called.
        """
        while True:
            ret, frame = self.capture.read()
            if frame is None:
                break

            cv.imshow('Frame', frame)

            keyboard = cv.waitKey(30)
            if keyboard == 27:
                break

        self.stop

    def stop(self):
        """
        Start the video capture loop.
        The loop continues until there are no more frames or the ESC key is pressed.
        After the loop ends, the stop method is automatically called.
        """
        self.capture.release()
        cv.destroyAllWindows()


if __name__ == '__main__':
    # Create an instance of VideoCapture and start it.
    video_capture = VideoCapture()
    video_capture.start()
