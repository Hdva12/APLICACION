from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush
import os
import confing

ANCHO, ALTO = 700, 500
COR_X, COR_Y = 200, 200
TITULO = 'quiz de conocimiento'
INPUT_TEXT = 'Ingrese Algo...'
BTN_TEXT = 'Enviar'

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.set_window()
        self.config_window()
        self.event_handler()
        self.show()

    def set_window(self): 
    
        self.input = QLineEdit(INPUT_TEXT)

        self.input.hide()
        self.btn = QPushButton(BTN_TEXT)
        self.label = QLabel()

        layout = QHBoxLayout()
        layout.addWidget(self.input, alignment=Qt.AlignLeft)
        layout.addWidget(self.btn, alignment=Qt.AlignLeft)
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def config_window(self):
        self.setGeometry(COR_X, COR_Y, ANCHO, ALTO)
        self.setWindowTitle(TITULO)
        self.set_background()

    def set_background(self):
        img_name = getattr(confing, 'fondo', None)
        if not img_name:
            return
        base = os.path.dirname(__file__)
        img_path = os.path.join(base, img_name)
        img_path = img_path.replace('\\', '/')
        if not os.path.exists(img_path):
            return
        pix = QPixmap(img_path)
        if pix.isNull():
            return
        scaled = pix.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

    def resizeEvent(self, event):
        # Reescalar fondo cuando la ventana cambia de tamaño
        self.set_background()
        super().resizeEvent(event)

    def event_handler(self):
        # FUNCION QUE SE ENCARGA DE MANEJAR LA LOGICA
        self.btn.clicked.connect(self.show_text)

    # AQUI SE DEFINEN TODAS LAS FUNCIONALIDADES DE LA APP
    def show_text(self):
        text = self.input.text()
        self.label.setText(text)

def run():
    # CREA Y EJECUTA LA APP
    app = QApplication([])
    main_window = MainWindow()
    app.exec_()

if __name__ == "__main__":
    run()