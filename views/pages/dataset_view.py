from qt_core import *

class DatasetView(QWidget):
    def __init__(self):
        super().__init__()

        # Creating the label for the Dataset Page
        label = QLabel("Dataset Page")
        
        # Creating the vertical layout for the Dataset Page
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)
