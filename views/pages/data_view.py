from qt_core import *
from views.pages.downloader_view import DownloaderView
from views.pages.create_shapefile_view import CreateShapefileView
from views.pages.plot_data_view import PlotDataView
from resources.widgets.tab_widget import TabWidget

class DataView(QWidget):
    def __init__(self):
        super().__init__()
        self.csv_path_line_edit_text = ""

        # Creating the views for each tab
        downloader_view = DownloaderView()
        self.create_shapefile_view = CreateShapefileView()
        self.plot_data_view = PlotDataView()

        # Create a scroll area and set the tab widget as its widget
        scroll_create_shapefile = QScrollArea()
        scroll_create_shapefile.setWidget(self.create_shapefile_view)
        scroll_create_shapefile.setWidgetResizable(True)

        scroll_downloader = QScrollArea()
        scroll_downloader.setWidget(downloader_view)
        scroll_downloader.setWidgetResizable(True)

        scroll_plot_data = QScrollArea()
        scroll_plot_data.setWidget(self.plot_data_view)
        scroll_plot_data.setWidgetResizable(True)

        # Creating the tab widget and adding the views as tabs
        self.tab_widget = TabWidget()
        self.tab_widget.addTab(scroll_create_shapefile, "Create Shapefile")
        self.tab_widget.addTab(scroll_downloader, "Download Images")
        self.tab_widget.addTab(scroll_plot_data, "Plot Data")

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
        elif index == 1:  # Downloader tab
            self.tab_widget.setCurrentIndex(1)
        elif index == 2:
            if self.create_shapefile_view.csv_path_line_edit.text() != "" and self.create_shapefile_view.csv_path_line_edit.text() != self.csv_path_line_edit_text:
                self.csv_path_line_edit_text = self.create_shapefile_view.csv_path_line_edit.text()
                self.tab_widget.setCurrentIndex(2)
                self.plot_data_view.allow_input(self.create_shapefile_view.csv)