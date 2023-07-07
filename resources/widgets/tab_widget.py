from qt_core import *

class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(
            """
            QTabWidget::pane {
                border: none;
            }
            QTabBar::tab {
                background-color: #E8F5E9;
                border: 1px solid #4CAF50;
                padding: 6px;
            }
            QTabBar::tab:selected {
                background-color: #388E3C;
                color: white;
            }
            """
        )