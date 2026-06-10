from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit, QGraphicsBlurEffect, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QColor, QFont, QFontDatabase, QFontMetrics
import os
import confing
import random
import preguntas


class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.set_window()
        self.config_window()
        self.event_handler()
        self.show()

    def set_window(self): 
    
        self.input = QLineEdit(confing.INPUT_TEXT)
        self.input.hide()

        # Título en la parte superior
        self.title_label = QLabel("Cuestionario de dragon ball")
        self.title_label.setAlignment(Qt.AlignCenter)
        # Etiqueta de feedback (Correcto / Incorrecto)
        self.feedback_label = QLabel("")
        self.feedback_label.setAlignment(Qt.AlignCenter)
        try:
            self.feedback_label.setStyleSheet('font-size: 32px; color: transparent;')
        except Exception:
            pass
        self.feedback_label.hide()
        # Intentar cargar la fuente proporcionada en confing.py
        try:
            font_file = getattr(confing, 'fuente', None)
            if font_file:
                base = os.path.dirname(__file__)
                font_path = os.path.join(base, font_file).replace('\\', '/')
                if os.path.exists(font_path):
                    fid = QFontDatabase.addApplicationFont(font_path)
                    if fid != -1:
                        families = QFontDatabase.applicationFontFamilies(fid)
                        if families:
                            family = families[0]
                            size = getattr(confing, 'TITULO_FONT_SIZE', 48)
                            self.title_label.setFont(QFont(family, size))
        except Exception:
            pass
        # Color del título
        try:
            title_color = getattr(confing, 'TITULO_FONT_COLOR', '#000000')
            self.title_label.setStyleSheet(f'color: {title_color};')
        except Exception:
            pass
        # Aplicar sombra al título si está configurada
        try:
            t_shadow_color = getattr(confing, 'TITULO_SHADOW_COLOR', '#444444')
            t_shadow_blur = getattr(confing, 'TITULO_SHADOW_BLUR', 12)
            t_shadow_off_x = getattr(confing, 'TITULO_SHADOW_OFFSET_X', 0)
            t_shadow_off_y = getattr(confing, 'TITULO_SHADOW_OFFSET_Y', 3)
            drop_t = QGraphicsDropShadowEffect(self.title_label)
            drop_t.setBlurRadius(t_shadow_blur)
            try:
                drop_t.setColor(QColor(t_shadow_color))
            except Exception:
                drop_t.setColor(QColor('#444444'))
            drop_t.setOffset(t_shadow_off_x, t_shadow_off_y)
            self.title_label.setGraphicsEffect(drop_t)
        except Exception:
            pass

        # Botones Iniciar y Salir
        self.btn_iniciar = QPushButton(getattr(confing, 'BTN_INICIAR_TEXT', 'Iniciar'))
        self.btn_salir = QPushButton(getattr(confing, 'BTN_SALIR_TEXT', 'Salir'))
        self.label = QLabel()

        # Estilo desde confing (botones más grandes y con bordes redondeados)
        try:
            radius = getattr(confing, 'BTN_BORDER_RADIUS', 20)
            btn_style = (
                f"background-color: {confing.BTN_COLOR}; "
                f"color: {confing.BTN_TEXT_COLOR}; "
                f"font-size: 20px; padding: 16px 28px; "
                f"border-radius: {radius}px; border: none;"
            )
        except Exception:
            btn_style = ''
        self.btn_iniciar.setStyleSheet(btn_style)
        self.btn_salir.setStyleSheet(btn_style)
        # Aplicar sombra más oscura a ambos botones según confing
        try:
            shadow_color = getattr(confing, 'BTN_SHADOW_COLOR', '#444444')
            shadow_blur = getattr(confing, 'BTN_SHADOW_BLUR_RADIUS', 20)
            shadow_off_x = getattr(confing, 'BTN_SHADOW_OFFSET_X', 0)
            shadow_off_y = getattr(confing, 'BTN_SHADOW_OFFSET_Y', 6)
            for btn in (self.btn_iniciar, self.btn_salir):
                drop = QGraphicsDropShadowEffect(btn)
                drop.setBlurRadius(shadow_blur)
                try:
                    drop.setColor(QColor(shadow_color))
                except Exception:
                    drop.setColor(QColor('#444444'))
                drop.setOffset(shadow_off_x, shadow_off_y)
                btn.setGraphicsEffect(drop)
        except Exception:
            pass

        # Tamaño idéntico y mayor para ambos botones
        btn_w, btn_h = 360, 100
        self.btn_iniciar.setFixedSize(btn_w, btn_h)
        self.btn_salir.setFixedSize(btn_w, btn_h)

        # Layout vertical con título arriba y botones hacia abajo
        layout = QVBoxLayout()
        # Guardar referencia para poder añadir/mostrar elementos dinámicamente
        self.main_layout = layout
        layout.addWidget(self.title_label, alignment=Qt.AlignHCenter)
        layout.addWidget(self.feedback_label, alignment=Qt.AlignHCenter)
        layout.addStretch(1)
        layout.addWidget(self.input, alignment=Qt.AlignHCenter)
        # Añadir gran espacio para empujar los botones hacia abajo
        layout.addStretch(6)
        layout.addWidget(self.btn_iniciar, alignment=Qt.AlignHCenter)
        layout.addWidget(self.btn_salir, alignment=Qt.AlignHCenter)
        layout.addWidget(self.label, alignment=Qt.AlignHCenter)
        # Contenedor para los botones inferiores (oculto inicialmente)
        self.bottom_container = QWidget(self)
        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setSpacing(20)
        self.bottom_container.setLayout(self.bottom_layout)
        self.bottom_container.hide()
        layout.addWidget(self.bottom_container, alignment=Qt.AlignHCenter | Qt.AlignBottom)
        layout.addStretch(1)

        self.setLayout(layout)

    def config_window(self):
        self.setGeometry(confing.COR_X, confing.COR_Y, confing.ANCHO, confing.ALTO)
        self.setWindowTitle(confing.TITULO)
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

        # Mostrar el fondo en un QLabel para poder aplicar efectos (blur)
        scaled = pix.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        if not hasattr(self, 'bg_label'):
            self.bg_label = QLabel(self)
            self.bg_label.setScaledContents(True)
            self.bg_label.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.bg_label.setPixmap(scaled)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())

        # Aplicar difuminado según configuración
        blur_radius = getattr(confing, 'BG_BLUR_RADIUS', 0)
        if blur_radius and blur_radius > 0:
            blur = QGraphicsBlurEffect(self.bg_label)
            blur.setBlurRadius(blur_radius)
            self.bg_label.setGraphicsEffect(blur)
        else:
            self.bg_label.setGraphicsEffect(None)

        # Asegurar que quede detrás
        try:
            self.bg_label.lower()
        except Exception:
            pass
        self.setAutoFillBackground(False)

    def resizeEvent(self, event):
        # Reescalar fondo cuando la ventana cambia de tamaño
        self.set_background()
        super().resizeEvent(event)

    def event_handler(self):
        # FUNCION QUE SE ENCARGA DE MANEJAR LA LOGICA
        # Iniciar muestra el texto del input y luego oculta widgets dejando solo el fondo
        self.btn_iniciar.clicked.connect(self.show_text)
        # Salir cierra la aplicación
        self.btn_salir.clicked.connect(lambda: QApplication.instance().quit())

    # AQUI SE DEFINEN TODAS LAS FUNCIONALIDADES DE LA APP
    def show_text(self):
        text = self.input.text()
        self.label.setText(text)
        # Ocultar widgets para dejar solo el fondo visible
        for w in (self.input, self.btn_iniciar, self.btn_salir, self.label):
            try:
                w.hide()
            except Exception:
                pass
        # Inicializar índice de pregunta y mostrar primera pregunta
        self.current_question_index = 0
        try:
            if preguntas.PREGUNTAS:
                q = preguntas.PREGUNTAS[self.current_question_index]
                q_text = q.get('pregunta') if isinstance(q, dict) else None
                if q_text:
                    self.title_label.setText(q_text)
        except Exception:
            pass
        try:
            self.title_label.show()
        except Exception:
            pass
        # Crear y mostrar los botones inferiores con opciones de la pregunta
        self.create_bottom_buttons()
        self.bottom_container.show()
        # Determinar una posición aleatoria única para los botones
        self.randomize_bottom_positions()

    def create_bottom_buttons(self):
        # Si ya existen, asegurarse de que estén visibles
        # Obtener índice de la pregunta actual
        idx = getattr(self, 'current_question_index', 0)
        # Obtener opciones desde el módulo `preguntas`
        opts = None
        try:
            if preguntas.PREGUNTAS and 0 <= idx < len(preguntas.PREGUNTAS):
                q = preguntas.PREGUNTAS[idx]
                opts = q.get('opciones') if isinstance(q, dict) else None
        except Exception:
            opts = None

        # Si no hay opciones, usar valores por defecto
        if not opts:
            items = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]
        else:
            items = list(opts.items())

        # Tamaño y estilo heredado de confing (botones estilo Kahoot: más grandes)
        btn_w, btn_h = 480, 140
        try:
            radius = getattr(confing, 'BTN_BORDER_RADIUS', 20)
            color = getattr(confing, 'BTN_COLOR', '#87CEEB')
            text_color = getattr(confing, 'BTN_TEXT_COLOR', '#ffffff')
            base_style = f"background-color: {color}; color: {text_color}; border-radius: {radius}px; font-size: 28px;"
        except Exception:
            base_style = ''

        # Si ya existen botones, actualizar su texto y option_key
        if hasattr(self, 'bottom_buttons') and self.bottom_buttons:
            # si la cantidad difiere, reconstruir
            if len(self.bottom_buttons) != len(items):
                # eliminar widgets antiguos
                while self.bottom_layout.count():
                    item = self.bottom_layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.setParent(None)
                self.bottom_buttons = []
            else:
                for b, (key, text) in zip(self.bottom_buttons, items):
                    b.option_key = key
                    try:
                        b.setText(self.wrap_text_for_button(text, btn_w, b.font()))
                    except Exception:
                        b.setText(text)
                    b.setStyleSheet(base_style)
                    try:
                        b.setEnabled(True)
                    except Exception:
                        pass
                    b.setFixedSize(btn_w, btn_h)
                    b.show()
                return

        # Crear botones nuevos
        self.bottom_buttons = []
        for key, text in items:
            b = QPushButton(text)
            # Ajustar texto para que haga wraps dentro del ancho del botón
            try:
                b.setText(self.wrap_text_for_button(text, btn_w, b.font()))
            except Exception:
                b.setText(text)
            b.option_key = key
            b.setFixedSize(btn_w, btn_h)
            b.setStyleSheet(base_style)
            # conectar al handler
            b.clicked.connect(lambda _, btn=b: self.on_bottom_clicked(btn))
            self.bottom_buttons.append(b)
            self.bottom_layout.addWidget(b, alignment=Qt.AlignHCenter)

    def randomize_bottom_positions(self):
        # Mezcla aleatoria de los botones reordenándolos en el layout
        if not hasattr(self, 'bottom_buttons') or not self.bottom_buttons:
            return
        order = self.bottom_buttons[:]
        random.shuffle(order)
        # Vaciar layout
        while self.bottom_layout.count():
            item = self.bottom_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
        # Volver a añadir en nuevo orden
        for w in order:
            self.bottom_layout.addWidget(w, alignment=Qt.AlignHCenter)
        # actualizar referencia a la lista en el nuevo orden
        self.bottom_buttons = order

    def wrap_text_for_button(self, text: str, max_width: int, font: QFont) -> str:
        """Insert line breaks into `text` so it fits within `max_width` using `font` metrics.

        Returns a string with '\n' where appropriate.
        """
        try:
            fm = QFontMetrics(font)
        except Exception:
            return text

        words = text.split(' ')
        if not words:
            return text

        lines = []
        cur = ''
        padding = 24  # internal padding allowance
        effective_width = max_width - padding
        for w in words:
            if cur:
                test = cur + ' ' + w
            else:
                test = w
            if fm.horizontalAdvance(test) <= effective_width:
                cur = test
            else:
                # if single word too long, break the word
                if fm.horizontalAdvance(w) > effective_width:
                    part = ''
                    for ch in w:
                        if fm.horizontalAdvance(part + ch) <= effective_width:
                            part += ch
                        else:
                            if cur:
                                lines.append(cur)
                                cur = ''
                            lines.append(part)
                            part = ch
                    if part:
                        if cur:
                            lines.append(cur)
                            cur = part
                        else:
                            cur = part
                else:
                    if cur:
                        lines.append(cur)
                    cur = w
        if cur:
            lines.append(cur)

        return '\n'.join(lines)

    def on_bottom_clicked(self, button):
        # Manejar respuesta: mostrar correcta en verde y la seleccionada
        # en rojo si es incorrecta; luego avanzar tras breve pausa.
        try:
            chosen = getattr(button, 'option_key', None)
        except Exception:
            chosen = None

        idx = getattr(self, 'current_question_index', 0)
        correcta = None
        try:
            if preguntas.PREGUNTAS and 0 <= idx < len(preguntas.PREGUNTAS):
                q = preguntas.PREGUNTAS[idx]
                correcta = q.get('correcta') if isinstance(q, dict) else None
        except Exception:
            correcta = None

        # Estilos de feedback
        ok_style = 'background-color: #28a745; color: #ffffff; border-radius: %dpx; font-size: 28px;' % getattr(confing, 'BTN_BORDER_RADIUS', 20)
        bad_style = 'background-color: #dc3545; color: #ffffff; border-radius: %dpx; font-size: 28px;' % getattr(confing, 'BTN_BORDER_RADIUS', 20)

        # Desactivar todos los botones mientras mostramos feedback
        try:
            for b in getattr(self, 'bottom_buttons', []):
                b.setEnabled(False)
        except Exception:
            pass

        # Marcar la correcta y la seleccionada
        try:
            for b in getattr(self, 'bottom_buttons', []):
                try:
                    if getattr(b, 'option_key', None) == correcta:
                        b.setStyleSheet(ok_style)
                    elif getattr(b, 'option_key', None) == chosen:
                        # Si es incorrecta, marcar en rojo
                        if correcta is not None and chosen != correcta:
                            b.setStyleSheet(bad_style)
                except Exception:
                    pass
        except Exception:
            pass

        # Mostrar texto de feedback encima de los botones
        try:
            if correcta is not None and chosen is not None:
                if chosen == correcta:
                    self.feedback_label.setText('Correcto')
                    self.feedback_label.setStyleSheet('color: #28a745; font-size: 32px;')
                else:
                    self.feedback_label.setText('Incorrecto')
                    self.feedback_label.setStyleSheet('color: #dc3545; font-size: 32px;')
                self.feedback_label.show()
        except Exception:
            pass

        # Tras 1.2s avanzamos a la siguiente pregunta
        def after_feedback():
            try:
                try:
                    self.feedback_label.hide()
                except Exception:
                    pass
                next_index = idx + 1
                if next_index < len(preguntas.PREGUNTAS):
                    self.current_question_index = next_index
                    try:
                        q = preguntas.PREGUNTAS[next_index]
                        q_text = q.get('pregunta') if isinstance(q, dict) else None
                        if q_text:
                            self.title_label.setText(q_text)
                    except Exception:
                        pass
                    # Restaurar estilos y actualizar botones
                    self.create_bottom_buttons()
                    self.randomize_bottom_positions()
                else:
                    try:
                        self.bottom_container.hide()
                    except Exception:
                        pass
                    try:
                        self.title_label.setText('Cuestionario terminado')
                    except Exception:
                        pass
            except Exception:
                pass

        QTimer.singleShot(1200, after_feedback)

def run():
    # CREA Y EJECUTA LA APP
    app = QApplication([])
    main_window = MainWindow()
    app.exec_()

if __name__ == "__main__":
    run()