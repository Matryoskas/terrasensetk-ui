from qt_core import *

class DoubleSpinBox(QDoubleSpinBox):
    def __init__(self):
        super().__init__()

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