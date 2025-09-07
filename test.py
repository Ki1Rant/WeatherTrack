import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QCursor


class SimpleResizableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setGeometry(200, 200, 400, 300)
        self.setMinimumSize(200, 150)

        # Центральный виджет с отступами для границ
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(5, 5, 5, 5)

        # Заголовок
        header = QLabel("Перетаскивайте меня")
        header.setStyleSheet("""
            background-color: #3498db;
            color: white;
            padding: 10px;
            border-radius: 3px;
        """)
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        # Содержимое
        content = QLabel("Простое изменяемое окно")
        content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        content.setStyleSheet("background-color: #f0f0f0; padding: 30px;")
        layout.addWidget(content)

        self.drag_position = QPoint()
        self.border_width = 5

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.pos()
            rect = self.rect()

            # Проверяем, не на границе ли клик
            if (pos.x() > self.border_width and pos.x() < rect.width() - self.border_width and
                    pos.y() > self.border_width and pos.y() < rect.height() - self.border_width):
                self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        pos = event.pos()
        rect = self.rect()

        # Изменяем курсор при наведении на границы
        if (pos.x() <= self.border_width or pos.x() >= rect.width() - self.border_width or
                pos.y() <= self.border_width or pos.y() >= rect.height() - self.border_width):
            self.setCursor(Qt.CursorShape.SizeAllCursor)
        else:
            self.unsetCursor()

        if event.buttons() == Qt.MouseButton.LeftButton and not self.drag_position.isNull():
            self.move(event.globalPosition().toPoint() - self.drag_position)

    def mouseReleaseEvent(self, event):
        self.drag_position = QPoint()
        self.unsetCursor()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleResizableWindow()
    window.show()
    sys.exit(app.exec())