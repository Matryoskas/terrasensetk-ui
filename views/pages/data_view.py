from qt_core import *
from views.pages.downloader_view import DownloaderView
from views.pages.dataset_view import DatasetView
from views.pages.create_shapefile_view import CreateShapefileView
from resources.widgets.tab_widget import TabWidget

class DataView(QWidget):
    def __init__(self):
        super().__init__()

        # Creating the views for each tab
        downloader_view = DownloaderView()
        dataset_view = DatasetView()
        create_shapefile_view = CreateShapefileView()

        # Creating the tab widget and adding the views as tabs
        self.tab_widget = TabWidget()
        self.tab_widget.addTab(create_shapefile_view, "Create Shapefile")
        self.tab_widget.addTab(dataset_view, "Dataset")
        self.tab_widget.addTab(downloader_view, "Downloader")

        # Create a scroll area and set the tab widget as its widget
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.tab_widget)
        scroll_area.setWidgetResizable(True)
    
        # Remove the border of the scroll area using Qt StyleSheet
        scroll_area.setStyleSheet("QScrollArea { border: none; }")

        # Creating the vertical layout for the data page
        layout = QVBoxLayout()
        layout.addWidget(scroll_area)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove the outer margins
        self.setLayout(layout)

        # Connect the signals to the slots
        self.tab_widget.currentChanged.connect(self.tab_changed)

    def tab_changed(self, index):
        # Logic to display the corresponding page for the selected tab
        if index == 0:  # Create_shapefile tab
            self.show_create_shapefile()
        elif index == 1:  # Dataset tab
            self.show_dataset()
        elif index == 2:  # Downloader tab
            self.show_downloader()

    def show_create_shapefile(self):
        # Logic to display the create_shapefile page
        self.tab_widget.setCurrentIndex(0)

    def show_dataset(self): 
        # Logic to display the dataset page
        self.tab_widget.setCurrentIndex(1)

    def show_downloader(self):
        # Logic to display the downloader page
        self.tab_widget.setCurrentIndex(2)


