from qt_core import *

class ComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('''
            QComboBox {
                background-color: #FFFFFF;
                border: 1px solid #CCCCCC;
                border-radius: 3px;
                padding: 4px 8px;
                color: #000000;
                font-size: 12px;
                font-weight: normal;
                selection-background-color: #DDDDDD;
            }
            QComboBox:hover {
                border: 1px solid #999999; 
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                
                border: none;
                background-color: transparent;
            }
            QComboBox::down-arrow {
                image: url(resources/icons/widget_icons/down_arrow.png);
                width: 16px;
                height: 16px;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #C8E6C9;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #C8E6C9;
                color: black;
            }
            QComboBox QAbstractItemView {
                outline: none;
                border: none;
            }
        ''')
        self.setCursor(Qt.PointingHandCursor)
