from qt_core import *
from resources.widgets.push_button import PushButton
from resources.widgets.line_edit import LineEdit
import fiona
import pandas as pd
import sentinelhub as sh
import os

class DatasetView(QWidget):
    def __init__(self):
        super().__init__()
        
        # CSV FILE
        #//////////////////////////////////////////////////////////////////////////
        # Label for the csv file path
        csv_path_label = QLabel("CSV Path:")

        # Line edit for displaying and editing the selected csv file
        self.csv_path_line_edit = LineEdit()
        self.csv_path_line_edit.setReadOnly(True)

        # Button for choosing a csv file
        csv_path_button = PushButton("Browse...")
        csv_path_button.setFixedWidth(100)

        # Layout for csv_path_line_edit and csv_path_button
        csv_folder_layout = QHBoxLayout()
        csv_folder_layout.setContentsMargins(0, 0, 0, 0)
        csv_folder_layout.addWidget(self.csv_path_line_edit) 
        csv_folder_layout.addWidget(csv_path_button)

        # DESTINATION FOLDER
        #//////////////////////////////////////////////////////////////////////////
        # Label for the destination folder
        shapefile_path_label = QLabel("Destination Folder:")

        # Line edit for displaying and editing the selected folder
        self.shapefile_path_line_edit = LineEdit()
        self.shapefile_path_line_edit.setReadOnly(True)

        # Button for choosing a folder
        shapefile_path_button = PushButton("Browse...")
        shapefile_path_button.setFixedWidth(100)

        # Layout for folder_line_edit and destination_folder_button
        shapefile_folder_layout = QHBoxLayout()
        shapefile_folder_layout.setContentsMargins(0, 0, 0, 0)
        shapefile_folder_layout.addWidget(self.shapefile_path_line_edit) 
        shapefile_folder_layout.addWidget(shapefile_path_button)

        # NAME OF THE SHAPEFILE
        #//////////////////////////////////////////////////////////////////////////
        # Label for the name of the shapefile
        shapefile_name_label = QLabel("Name of the shapefile:")

        # Line edit for displaying and editing the name of the shapefile
        self.shapefile_name_line_edit = LineEdit()

        # Layout for shapefile_name_line_edit
        shapefile_name_layout = QHBoxLayout()
        shapefile_name_layout.setContentsMargins(0, 0, 0, 0)
        shapefile_name_layout.addWidget(self.shapefile_name_line_edit)

        # CONVERT BUTTON
        #//////////////////////////////////////////////////////////////////////////
        convert_button = PushButton("Convert")
        convert_button.setFixedWidth(150)
        convert_icon = QIcon("resources/icons/convert_page_icons/convert_icon.png")
        convert_button.setIcon(convert_icon)

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
        content_layout.addWidget(csv_path_label)
        content_layout.addLayout(csv_folder_layout)  
        content_layout.addSpacing(10)
        content_layout.addWidget(shapefile_path_label)
        content_layout.addLayout(shapefile_folder_layout)
        content_layout.addSpacing(10)
        content_layout.addWidget(shapefile_name_label)
        content_layout.addLayout(shapefile_name_layout)
        content_layout.addSpacing(10)
        content_layout.addWidget(convert_button)
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

        # Connect select_file_button to choose_shapefile function
        csv_path_button.clicked.connect(self.choose_csv)

        # Connect destination_folder_button to choose_folder function
        shapefile_path_button.clicked.connect(self.choose_folder)

        # Connect convert_button to convert_to_shapefile function
        convert_button.clicked.connect(self.convert_to_shapefile)

    #FUNCTIONS
    #//////////////////////////////////////////////////////////////////////////

    def choose_csv(self):
        #Choose a csv and set its path to the line edit
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle("Choose CSV File")
        file_dialog.setNameFilter("Comma-separated Values (*.csv)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            self.csv_path_line_edit.setText(selected_file)

    def choose_folder(self):
        folder_dialog = QFileDialog.getExistingDirectory(
            self, "Choose Folder", QDir.homePath()
        )
        if folder_dialog:
            self.shapefile_path_line_edit.setText(folder_dialog)
    
    def page_validation(self):
        shapefile_directory = self.shapefile_path_line_edit.text()
        csv_path = self.csv_path_line_edit.text()
        shapefile_name = self.shapefile_name_line_edit.text()
        
        if not csv_path:
            QMessageBox.warning(self, "Field not filled", "Please select a CSV file")
            return -1
        if not shapefile_directory:
            QMessageBox.warning(self, "Destination Folder Not Specified", "Please specify the destination folder for the Shapefile")
            return -1
        if not shapefile_name:
            QMessageBox.warning(self, "Field not filled", "Please specify the name of the Shapefile")
            return -1

    def convert_to_shapefile(self):
        if self.page_validation() == -1:
            return
        
        config = sh.SHConfig()
        config.sh_client_id= r'9bd0a46d-3d5b-4dc0-98b5-546b3635f9f3'
        config.sh_client_secret = r'~)x%O:RiSc|F5i+SIL}^fZUlWOa.;E^{_:&!J6@:'
        config.save()
        
        csv_path = self.csv_path_line_edit.text()
        shapefile_dir_path = self.shapefile_path_line_edit.text() + '/' + self.shapefile_name_line_edit.text()
        try:
            os.mkdir(shapefile_dir_path)
        except FileExistsError:
            pass
        shapefile_path = shapefile_dir_path + '/' + self.shapefile_name_line_edit.text() + '.shp'

        gt = pd.read_csv(csv_path)

        schema_props = ""
        for col in list(gt.columns):
            schema_props += f"('{col}','str'),"

        schema = {
            'geometry':'Point',
            'properties':[('pedlabsampnum','str'),('observation_date','int'),('date','date'),('ca_nh4_ph_7','float'),('mg_nh4_ph_7','float'),('na_nh4_ph_7','float'),('k_nh4_ph_7','float'),('exchangeable_sodium','float'),('cec7_clay_ratio','float'),('cec_nh4_ph_7','float'),('ph_cacl2','str')]
        }
        
        pointShp = fiona.open(shapefile_path, mode='w', driver='ESRI Shapefile', schema = schema, crs = "WGS84")

        for index, row in gt.iterrows():
            
            dict_row_info = row.to_dict()
            del(dict_row_info["latitude_std_decimal_degrees"])
            del(dict_row_info["longitude_std_decimal_degrees"])

            row_dict = {
                "geometry": {'type':'Point', 'coordinates': (row["longitude_std_decimal_degrees"],row["latitude_std_decimal_degrees"])},
                "properties": dict_row_info
            }
            pointShp.write(row_dict)
        pointShp.close()
        self.clear_page()
        QMessageBox.information(self, "Success", "Shapefile created successfully")

    def clear_page(self):
        # Clear csv field
        self.csv_path_line_edit.clear()
        # Clear download destination field
        self.shapefile_path_line_edit.clear()
        # Clear shapefile name field
        self.shapefile_name_line_edit.clear()