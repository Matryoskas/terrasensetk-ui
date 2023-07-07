from qt_core import *

class PerformanceEvaluationView(QWidget):
    def __init__(self):
        super().__init__()

        # Creating the QGroupBox for the  Performance Evaluation Page
        group_box = QGroupBox("Performance Evaluation Page")

        # Creating the label for the  Performance Evaluation Page
        label = QLabel("Content of the Performance Evaluation Page")

        # Creating the vertical layout for the  Performance Evaluation Page
        layout = QVBoxLayout()
        layout.addWidget(label)
        group_box.setLayout(layout)

        # Creating the vertical layout for the Performance Evaluation View
        main_layout = QVBoxLayout()
        main_layout.addWidget(group_box)
        self.setLayout(main_layout)

