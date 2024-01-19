import cv2
import numpy as np
import time
import pyautogui

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
output_file = 'screen_record.mp4'
fps = 30.0
frame_size = (1920, 1080)  # Change this to match your screen resolution
out = cv2.VideoWriter(output_file, fourcc, fps, frame_size)

# Initialize the VideoCapture object to capture the screen
cap = cv2.VideoCapture(0)

try:
    if not cap.isOpened():
        print("Unable to read camera feed")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Convert the captured frame to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write the frame to the output file
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('Screen Recording', frame)

        # Stop recording when the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Release the VideoCapture and VideoWriter objects and close all windows
    cap.release()
    out.release()
    cv2.destroyAllWindows()