import sys
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QColor, QPainter, QPen, QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QColorDialog

# From copilot, the code is NOT working
class DrawingProgram(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Drawing Program")

        # Set the window size
        self.setGeometry(100, 100, 800, 600)

        # Set the default pen color and width
        self.pen_color = QColor(0, 0, 0)
        self.pen_width = 2

        # Set the drawing mode to line
        self.drawing_mode = "line"

        # Create a list to hold the points of the current drawing
        self.points = []

        # Create a QAction for the color picker
        color_picker_action = QAction("Pick Color", self)
        color_picker_action.triggered.connect(self.pick_color)

        # Create a QAction for the line drawing mode
        line_mode_action = QAction("Line", self)
        line_mode_action.triggered.connect(lambda: self.set_drawing_mode("line"))

        # Create a QAction for the circle drawing mode
        circle_mode_action = QAction("Circle", self)
        circle_mode_action.triggered.connect(lambda: self.set_drawing_mode("circle"))

        # Create a menu bar
        menu_bar = self.menuBar()

        # Create a File menu
        file_menu = menu_bar.addMenu("File")

        # Create an Exit action
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Create a Draw menu
        draw_menu = menu_bar.addMenu("Draw")

        # Add the color picker and drawing mode actions to the Draw menu
        draw_menu.addAction(color_picker_action)
        draw_menu.addAction(line_mode_action)
        draw_menu.addAction(circle_mode_action)

    def paintEvent(self, event):
        # Create a QPainter object
        painter = QPainter(self)

        # Set the pen color and width
        painter.setPen(QPen(self.pen_color, self.pen_width))

        # Draw the current drawing
        if self.drawing_mode == "line":
            painter.drawPolyline(self.points)
        elif self.drawing_mode == "circle":
            if len(self.points) == 2:
                center = QPoint((self.points[0].x() + self.points[1].x()) / 2, (self.points[0].y() + self.points[1].y()) / 2)
                radius = ((self.points[1].x() - self.points[0].x()) ** 2 + (self.points[1].y() - self.points[0].y()) ** 2) ** 0.5 / 2
                painter.drawEllipse(center, radius, radius)

    def mousePressEvent(self, event):
        # Add the current mouse position to the points list
        self.points.append(event.pos())

        # Redraw the window
        self.update()

    def mouseReleaseEvent(self, event):
        # Clear the points list
        self.points.clear()

    def pick_color(self):
        # Open a QColorDialog and get the selected color
        color = QColorDialog.getColor()

        # Set the pen color to the selected color
        if color.isValid():
            self.pen_color = color

    def set_drawing_mode(self, mode):
        # Set the drawing mode to the specified mode
        self.drawing_mode = mode


if __name__ == "__main__":
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create a DrawingProgram instance
    drawing_program = DrawingProgram()

    # Show the window
    drawing_program.show()

    # Run the event loop
    sys.exit(app.exec())