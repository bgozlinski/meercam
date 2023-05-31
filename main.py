import cv2 as cv


class VideoCapture:
    def __init__(self, index=0):
        # Initialize VideoCapture object with the provided index.
        self.capture = cv.VideoCapture(index)

    def start(self):
        # Start the video capture loop.
        while True:
            # Read the next frame from the video capture object.
            ret, frame = self.capture.read()
            # If the frame is None, it means that there's an issue with the video capture
            # (perhaps the video is over, or there's an issue with the webcam), so break the loop.
            if frame is None:
                break

            # Display the current frame in a window named 'Frame'.
            cv.imshow('Frame', frame)

            # Wait for a keyboard event for a delay of 30 milliseconds.
            # If the ESC key is pressed (ASCII 27), break the loop.
            keyboard = cv.waitKey(30)
            if keyboard == 27:
                break

        # After the loop is broken, stop the video capture.
        self.stop

    def stop(self):
        # Release the video capture object and destroy all windows to free up resources.
        self.capture.release()
        cv.destroyAllWindows()


if __name__ == '__main__':
    video_capture = VideoCapture()
    video_capture.start()
