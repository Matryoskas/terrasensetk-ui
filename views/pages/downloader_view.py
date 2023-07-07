from qt_core import *
import terrasensetk as tstk
from models.downloader_model import DownloaderModel
from resources.widgets.push_button import PushButton
from resources.widgets.line_edit import LineEdit
from resources.widgets.combo_box import ComboBox
from resources.widgets.check_box import CheckBox
from resources.widgets.date_edit import DateEdit
from resources.widgets.spin_box import SpinBox

class DownloaderView(QWidget):
    def __init__(self):
        super().__init__()

        self.model = DownloaderModel()
    
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

        #DATE OF IMAGES
        #//////////////////////////////////////////////////////////////////////////
        # Date of images GroupBox
        self.date_group_box = QGroupBox("Date of Images")

        # Date of images radio buttons -> "Shapefile Dates"(True) "Single Date" and "File with Dates"
        self.radio_shapefile_dates = QRadioButton("Shapefile Dates")
        self.radio_single_date = QRadioButton("Single Date")
        self.radio_file_with_dates = QRadioButton("File with Dates")
        self.radio_shapefile_dates.setChecked(True)  

        # DATE OF IMAGES -> Shapefile Dates
        #//////////////////////////////////////////////////////////////////////////
         # Shapefile Dates -> Days before label and spinBox
        self.shapefile_days_before_label = QLabel('Number of Days Before:')
        self.shapefile_days_before_spinbox = SpinBox()
        self.shapefile_days_before_spinbox.setMinimum(0)

        # Shapefile Dates -> Days before layout
        shapefile_days_before_layout = QVBoxLayout()
        shapefile_days_before_layout.addWidget(self.shapefile_days_before_label)
        shapefile_days_before_layout.addWidget(self.shapefile_days_before_spinbox)
    
        # Shapefile Dates -> Days after label and spinBox
        self.shapefile_days_after_label = QLabel('Number of Days After:')
        self.shapefile_days_after_spinbox = SpinBox()
        self.shapefile_days_after_spinbox.setMinimum(0)

        # Shapefile Dates -> Days after layout
        shapefile_days_after_layout = QVBoxLayout()
        shapefile_days_after_layout.addWidget(self.shapefile_days_after_label)
        shapefile_days_after_layout.addWidget(self.shapefile_days_after_spinbox)

        # Shapefile Dates -> Days layout = shapefile_days_before_layout + shapefile_days_after_layout
        shapefile_days_layout = QHBoxLayout()
        shapefile_days_layout.addLayout(shapefile_days_before_layout)
        shapefile_days_layout.addLayout(shapefile_days_after_layout)

        # DATE OF IMAGES -> SINGLE DATE
        #//////////////////////////////////////////////////////////////////////////
        # Single Date label and dateEdit
        self.label_single_date = QLabel("Choose a Date:")
        self.single_date = DateEdit(QDate.currentDate())
        self.single_date.setCalendarPopup(True)
       
        # Single Date -> Days before label and spinBox
        self.days_before_label = QLabel('Number of Days Before:')
        self.days_before_spinbox = SpinBox()
        self.days_before_spinbox.setMinimum(0)

        # Single Date -> Days before layout
        days_before_layout = QVBoxLayout()
        days_before_layout.addWidget(self.days_before_label)
        days_before_layout.addWidget(self.days_before_spinbox)
    
        # Single Date -> Days after label and spinBox
        self.days_after_label = QLabel('Number of Days After:')
        self.days_after_spinbox = SpinBox()
        self.days_after_spinbox.setMinimum(0)

        # Single Date -> Days after layout
        days_after_layout = QVBoxLayout()
        days_after_layout.addWidget(self.days_after_label)
        days_after_layout.addWidget(self.days_after_spinbox)

        # Single Date -> Days layout = days_before_layout + days_after_layout
        single_date_days_layout = QHBoxLayout()
        single_date_days_layout.addLayout(days_before_layout)
        single_date_days_layout.addLayout(days_after_layout)

        # DATE OF IMAGES -> FILE WITH DATES
        #//////////////////////////////////////////////////////////////////////////
        # FILE WITH DATES -> Line edit and button
        self.label_file_with_dates = QLabel("Choose a Date File:")
        self.line_edit_file_with_dates = LineEdit()
        self.line_edit_file_with_dates.setReadOnly(True)
        self.date_file_button = PushButton("Browse...")

        # FILE WITH DATES -> Layout for line edit and button
        date_file_layout = QHBoxLayout()
        date_file_layout.addWidget(self.line_edit_file_with_dates)
        date_file_layout.addWidget(self.date_file_button)

        # FILE WITH DATES -> Number of days before
        self.days_before_file_label = QLabel('Number of Days Before:')
        self.days_before_file_spinbox = SpinBox()
        self.days_before_file_spinbox.setMinimum(0)

        # FILE WITH DATES -> Layout for number of days before
        days_before_file_layout = QVBoxLayout()
        days_before_file_layout.addWidget(self.days_before_file_label)
        days_before_file_layout.addWidget(self.days_before_file_spinbox)

        # FILE WITH DATES -> Days after
        self.days_after_file_label = QLabel('Number of Days After:')
        self.days_after_file_spinbox = SpinBox()
        self.days_after_file_spinbox.setMinimum(0)

        # FILE WITH DATES -> Days after layout
        days_after_file_layout = QVBoxLayout()
        days_after_file_layout.addWidget(self.days_after_file_label)
        days_after_file_layout.addWidget(self.days_after_file_spinbox)

        # FILE WITH DATES -> Days layout
        days_file_layout= QHBoxLayout()
        days_file_layout.addLayout(days_before_file_layout)
        days_file_layout.addLayout(days_after_file_layout)

        # DATE OF IMAGES -> Vertical Layout
        date_layout = QVBoxLayout()
        date_layout.addWidget(self.radio_shapefile_dates)
        date_layout.addSpacing(5)
        date_layout.addLayout(shapefile_days_layout)
        date_layout.addWidget(self.radio_single_date)
        date_layout.addSpacing(5)
        date_layout.addWidget(self.label_single_date)
        date_layout.addWidget(self.single_date)
        date_layout.addSpacing(5)
        date_layout.addLayout(single_date_days_layout)
        date_layout.addSpacing(15)
        date_layout.addWidget(self.radio_file_with_dates)
        date_layout.addSpacing(5)
        date_layout.addWidget(self.label_file_with_dates)
        date_layout.addLayout(date_file_layout)
        date_layout.addSpacing(5)
        date_layout.addLayout(days_file_layout)
     
        # Set date_group_box Layout
        self.date_group_box.setLayout(date_layout)
        
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
        content_layout.addSpacing(10)
        content_layout.addWidget(download_path_label)
        content_layout.addLayout(destination_folder_layout)  
        content_layout.addSpacing(10)
        content_layout.addWidget(satellites_label) 
        content_layout.addWidget(self.satellites_combo)
        content_layout.addSpacing(10)
        content_layout.addWidget(self.select_all_bands_checkbox)
        content_layout.addWidget(self.bands_groupbox)  
        content_layout.addSpacing(10)
        content_layout.addWidget(shapefile_label) 
        content_layout.addLayout(shapefile_layout)
        content_layout.addSpacing(10)
        content_layout.addWidget(self.date_group_box)
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

        #Disable "Single Date" and "File with Dates" options when downloader page is started
        self.shapefile_dates_selected(True)

        # Connect select_all_bands_checkbox to select_all_bands function
        self.select_all_bands_checkbox.stateChanged.connect(self.select_all_bands)

        # Connect satellites_combo to update_bands function
        self.satellites_combo.currentIndexChanged.connect(self.update_bands)

        # Connect select_file_button to choose_shapefile function
        select_file_button.clicked.connect(self.choose_shapefile)

        # Connect radio_shapefile_dates to shapefile_dates_selected function
        self.radio_shapefile_dates.toggled.connect(self.shapefile_dates_selected)

        # Connect radio_single_date to single_date_selected function
        self.radio_single_date.toggled.connect(self.single_date_selected)

        # Connect radio_file_with_dates to file_with_dates_selected function
        self.radio_file_with_dates.toggled.connect(self.file_with_dates_selected)

        # Connect download_button to download_images function
        download_button.clicked.connect(self.page_validation)

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

    def shapefile_dates_selected(self, checked):
        if checked:
            # Enable widgets related to "Shapefile Dates" option
            self.shapefile_days_before_label.setEnabled(True)
            self.shapefile_days_before_spinbox.setEnabled(True)
            self.shapefile_days_after_label.setEnabled(True)
            self.shapefile_days_after_spinbox.setEnabled(True)
            
            # Disable widgets related to "File with Dates" option
            self.label_file_with_dates.setEnabled(False)
            self.line_edit_file_with_dates.setEnabled(False)
            self.date_file_button.setEnabled(False)
            self.days_before_file_label.setEnabled(False)
            self.days_before_file_spinbox.setEnabled(False)
            self.days_after_file_label.setEnabled(False)
            self.days_after_file_spinbox.setEnabled(False)

            # Disable widgets related to "Single Date" option
            self.label_single_date.setEnabled(False)
            self.single_date.setEnabled(False)
            self.days_before_label.setEnabled(False)
            self.days_before_spinbox.setEnabled(False)
            self.days_after_label.setEnabled(False)
            self.days_after_spinbox.setEnabled(False)

    def single_date_selected(self, checked):
        if checked:
            # Enable widgets related to "Single Date" option
            self.label_single_date.setEnabled(True)
            self.single_date.setEnabled(True)
            self.days_before_label.setEnabled(True)
            self.days_before_spinbox.setEnabled(True)
            self.days_after_label.setEnabled(True)
            self.days_after_spinbox.setEnabled(True)

            # Disable widgets related to "Shapefile Dates" option
            self.shapefile_days_before_label.setEnabled(False)
            self.shapefile_days_before_spinbox.setEnabled(False)
            self.shapefile_days_after_label.setEnabled(False)
            self.shapefile_days_after_spinbox.setEnabled(False)
            
            # Disable widgets related to "File with Dates" option
            self.label_file_with_dates.setEnabled(False)
            self.line_edit_file_with_dates.setEnabled(False)
            self.date_file_button.setEnabled(False)
            self.days_before_file_label.setEnabled(False)
            self.days_before_file_spinbox.setEnabled(False)
            self.days_after_file_label.setEnabled(False)
            self.days_after_file_spinbox.setEnabled(False)

    def file_with_dates_selected(self, checked):
        if checked:
            # Enable widgets related to "File with Dates" option
            self.label_file_with_dates.setEnabled(True)
            self.line_edit_file_with_dates.setEnabled(True)
            self.date_file_button.setEnabled(True)
            self.days_before_file_label.setEnabled(True)
            self.days_before_file_spinbox.setEnabled(True)
            self.days_after_file_label.setEnabled(True)
            self.days_after_file_spinbox.setEnabled(True)

            # Disable widgets related to "Shapefile Dates" option
            self.shapefile_days_before_label.setEnabled(False)
            self.shapefile_days_before_spinbox.setEnabled(False)
            self.shapefile_days_after_label.setEnabled(False)
            self.shapefile_days_after_spinbox.setEnabled(False)
        
            # Disable widgets related to "Single Date" option
            self.label_single_date.setEnabled(False)
            self.single_date.setEnabled(False)
            self.days_before_label.setEnabled(False)
            self.days_before_spinbox.setEnabled(False)
            self.days_after_label.setEnabled(False)
            self.days_after_spinbox.setEnabled(False)

    def page_validation(self):
        download_path = self.download_path_line_edit.text()
        
        if not download_path:
            QMessageBox.warning(self, "Destination Folder Not Specified", "Please specify the destination folder for the download!")
            return
        bands_selected = False
        for i in range(self.bands_layout.count()):
            widget = self.bands_layout.itemAt(i).widget()
            if isinstance(widget, QCheckBox) and widget.isChecked():
                bands_selected = True
                break
        if not bands_selected:
            QMessageBox.warning(self, "Field not filled", "Please select at least one band")
            return
        shapefile_path = self.shapefile_line_edit.text()
        
        if not shapefile_path:
            QMessageBox.warning(self, "Field not filled", "Please select a shapefile")
            return 
        
        if self.radio_shapefile_dates.isChecked():
            result = QMessageBox.warning(self, "Warning", "Are you sure you have correctly filled in all the fields?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
            if result == QMessageBox.StandardButton.Cancel:
                return
        if self.radio_single_date.isChecked():
            QMessageBox.warning(
                self,
                "Unavailable Option",
                "The 'Single Date' option is currently unavailable. Please choose the 'Shapefile Dates' option.",
            )
            return
        elif self.radio_file_with_dates.isChecked():
            QMessageBox.warning(
                self,
                "Unavailable Option",
                "The 'File with Dates' option is currently unavailable. Please choose the 'Shapefile Dates' option.",
            )
            return
        QMessageBox.information(self, "Download started", f"Download started for: {download_path}")
        self.download_images()
        self.clear_page()
    
    def download_images(self):
        
        # Variables needed to download the images
        shapefile_path = self.shapefile_line_edit.text()
        bands = self.get_selected_bands()
        download_path = self.download_path_line_edit.text()
        days = self.shapefile_days_before_spinbox.value()
        #Variables to use in the future instead of the days variable
        '''
        days_before = self.shapefile_days_before_spinbox.value()
        days_after = self.shapefile_days_after_spinbox.value()
        '''
        
        # Download Images
        down = tstk.CustomDownloader(shapefile_path)
        down.get_bbox(500,True)
        down.download_images(download_path,bands,date_field="date",date_fmt='%Y-%m-%d',padding_days=days)
        

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
        # Uncheck date selection (Shapefile Dates, Single Date, File with Dates)
        self.radio_shapefile_dates.setChecked(True)
        self.radio_single_date.setChecked(False)
        self.radio_file_with_dates.setChecked(False)
        # Clean values from days before and after (Shapefile Dates)
        self.shapefile_days_before_spinbox.setValue(0)
        self.shapefile_days_after_spinbox.setValue(0)
        # Clean single date value and days before and after (Single Date)
        self.single_date.setDate(QDate.currentDate())
        self.days_before_spinbox.setValue(0)
        self.days_after_spinbox.setValue(0)
        # Clean file field with dates and values for days before and after (File with Dates)
        self.line_edit_file_with_dates.clear()
        self.days_before_file_spinbox.setValue(0)
        self.days_after_file_spinbox.setValue(0)

    
