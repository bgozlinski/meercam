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
        """opencv turn rgb to black and white
        Start the video capture loop.
        The loop continues until there are no more frames or the ESC key is pressed.
        After the loop ends, the stop method is automatically called.
        """
        while True:
            ret, frame = self.capture.read()
            if frame is None:
                break

            # Convert the frame to grayscale
            gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            # Apply Gaussian filtering for noise reduction
            denoised_frame = cv.GaussianBlur(gray_frame, (5, 5), 0)

            _, black_and_white_frame = cv.threshold(denoised_frame, 125, 255, cv.THRESH_BINARY)
            cv.imshow('Frame', black_and_white_frame)

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
