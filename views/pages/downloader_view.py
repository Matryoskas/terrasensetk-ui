from qt_core import *
import terrasensetk as tstk
import sentinelhub as sh
import geopandas as gpd
from models.downloader_model import DownloaderModel
from resources.widgets.push_button import PushButton
from resources.widgets.combo_box import ComboBox
from resources.widgets.check_box import CheckBox
from resources.widgets.line_edit import LineEdit
from resources.widgets.spin_box import SpinBox
from resources.widgets.double_spin_box import DoubleSpinBox

class DownloaderView(QWidget):
    def __init__(self):
        super().__init__()

        self.model = DownloaderModel()

        # SHAPEFILE
        #//////////////////////////////////////////////////////////////////////////
        # Shapefile label
        shapefile_label = QLabel("Shapefile:")

        # Shapefile line edit
        self.shapefile_line_edit = LineEdit()
        self.shapefile_line_edit.setReadOnly(True)

        # Button to select shapefile
        select_file_button = PushButton("Select file")
        select_file_button.setFixedWidth(100)

        # Shapefile layout
        shapefile_layout = QHBoxLayout()
        shapefile_layout.setContentsMargins(0, 0, 0, 0)
        shapefile_layout.addWidget(self.shapefile_line_edit) 
        shapefile_layout.addWidget(select_file_button)

        # DATE COLUMN
        #//////////////////////////////////////////////////////////////////////////
        # Date column label
        self.date_column_label = QLabel("Date Column:")
        self.date_column_label.setHidden(True)

        # Date column combo box
        self.date_column_combo = ComboBox()
        self.date_column_combo.setHidden(True)

        # DATE FORMAT
        #//////////////////////////////////////////////////////////////////////////
        # Date format label
        date_format_label = QLabel("Date Format:")

        # Date format combo box
        self.date_format_combo = ComboBox()
        self.date_format_combo.addItems(["YYYY-MM-DD", "DD-MM-YYYY"])

        # PADDING DAYS
        #//////////////////////////////////////////////////////////////////////////
        # Padding days label
        padding_days_label = QLabel("Padding Days:")

        # Padding days spin box
        self.padding_days_spinbox = SpinBox()
        self.padding_days_spinbox.setMinimum(0)

        #SATELLITES AND BANDS
        #//////////////////////////////////////////////////////////////////////////
        # Label for the satellites
        satellites_label = QLabel("Satellites:")

        # ComboBox for selecting satellites
        self.satellites_combo = ComboBox()
        self.satellites_combo.setFixedWidth(100)

        # Checkbox for selecting all bands
        self.select_all_bands_checkbox = CheckBox("Select All Bands")

        # QGroupBox for the bands
        self.bands_groupbox = QGroupBox("Bands")
        self.bands_groupbox.setMinimumWidth(650)
        self.bands_layout = QVBoxLayout()
        self.bands_groupbox.setLayout(self.bands_layout)
        
        # MAX CLOUD COVERAGE
        #//////////////////////////////////////////////////////////////////////////
        # Max cloud coverage label
        max_cloud_coverage_label = QLabel("Max Cloud Coverage:")

        # Max cloud coverage spin box
        self.max_cloud_coverage_spinbox = DoubleSpinBox()
        self.max_cloud_coverage_spinbox.setRange(0, 1)
        self.max_cloud_coverage_spinbox.setSingleStep(0.001)
        self.max_cloud_coverage_spinbox.setDecimals(3)

        # EXPECTED BBOX SIZE
        #//////////////////////////////////////////////////////////////////////////
        # Expected bbox size label
        expected_bbox_size_label = QLabel("Expected BBox Size:")

        # Expected bbox size spin box
        self.expected_bbox_size_spinbox = DoubleSpinBox()
        self.expected_bbox_size_spinbox.setMinimum(0.001)
        self.expected_bbox_size_spinbox.setDecimals(3)

        # DESTINATION FOLDER
        #//////////////////////////////////////////////////////////////////////////
        # Label for the destination folder
        download_path_label = QLabel("Download Path:")

        # Line edit for displaying and editing the selected folder
        self.download_path_line_edit = LineEdit()
        self.download_path_line_edit.setReadOnly(True)

        # Button for choosing a folder
        download_path_button = PushButton("Browse...")
        download_path_button.setFixedWidth(100)

        # Layout for folder_line_edit and destination_folder_button
        destination_folder_layout = QHBoxLayout()
        destination_folder_layout.setContentsMargins(0, 0, 0, 0)
        destination_folder_layout.addWidget(self.download_path_line_edit) 
        destination_folder_layout.addWidget(download_path_button)

        # DOWNLOAD BUTTON
        #//////////////////////////////////////////////////////////////////////////
        download_button = PushButton("Download")
        download_button.setFixedWidth(150)
        download_icon = QIcon("resources/icons/downloader_page_icons/download_arrow.png")
        download_button.setIcon(download_icon)
        
        # MAIN LAYOUT
        #//////////////////////////////////////////////////////////////////////////
        main_layout = QHBoxLayout()
        # Frame to occupy space on the left
        left_empty_frame = QFrame()
        left_empty_frame.setFixedWidth(40)
        left_empty_frame.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # Adding the empty frame to the left side of the horizontal layout
        main_layout.addWidget(left_empty_frame)

        # Creating a vertical layout for the content of the Downloader Page
        content_layout = QVBoxLayout()
        content_layout.addWidget(shapefile_label) 
        content_layout.addLayout(shapefile_layout) 
        content_layout.addSpacing(10)
        content_layout.addWidget(self.date_column_label)
        content_layout.addWidget(self.date_column_combo)
        content_layout.addSpacing(10)
        content_layout.addWidget(date_format_label)
        content_layout.addWidget(self.date_format_combo)
        content_layout.addSpacing(10)
        content_layout.addWidget(padding_days_label)
        content_layout.addWidget(self.padding_days_spinbox)
        content_layout.addSpacing(10)
        content_layout.addWidget(satellites_label) 
        content_layout.addWidget(self.satellites_combo)
        content_layout.addSpacing(10)
        content_layout.addWidget(self.select_all_bands_checkbox)
        content_layout.addWidget(self.bands_groupbox)  
        content_layout.addSpacing(10)
        content_layout.addWidget(max_cloud_coverage_label)
        content_layout.addWidget(self.max_cloud_coverage_spinbox)
        content_layout.addSpacing(10)
        content_layout.addWidget(expected_bbox_size_label)
        content_layout.addWidget(self.expected_bbox_size_spinbox)
        content_layout.addSpacing(10)
        content_layout.addWidget(download_path_label)
        content_layout.addLayout(destination_folder_layout)
        content_layout.addSpacing(10) 
        content_layout.addWidget(download_button)
        content_layout.setAlignment(Qt.AlignTop)
        
        # Adding the main layout to the horizontal layout
        main_layout.addLayout(content_layout)
    
        # Creating an empty frame to occupy space on the right
        right_empty_frame = QFrame()
        right_empty_frame.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        # Adding the empty frame to the right side of the horizontal layout
        main_layout.addWidget(right_empty_frame)

        # Set the main layout
        self.setLayout(main_layout)

        # CONNECT BUTTONS AND WIDGETS TO FUNCTIONS
        #//////////////////////////////////////////////////////////////////////////
        # Connect destination_folder_button to choose_folder function
        download_path_button.clicked.connect(self.choose_folder)

        # Update satellites list
        self.update_satellites()

        # Connect select_all_bands_checkbox to select_all_bands function
        self.select_all_bands_checkbox.stateChanged.connect(self.select_all_bands)

        # Connect satellites_combo to update_bands function
        self.satellites_combo.currentIndexChanged.connect(self.update_bands)

        # Connect select_file_button to choose_shapefile function
        select_file_button.clicked.connect(self.choose_shapefile)

        # Connect download_button to download_images function
        download_button.clicked.connect(self.download_images)

        self.shapefile_line_edit.textChanged.connect(self.add_shapefile_columns_to_combo_box)

    #FUNCTIONS
    #//////////////////////////////////////////////////////////////////////////

    def choose_folder(self):
        folder_dialog = QFileDialog.getExistingDirectory(
            self, "Choose Folder", QDir.homePath()
        )
        if folder_dialog:
            self.download_path_line_edit.setText(folder_dialog)
    
    def update_satellites(self):
        satellites = self.model.get_satellites()
        self.satellites_combo.clear()
        self.satellites_combo.addItems(satellites)
        self.update_bands()

    def update_bands(self):
        while self.bands_layout.count():
            child = self.bands_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        key = self.satellites_combo.currentText()
        values = self.model.get_bands(key)
        for value in values:
            checkbox = CheckBox(f"{value['code']} - {value['description']}")
            checkbox.setChecked(False)
            checkbox.stateChanged.connect(self.band_state_changed)
            self.bands_layout.addWidget(checkbox)

        self.select_all_bands_checkbox.blockSignals(True)
        self.select_all_bands_checkbox.setChecked(False)
        self.select_all_bands_checkbox.blockSignals(False)

    def band_state_changed(self):
        all_bands_selected = True
        for i in range(self.bands_layout.count()):
            widget = self.bands_layout.itemAt(i).widget()
            if isinstance(widget, QCheckBox):
                if not widget.isChecked():
                    all_bands_selected = False
                    break
        self.select_all_bands_checkbox.blockSignals(True) 
        self.select_all_bands_checkbox.setChecked(all_bands_selected)
        self.select_all_bands_checkbox.blockSignals(False)  

    def select_all_bands(self):
        checked = self.select_all_bands_checkbox.isChecked()
        for i in range(self.bands_layout.count()):
            widget = self.bands_layout.itemAt(i).widget()
            if isinstance(widget, QCheckBox):
                widget.setChecked(checked)
    
    def get_selected_bands(self):
        selected_bands = []
        for i in range(self.bands_layout.count()):
            widget = self.bands_layout.itemAt(i).widget()
            if isinstance(widget, QCheckBox) and widget.isChecked():
                band_code = widget.text().split(" - ")[0]
                selected_bands.append(band_code)
        return selected_bands

    def choose_shapefile(self):
        #Choose a shapefile and set its path to the line edit
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle("Choose Shapefile")
        file_dialog.setNameFilter("Shapefile (*.shp)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            self.shapefile_line_edit.setText(selected_file)

    def add_shapefile_columns_to_combo_box(self, path):
        if path != "":
            for i in range (self.date_column_combo.count()):
                self.date_column_combo.removeItem(0)
            self.date_column_label.setHidden(False)
            self.date_column_combo.setHidden(False)
            dataset_shape = gpd.read_file(path)
            self.date_column_combo.addItems(list(dataset_shape.columns.values))

    def page_validation(self):
        download_path = self.download_path_line_edit.text()
        
        if not download_path:
            QMessageBox.warning(self, "Destination Folder Not Specified", "Please specify the destination folder for the download!")
            return -1
        bands_selected = False
        for i in range(self.bands_layout.count()):
            widget = self.bands_layout.itemAt(i).widget()
            if isinstance(widget, QCheckBox) and widget.isChecked():
                bands_selected = True
                break
        if not bands_selected:
            QMessageBox.warning(self, "Field not filled", "Please select at least one band")
            return -1
        shapefile_path = self.shapefile_line_edit.text()
        
        if not shapefile_path:
            QMessageBox.warning(self, "Field not filled", "Please select a shapefile")
            return -1
    
    def download_images(self):
        if self.page_validation() == -1:
            return
        config = sh.SHConfig()
        config.sh_client_id= r'9bd0a46d-3d5b-4dc0-98b5-546b3635f9f3'
        config.sh_client_secret = r'~)x%O:RiSc|F5i+SIL}^fZUlWOa.;E^{_:&!J6@:'
        config.save()

        # Variables needed to download the images
        shapefile_path = self.shapefile_line_edit.text()
        bands = self.get_selected_bands()
        download_path = self.download_path_line_edit.text()
        date_column = self.date_column_combo.currentText()
        if self.date_format_combo.currentText() == "YYYY-MM-DD":
            date_format = "%Y-%m-%d"
        else:
            date_format = "%d-%m-%Y"
        padding_days = self.padding_days_spinbox.value()
        maxcc = self.max_cloud_coverage_spinbox.value()
        expected_bbox_size = self.expected_bbox_size_spinbox.value()
        
        # Download Images
        down = tstk.CustomDownloader(shapefile_path)
        down.get_bbox(expected_bbox_size,True)
        down.download_images(download_path, bands, date_field=date_column, date_fmt=date_format, padding_days=padding_days, maxcc=maxcc)
        QMessageBox.information(self, "Download started", f"Download started for: {download_path}")
        self.clear_page()
        
    def clear_page(self):
        # Clear download destination field
        self.download_path_line_edit.clear()
        # Clear satellite selection
        self.satellites_combo.setCurrentIndex(0)
        # Unchecking the option "Select all bands."
        self.select_all_bands_checkbox.setChecked(False)
        # Clear band selection
        for i in range(self.bands_layout.count()):
            widget = self.bands_layout.itemAt(i).widget()
            if isinstance(widget, QCheckBox):
                widget.setChecked(False)
        # Clear shapefile field
        self.shapefile_line_edit.clear()
        # Clear padding days field
        self.padding_days_spinbox.setValue(0)
        # Clear max cloud coverage field
        self.max_cloud_coverage_spinbox.setValue(0)
        # Clear expected bbox size field
        self.expected_bbox_size_spinbox.setValue(0)
        # Clear date column combo box
        self.date_column_label.setHidden(True)
        self.date_column_combo.setHidden(True)
        for i in range (self.date_column_combo.count()):
            self.date_column_combo.removeItem(0)
        # Clear date format combo box
        self.date_format_combo.setCurrentIndex(0)