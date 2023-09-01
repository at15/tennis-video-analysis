import cv2
import tkinter as tk

# Create a Tkinter window with a scroll bar widget
root = tk.Tk()
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Load the video file from the iPhone using OpenCV's VideoCapture function
cap = cv2.VideoCapture('iphone_video.mp4')

# Set the frame rate of the video to a slower value to achieve slow motion
fps = cap.get(cv2.CAP_PROP_FPS)
slow_fps = fps / 2
cap.set(cv2.CAP_PROP_FPS, slow_fps)

# Create a loop to read each frame of the video and display it in the Tkinter window
def update_frame(val):
    cap.set(cv2.CAP_PROP_POS_FRAMES, val)
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Video Player', frame)
        cv2.waitKey(1)

# Use the scroll bar widget to control the position of the video playback
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
scrollbar.config(command=update_frame, from_=0, to=frame_count)

# Add buttons to control the playback, such as play, pause, and stop
play_button = tk.Button(root, text='Play', command=lambda: cv2.waitKey(0))
play_button.pack(side=tk.LEFT)
pause_button = tk.Button(root, text='Pause', command=lambda: cv2.waitKey(1))
pause_button.pack(side=tk.LEFT)
stop_button = tk.Button(root, text='Stop', command=lambda: cv2.destroyAllWindows())
stop_button.pack(side=tk.LEFT)

# Start the Tkinter main loop
cv2.namedWindow('Video Player')
cv2.waitKey(1)
root.mainloop()

# Release the video capture and destroy the OpenCV window
cap.release()
cv2.destroyAllWindows()