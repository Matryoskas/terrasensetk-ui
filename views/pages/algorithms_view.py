from qt_core import *

class AlgorithmsView(QWidget):
    def __init__(self):
        super().__init__()

        # Creating the QGroupBox for the Algorithms Page
        group_box = QGroupBox("Algorithms Page")

        # Creating the label for the Algorithms Page
        label = QLabel("Content of the Algorithms Page")

        # Creating the vertical layout for the Algorithms Page
        layout = QVBoxLayout()
        layout.addWidget(label)
        group_box.setLayout(layout)

        # Creating the vertical layout for the AlgorithmView
        main_layout = QVBoxLayout()
        main_layout.addWidget(group_box)
        self.setLayout(main_layout)

