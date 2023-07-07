from qt_core import *

class PushButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet('''
            QPushButton {
                background-color: #388E3C;
                border: 1px solid #228B22;
                border-radius: 5px;
                color: #FFFFFF;
                font-size: 14px;
                padding: 4px 16px;
            }
            
            QPushButton:hover {
                background-color: #3CB371;
            }
            
            QPushButton:pressed {
                background-color: #32CD32;
            }
            
            QPushButton:disabled {
                background-color: #CCCCCC;
                border: 1px solid #999999;
                color: #999999;
            }
        ''')
        self.setCursor(Qt.PointingHandCursor)
