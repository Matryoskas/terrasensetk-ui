from qt_core import *

class DateEdit(QDateEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet('''
            QDateEdit {
                background-color: #FFFFFF;
                border: 1px solid #CCCCCC;
                border-radius: 3px;
                padding: 4px 8px;
                color: #000000;
                font-size: 12px;
                font-weight: normal;
            }
            
            QDateEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border: none;
                background-color: transparent;
            }
            
            QDateEdit::down-arrow {
                image: url(resources/icons/widget_icons/down_arrow.png);
                width: 16px;
                height: 16px;
            }
            
            QDateEdit::up-arrow {
                image: url(resources/icons/widget_icons/down_arrow.png);
                width: 16px;
                height: 16px;
            }
            
            QDateEdit::down-button {
                border: none;
                background-color: transparent;
            }
            
            QDateEdit::up-button {
                border: none;
                background-color: transparent;
            }
            QDateEdit:disabled {
                background-color: #F0F0F0;
                color: #999999;
            }
            
        ''')
        self.setCursor(Qt.PointingHandCursor)

