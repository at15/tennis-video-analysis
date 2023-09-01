import cv2

# Load the video file using OpenCV's VideoCapture function
cap = cv2.VideoCapture('test_serve.mov')

# Create a window to display the video player and a trackbar widget for the progress bar
cv2.namedWindow('Video Player')
cv2.createTrackbar('Progress', 'Video Player', 0, int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), lambda x: None)

# Create a loop to read each frame of the video and display it
while True:
    # Read the current position of the trackbar widget
    pos = cv2.getTrackbarPos('Progress', 'Video Player')

    # Set the position of the video playback to the current position of the trackbar widget
    cap.set(cv2.CAP_PROP_POS_FRAMES, pos)

    # Read the next frame of the video
    ret, frame = cap.read()

    if ret:
        # Display the current frame of the video
        cv2.imshow('Video Player', frame)

        # Update the position of the trackbar widget
        cv2.setTrackbarPos('Progress', 'Video Player', pos + 1)

        # Calculate the current time and duration of the video
        current_time = int(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)
        total_time = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS))

        # Calculate the current percentage of the video
        current_percent = int(pos / cap.get(cv2.CAP_PROP_FRAME_COUNT) * 100)

        # Update the label of the trackbar widget with the current position of the video playback
        label = f'Frame: {pos} / {int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}  Time: {current_time} / {total_time} sec  Percent: {current_percent}%'
        cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        # Check for the 'q' key press and exit the loop if it is pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and destroy the OpenCV window
cap.release()
cv2.destroyAllWindows()