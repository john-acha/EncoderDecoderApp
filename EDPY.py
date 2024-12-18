# The application allows users to encode and decode text using Base64 encoding.
__autor__ = 'John Acha'

import sys
import base64
import binascii
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        input_label = QLabel('Input Text:')
        self.input_text = QTextEdit()
        output_label = QLabel('Output Text:')
        self.output_text = QTextEdit()
        encode_button = QPushButton('Encode')
        decode_button = QPushButton('Decode')

        layout = QVBoxLayout()

        layout.addWidget(input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(encode_button)

        layout.addWidget(output_label)
        layout.addWidget(self.output_text)
        layout.addWidget(decode_button)

        encode_button.clicked.connect(self.encode_text)
        decode_button.clicked.connect(self.decode_text)
        self.input_text.setFocus()
        self.setLayout(layout)

        self.setWindowTitle('Encoder & Decoder')
        self.resize(400, 300)

    def encode_text(self):
        input_data = self.input_text.toPlainText()
        encoded_data = base64.b64encode(input_data.encode()).decode()
        self.output_text.setText(encoded_data)

    def decode_text(self):
        input_data = self.input_text.toPlainText()
        try:
            decoded_data = base64.b64decode(input_data.encode()).decode()
            self.output_text.setText(decoded_data)
        except (binascii.Error, UnicodeDecodeError):
            self.output_text.setText('<font color=red>Error: The text entered is not valid for decoding.</font>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
