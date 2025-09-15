import sys

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QApplication, QMainWindow
from PyQt6.QtCore import Qt, QSize, QPoint

class WhiteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle("Погода")

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        central_widget = QWidget()
        central_widget.setStyleSheet("""
            QWidget {
                background-color: #95c2db;
                border-radius: 25px;
                border: 2px solid #737feb;
            }
        """)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(3, 3, 3, 3)
        top_layout = QHBoxLayout()

        self.header = QWidget()
        #self.header.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.header.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # self.header.setStyleSheet("""
        #     QWidget {
        #         background-color: grey;
        #         border-radius: 25px;
        #         border: 2px solid #737feb;
        #     }
        # """)
        self.header.setFixedHeight(30)
        top_layout.addWidget(self.header)
        # top_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        button = QPushButton("X")
        button.setFixedSize(QSize(20, 20))
        button.setStyleSheet("""
            QPushButton{
                color: 1c1c1c;
                border: none;
                border-radius: 8px;
                font-size: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #9e9d9d;
            }
            QPushButton:Pressed {
                background-color: #737070;
            }
        """)
        button.clicked.connect(self.close)
        top_layout.addWidget(button)

        main_layout.addLayout(top_layout)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.drag_position = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # Проверяем, был ли клик в области заголовка
            header_rect = self.header.geometry()
            header_rect.moveTo(self.header.mapToGlobal(QPoint(0, 0)) - self.mapToGlobal(QPoint(0, 0)))

            if header_rect.contains(event.pos()):
                self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
                event.accept()
            else:
                event.ignore()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and not self.drag_position.isNull():
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_position = QPoint()
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = WhiteWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    i = 0
    main()