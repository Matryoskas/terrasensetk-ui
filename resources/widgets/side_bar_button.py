from qt_core import *

class SideBarButton(QToolButton):
    def __init__(self, text, icon_path, icon_size=(32, 32)):
        super().__init__()
        self.setFixedSize(95, 70)
        
        icon = QIcon(icon_path)
        self.setIcon(icon)
        self.setIconSize(QSize(*icon_size))
        
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setText(text)
        
        self.setCursor(Qt.PointingHandCursor)
        
        self.setStyleSheet("""
            QToolButton {
                border: none;
                padding: 7px 12px;
                background-color: #4CAF50;
                font-family: Lato, sans-serif;
                color: #FFFFFF;
                font-weight: bold;
            }
        
            QToolButton:hover {
                background-color: #388E3C;
            }
        
            QToolButton:pressed {
                background-color: #1B5E20;
            }
        """)
    

        
        