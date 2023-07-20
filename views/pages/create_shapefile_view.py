from qt_core import *
from resources.widgets.push_button import PushButton
import fiona
import pandas as pd
import sentinelhub as sh
import os

class LineWidget(QWidget):
    def __init__(self, line_num):
        super().__init__()

        # Label for the date field
        self.date_label = QLabel("Date:")

        # Line edit for displaying and editing the date
        self.date_edit = QDateEdit()
        self.date_edit.setDisplayFormat("yyyy-MM-dd")

        # Label for the longitude field
        self.longitude_label = QLabel("Longitude:")

        # Line edit for displaying and editing the longitude
        self.longitude_line_edit = QLineEdit()

        # Label for the latitude field
        self.latitude_label = QLabel("Latitude:")

        # Line edit for displaying and editing the latitude
        self.latitude_line_edit = QLineEdit()

        self.samp_num_label = QLabel("Sample Number:")
        self.sampnum_line_edit = QLineEdit()

        self.calcium_label = QLabel("Calcium:")
        self.calcium_line_edit = QLineEdit()

        self.magnesium_label = QLabel("Magnesium:")
        self.magnesium_line_edit = QLineEdit()

        self.sodium_label = QLabel("Sodium:")
        self.sodium_line_edit = QLineEdit()

        self.potassium_label = QLabel("Potassium:")
        self.potassium_line_edit = QLineEdit()

        self.exchangeable_sodium_label = QLabel("Exchangeable Sodium:")
        self.exchangeable_sodium_line_edit = QLineEdit()

        self.clay_ratio_label = QLabel("Clay Ratio:")
        self.clay_ratio_line_edit = QLineEdit()

        self.cec_nh4_ph_7_label = QLabel("CEC NH4 pH 7:")
        self.cec_nh4_ph_7_line_edit = QLineEdit()

        self.cacl_label = QLabel("Calcium Chloride:")
        self.cacl_line_edit = QLineEdit()

        self.hide_optional_fields()

        # DATA LAYOUT
        #//////////////////////////////////////////////////////////////////////////

        self.check_box = QCheckBox("Show optional fields")

        self.data_layout = QGridLayout()
        self.data_layout.addWidget(self.date_label, 0, 0)
        self.data_layout.addWidget(self.latitude_label, 0, 1)
        self.data_layout.addWidget(self.longitude_label, 0, 2)
        self.data_layout.addWidget(self.date_edit, 1, 0)
        self.data_layout.addWidget(self.latitude_line_edit, 1, 1)
        self.data_layout.addWidget(self.longitude_line_edit, 1, 2)
        self.data_layout.addWidget(self.samp_num_label, 2, 0)
        self.data_layout.addWidget(self.calcium_label, 2, 1)
        self.data_layout.addWidget(self.magnesium_label, 2, 2)
        self.data_layout.addWidget(self.sampnum_line_edit, 3, 0)
        self.data_layout.addWidget(self.calcium_line_edit, 3, 1)
        self.data_layout.addWidget(self.magnesium_line_edit, 3, 2)
        self.data_layout.addWidget(self.sodium_label, 4, 0)
        self.data_layout.addWidget(self.potassium_label, 4, 1)
        self.data_layout.addWidget(self.exchangeable_sodium_label, 4, 2)
        self.data_layout.addWidget(self.sodium_line_edit, 5, 0)
        self.data_layout.addWidget(self.potassium_line_edit, 5, 1)
        self.data_layout.addWidget(self.exchangeable_sodium_line_edit, 5, 2)
        self.data_layout.addWidget(self.clay_ratio_label, 6, 0)
        self.data_layout.addWidget(self.cec_nh4_ph_7_label, 6, 1)
        self.data_layout.addWidget(self.cacl_label, 6, 2)
        self.data_layout.addWidget(self.clay_ratio_line_edit, 7, 0)
        self.data_layout.addWidget(self.cec_nh4_ph_7_line_edit, 7, 1)
        self.data_layout.addWidget(self.cacl_line_edit, 7, 2)

        line_label = QLabel(f"Line {line_num}:")
        line_layout = QVBoxLayout()
        line_layout.addWidget(line_label)
        line_layout.addWidget(self.check_box)
        line_layout.addLayout(self.data_layout)
        self.setLayout(line_layout)

        # CONNECT BUTTONS AND WIDGETS TO FUNCTIONS
        #//////////////////////////////////////////////////////////////////////////

        # Connect check_box to show_optional_fields function
        self.check_box.toggled.connect(self.react_to_toggle)

    # FUNCTIONS
    #//////////////////////////////////////////////////////////////////////////

    def react_to_toggle(self):
        if self.check_box.isChecked():
            self.show_optional_fields()
        else:
            self.hide_optional_fields()

    def show_optional_fields(self):
        self.samp_num_label.setVisible(True)
        self.calcium_label.setVisible(True)
        self.magnesium_label.setVisible(True)
        self.sampnum_line_edit.setVisible(True)
        self.calcium_line_edit.setVisible(True)
        self.magnesium_line_edit.setVisible(True)
        self.sodium_label.setVisible(True)
        self.potassium_label.setVisible(True)
        self.exchangeable_sodium_label.setVisible(True)
        self.sodium_line_edit.setVisible(True)
        self.potassium_line_edit.setVisible(True)
        self.exchangeable_sodium_line_edit.setVisible(True)
        self.clay_ratio_label.setVisible(True)
        self.cec_nh4_ph_7_label.setVisible(True)
        self.cacl_label.setVisible(True)
        self.clay_ratio_line_edit.setVisible(True)
        self.cec_nh4_ph_7_line_edit.setVisible(True)
        self.cacl_line_edit.setVisible(True)
    
    def hide_optional_fields(self):
        self.samp_num_label.setHidden(True)
        self.calcium_label.setHidden(True)
        self.magnesium_label.setHidden(True)
        self.sampnum_line_edit.setHidden(True)
        self.calcium_line_edit.setHidden(True)
        self.magnesium_line_edit.setHidden(True)
        self.sodium_label.setHidden(True)
        self.potassium_label.setHidden(True)
        self.exchangeable_sodium_label.setHidden(True)
        self.sodium_line_edit.setHidden(True)
        self.potassium_line_edit.setHidden(True)
        self.exchangeable_sodium_line_edit.setHidden(True)
        self.clay_ratio_label.setHidden(True)
        self.cec_nh4_ph_7_label.setHidden(True)
        self.cacl_label.setHidden(True)
        self.clay_ratio_line_edit.setHidden(True)
        self.cec_nh4_ph_7_line_edit.setHidden(True)
        self.cacl_line_edit.setHidden(True)

class CreateShapefileView(QWidget):
    def __init__(self):
        self.line_num = 2
        super().__init__()

        # DESTINATION FOLDER
        #//////////////////////////////////////////////////////////////////////////
        # Label for the destination folder
        shapefile_path_label = QLabel("Destination Folder:")

        # Line edit for displaying and editing the selected folder
        self.shapefile_path_line_edit = QLineEdit()
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
        self.shapefile_name_line_edit = QLineEdit()

        # Layout for shapefile_name_line_edit
        shapefile_name_layout = QHBoxLayout()
        shapefile_name_layout.setContentsMargins(0, 0, 0, 0)
        shapefile_name_layout.addWidget(self.shapefile_name_line_edit)

        # DATA LAYOUT
        #//////////////////////////////////////////////////////////////////////////
        data_label = QLabel("Data:")
        data_label.setFixedSize(150, 30)

        # ADD LINE BUTTON
        #//////////////////////////////////////////////////////////////////////////

        add_line_button = PushButton('')
        add_line_icon = QIcon("resources/icons/create_shapefile_icons/add_icon.svg")
        add_line_button.setIcon(add_line_icon)

        # REMOVE LINE BUTTON
        #//////////////////////////////////////////////////////////////////////////

        self.remove_line_button = PushButton('')
        self.remove_line_button.setHidden(True)
        remove_line_icon = QIcon("resources/icons/create_shapefile_icons/minus_icon.svg")
        self.remove_line_button.setIcon(remove_line_icon)

        # CREATE BUTTON
        #//////////////////////////////////////////////////////////////////////////
        create_button = PushButton("Create Shapefile")
        create_button.setFixedWidth(160)
        convert_icon = QIcon("resources/icons/convert_page_icons/convert_icon.png")
        create_button.setIcon(convert_icon)

        # MAIN LAYOUT
        #//////////////////////////////////////////////////////////////////////////
        main_layout = QHBoxLayout()
        # Frame to occupy space on the left
        left_empty_frame = QFrame()
        left_empty_frame.setFixedWidth(40)
        left_empty_frame.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # Adding the empty frame to the left side of the horizontal layout
        main_layout.addWidget(left_empty_frame)

        # Creating a horizontal layout for the add and remove buttons

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(add_line_button)
        self.buttons_layout.addWidget(self.remove_line_button)

        # Creating a vertical layout for the content
        self.content_layout = QVBoxLayout()
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(shapefile_path_label)
        self.content_layout.addLayout(shapefile_folder_layout)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(shapefile_name_label)
        self.content_layout.addLayout(shapefile_name_layout)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(data_label)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(LineWidget(1))
        self.content_layout.addSpacing(10)
        self.content_layout.addLayout(self.buttons_layout)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(create_button)
        self.content_layout.setAlignment(Qt.AlignTop)
        
        # Adding the main layout to the horizontal layout
        main_layout.addLayout(self.content_layout)
    
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
        shapefile_path_button.clicked.connect(self.choose_folder)

        # Connect convert_button to convert_to_shapefile function
        create_button.clicked.connect(self.convert_to_shapefile)

        # Connect add_line_button to add_line function
        add_line_button.clicked.connect(self.add_line)

        # Connect remove_line_button to remove_line function
        self.remove_line_button.clicked.connect(self.remove_line)

    #FUNCTIONS
    #//////////////////////////////////////////////////////////////////////////

    def choose_folder(self):
        folder_dialog = QFileDialog.getExistingDirectory(
            self, "Choose Folder", QDir.homePath()
        )
        if folder_dialog:
            self.shapefile_path_line_edit.setText(folder_dialog)

    def add_line(self):
        self.content_layout.insertWidget(self.content_layout.count() - 3, LineWidget(self.line_num))
        self.remove_line_button.setVisible(True)
        self.line_num += 1

    def remove_line(self):
        self.content_layout.itemAt(self.content_layout.count() - 4).widget().deleteLater()
        self.line_num -= 1
        if self.line_num <= 2:
            self.remove_line_button.setHidden(True)

    def page_validation(self):
        shapefile_directory = self.shapefile_path_line_edit.text()
        shapefile_name = self.shapefile_name_line_edit.text()
        
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
            print(dict_row_info)
            del(dict_row_info["latitude_std_decimal_degrees"])
            del(dict_row_info["longitude_std_decimal_degrees"])

            row_dict = {
                "geometry": {'type':'Point', 'coordinates': (row.longitude_std_decimal_degrees, row.latitude_std_decimal_degrees)},
                "properties": dict_row_info
            }
            pointShp.write(row_dict)
        pointShp.close()
        self.clear_page()
        QMessageBox.information(self, "Success", "Shapefile created successfully")

    def clear_page(self):
        # Clear download destination field
        self.shapefile_path_line_edit.clear()
        # Clear shapefile name field
        self.shapefile_name_line_edit.clear()