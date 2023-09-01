from moviepy.editor import VideoFileClip
import pygame

# Load the video file using moviepy's VideoFileClip function
clip = VideoFileClip('test_serve.mov')

# Get the original video resolution
width, height = clip.size
print('width height from video is ' + str(width) + ' ' + str(height))
# Swap width and height because the video is rotated 90 degrees
width, height = height, width

# Initialize Pygame
pygame.init()

# Create a Pygame window with the original video resolution
screen = pygame.display.set_mode((width, height))

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Set the initial position of the progress bar
progress = 0

# Create a loop to read each frame of the video and display it
while True:
    # Read the next frame of the video
    frame = clip.get_frame(progress)

    # Rotate the frame by 90 degrees
    frame = pygame.surfarray.make_surface(frame.swapaxes(1, 0))

    # Display the current frame of the video
    screen.blit(frame, (0, 0))

    # Draw the progress bar
    pygame.draw.rect(screen, (255, 255, 255), (0, height - 10, int(progress / clip.duration * width), 10))

    # Update the Pygame window
    pygame.display.flip()

    # Check for Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the loop if the window is closed
            pygame.quit()
            quit()

    # Increment the progress bar position
    progress += 1 / clip.fps

    # Check if the end of the video is reached
    if progress > clip.duration:
        break

    # Control the frame rate
    clock.tick(clip.fps)

# Release the video clip and quit Pygame
clip.reader.close()
pygame.quit()