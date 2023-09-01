import sys
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QSizePolicy, QVBoxLayout, QWidget, QFileDialog, QMenuBar, QStatusBar, QToolBar, QSlider, QHBoxLayout
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
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

    def open_file(self):
        # Open a file dialog to select a video file
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video", "", "Video Files (*.mp4 *.avi *.mkv)")

        if file_name != "":
            # Create a QMediaContent object with the selected file
            media_content = QMediaContent(QUrl.fromLocalFile(file_name))

            # Set the media player to use the QMediaContent
            self.media_player.setMedia(media_content)

            # Set the window title to the name of the selected file
            self.setWindowTitle(f"Video Player - {file_name}")

            # Play the video
            self.play()

    def play(self):
        # Play the video
        self.media_player.play()

    def pause(self):
        # Pause the video
        self.media_player.pause()

    def stop(self):
        # Stop the video
        self.media_player.stop()

    def set_position(self, position):
        # Set the playback position of the video
        self.media_player.setPosition(position)

        # Update the position slider
        self.position_slider.setValue(position)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())