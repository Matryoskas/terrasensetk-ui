from qt_core import *

class CheckBox(QCheckBox):
    def __init__(self, text):
        super().__init__(text)
        
        self.setStyleSheet('''
            QCheckBox {
                spacing: 5px;
                font-size: 12px;
                font-weight: normal;
                color: #000000;
            }
            
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
            }
            
            QCheckBox::indicator:unchecked {
                border: 1px solid #CCCCCC;
                background-color: #FFFFFF;
                border-radius: 2px;
            }
            
            QCheckBox::indicator:unchecked:hover {
                border: 1px solid #999999;
            }
            
            QCheckBox::indicator:checked {
                border: 1px solid #62B964;
                background-color: #8CCF8F;
                image: url(resources/icons/widget_icons/check_box_mark.png);
                border-radius: 2px; 
            }
            
            QCheckBox::indicator:checked:hover {
                border: 1px solid #389238;
            }
            
            QCheckBox::indicator:checked:disabled {
                border: 1px solid #CCCCCC;
                background-color: #DDDDDD;
            }
            
            QCheckBox::indicator:indeterminate {
                border: 1px solid #CCCCCC;
                background-color: #FFFFFF;
                border-radius: 2px;
            }
            
            QCheckBox::indicator:indeterminate:hover {
                border: 1px solid #999999;
            }
            
            QCheckBox::indicator:indeterminate:checked {
                border: 1px solid #62B964;
                background-color: #62B964;
                border-radius: 2px;
            }
            
            QCheckBox::indicator:indeterminate:checked:hover {
                border: 1px solid #389238;
            }
        ''')
        self.setCursor(Qt.PointingHandCursor)



