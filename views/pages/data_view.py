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

        # Create a scroll area and set the tab widget as its widget
        self.scroll_create_shapefile = QScrollArea()
        self.scroll_create_shapefile.setWidget(create_shapefile_view)
        self.scroll_create_shapefile.setWidgetResizable(True)

        scroll_dataset = QScrollArea()
        scroll_dataset.setWidget(dataset_view)
        scroll_dataset.setWidgetResizable(True)

        scroll_downloader = QScrollArea()
        scroll_downloader.setWidget(downloader_view)
        scroll_downloader.setWidgetResizable(True)

        # Creating the tab widget and adding the views as tabs
        self.tab_widget = TabWidget()
        self.tab_widget.addTab(self.scroll_create_shapefile, "Create Shapefile")
        self.tab_widget.addTab(scroll_dataset, "Dataset")
        self.tab_widget.addTab(scroll_downloader, "Downloader")

        # Creating the vertical layout for the data page
        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        # Connect the signals to the slots
        self.tab_widget.currentChanged.connect(self.tab_changed)

    def tab_changed(self, index):
        # Logic to display the corresponding page for the selected tab
        if index == 0:  # Create_shapefile tab
            self.tab_widget.setCurrentIndex(0)
        elif index == 1:  # Dataset tab
            self.tab_widget.setCurrentIndex(1)
        elif index == 2:  # Downloader tab
            self.tab_widget.setCurrentIndex(2)
