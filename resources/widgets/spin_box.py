from qt_core import *

class SpinBox(QSpinBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet('''
            QSpinBox {
                background-color: #FFFFFF;
                border: 1px solid #CCCCCC;
                border-radius: 3px;
                padding: 4px 8px;
                color: #000000;
                font-size: 12px;
                font-weight: normal;
            }
            
            QSpinBox:disabled {
                background-color: #F0F0F0;
                color: #999999;
            }
        ''')
        self.setCursor(Qt.PointingHandCursor)
