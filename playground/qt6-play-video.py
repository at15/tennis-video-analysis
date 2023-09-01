import sys
import cv2
from PyQt6.QtCore import Qt, QUrl, QTimer
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QSizePolicy, QVBoxLayout, QWidget, QFileDialog, QMenuBar, QStatusBar, QToolBar, QSlider, QHBoxLayout, QPushButton
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtGui import QAction, QIcon

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QMediaPlayer object
        self.media_player = QMediaPlayer()

        # Create a QVideoWidget object to display the video
        self.video_widget = QVideoWidget()

        # Set the QVideoWidget as the central widget of the main window
        self.setCentralWidget(self.video_widget)

        # Set the media player to use the QVideoWidget as its output
        self.media_player.setVideoOutput(self.video_widget)

        # Create a QMenuBar
        menu_bar = QMenuBar(self)

        # Create a File menu
        file_menu = menu_bar.addMenu("File")

        # Create an Open action
        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # Set the menu bar of the main window
        self.setMenuBar(menu_bar)

        # Create a QToolBar
        tool_bar = QToolBar(self)

        # Create a Play button
        play_button = QAction("Play", self)
        play_button.setShortcut("Space")
        play_button.triggered.connect(self.play)
        tool_bar.addAction(play_button)

        # Create a Pause button
        pause_button = QAction("Pause", self)
        pause_button.setShortcut("Ctrl+Space")
        pause_button.triggered.connect(self.pause)
        tool_bar.addAction(pause_button)

        # Create a Stop button
        stop_button = QAction("Stop", self)
        stop_button.setShortcut("Ctrl+Shift+Space")
        stop_button.triggered.connect(self.stop)
        tool_bar.addAction(stop_button)

        # Create a progress bar
        self.progress_bar = QSlider(Qt.Orientation.Horizontal)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.sliderMoved.connect(self.set_position)
        tool_bar.addWidget(self.progress_bar)

        # Add the tool bar to the main window
        self.addToolBar(tool_bar)

        # Create a timer to update the progress bar
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress_bar)

    def open_file(self):
        # Open a file dialog to select a video file
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video", "", "Video Files (*.mp4 *.mov)")

        if file_name != "":
            # Set the media player to play the selected file
            self.media_player.setSource(QUrl.fromLocalFile(file_name))

            # Set the progress bar range to the duration of the video
            duration = self.media_player.duration()
            self.progress_bar.setRange(0, duration)

            # Start the timer to update the progress bar
            self.timer.start(1000)

            # Not sure why, but MP4 file can detect portrait correctly, but MOV file cannot.
            # # Get the size of the video
            # video_size = self.video_widget.size()

            # # If the video is taller than it is wide, adjust the size of the video widget
            # if video_size.height() > video_size.width():
            #     self.video_widget.setFixedSize(video_size.height(), video_size.width())
            # else:
            #     self.video_widget.setFixedSize(video_size.width(), video_size.height())


    def play(self):
        # Start playing the video
        self.media_player.play()

    def pause(self):
        # Pause the video
        self.media_player.pause()

    def stop(self):
        # Stop the video and reset the progress bar
        self.media_player.stop()
        self.progress_bar.setValue(0)

    def set_position(self, position):
        # Set the position of the video to the selected position on the progress bar
        self.media_player.setPosition(position)

    def update_progress_bar(self):
        # Update the progress bar to reflect the current position of the video
        position = self.media_player.position()
        self.progress_bar.setValue(position)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec())