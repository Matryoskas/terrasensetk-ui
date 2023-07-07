import sys
from qt_core import *
from views.windows.main_window_view import MainWindowView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("TerrasenseTK")

        # SETUP MAIN WINDOW
        self.ui = MainWindowView()
        self.ui.setup_ui(self)

        # Connecting the signals to the slots
        self.ui.data_button.clicked.connect(self.show_data_view)
        self.ui.algorithms_button.clicked.connect(self.show_algorithms_view)
        self.ui.Performance_evaluation_button.clicked.connect(self.show_Performance_evaluation_view)

        self.show()

    def show_data_view(self):
        # Showing the data page
        self.ui.pages.setCurrentWidget(self.ui.data_view)

    def show_algorithms_view(self):
        # Showing the algorithms page
        self.ui.pages.setCurrentWidget(self.ui.algorithms_view)
    
    def show_Performance_evaluation_view(self):
        # Showing the Performance evawluation page
        self.ui.pages.setCurrentWidget(self.ui.performance_evaluation_view)
    
if __name__ == "__main__":
    # Create the Qt application
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("resources/icons/main_window_icons/TSTK_icon.png"))
    # Create the main window
    window = MainWindow()
    # Start the Qt event loop
    sys.exit(app.exec())

