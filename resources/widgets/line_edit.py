from qt_core import *

class LineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('''
            QLineEdit {
                background-color: #F0F0F0;
                border: 1px solid #CCCCCC;
                border-radius: 2px;
                padding: 4px 8px;
            }
            
            QLineEdit:disabled {
                background-color: #CCCCCC;
                border-color: #999999;
                color: #999999;
            }
        ''')
    
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        
        if self.isEnabled():
            line_color = QColor("#388E3C") 
        else:
            line_color = QColor("#999999")  
        
        painter.setBrush(line_color)
        painter.drawRect(0, self.height() - 2, self.width(), 2)
