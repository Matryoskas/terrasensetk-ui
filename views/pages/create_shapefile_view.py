from qt_core import *
from resources.widgets.push_button import PushButton
import fiona
import pandas as pd
import sentinelhub as sh
import os

class CSVComboBox(QComboBox):
    old_index = new_index = None

    def __init__(self, columns, id):
        super().__init__()
        self.setPlaceholderText("Select a column")
        self.addItems(columns)
        self.id = id
        self.currentIndexChanged.connect(self.update_combo_boxes)

    def disable_items_after_creation(self):
        for combo_box in self.parent().csv_combo_boxes:
            combo_box_index = combo_box.currentIndex()
            if combo_box is not self and combo_box_index != -1:
                self.model().item(combo_box_index).setEnabled(False)

    def update_combo_boxes(self, index):
        self.old_index = self.new_index
        self.new_index = index
        for combo_box in self.parent().csv_combo_boxes:
            if combo_box is not self:
                combo_box.model().item(index).setEnabled(False)
                if self.old_index is not None:
                    combo_box.model().item(self.old_index).setEnabled(True)

    def enable_item(self, index):
        if index != -1:
            self.model().item(index).setEnabled(True)

class CreateShapefileView(QWidget):
    def __init__(self):
        super().__init__()

        # CSV FILE
        #//////////////////////////////////////////////////////////////////////////
        csv_path_label = QLabel("CSV file:")
        self.csv_path_line_edit = QLineEdit()
        self.csv_path_line_edit.setReadOnly(True)
        csv_path_button = PushButton("Browse...")
        csv_path_button.setFixedWidth(100)
        csv_path_layout = QHBoxLayout()
        csv_path_layout.setContentsMargins(0, 0, 0, 0)
        csv_path_layout.addWidget(self.csv_path_line_edit)
        csv_path_layout.addWidget(csv_path_button)

        # DESTINATION FOLDER
        #//////////////////////////////////////////////////////////////////////////
        # Label for the destination folder
        shapefile_path_label = QLabel("Destination folder:")

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
        shapefile_name_label = QLabel("Shapefile name:")

        # Line edit for displaying and editing the name of the shapefile
        self.shapefile_name_line_edit = QLineEdit()

        # Layout for shapefile_name_line_edit
        shapefile_name_layout = QHBoxLayout()
        shapefile_name_layout.setContentsMargins(0, 0, 0, 0)
        shapefile_name_layout.addWidget(self.shapefile_name_line_edit)

        # ADD ROW BUTTON
        #//////////////////////////////////////////////////////////////////////////

        self.add_row_button = PushButton('')
        add_row_icon = QIcon("resources/icons/create_shapefile_icons/add_icon.svg")
        self.add_row_button.setIcon(add_row_icon)

        # REMOVE ROW BUTTON
        #//////////////////////////////////////////////////////////////////////////

        self.remove_row_button = PushButton('')
        self.remove_row_button.setHidden(True)
        remove_row_icon = QIcon("resources/icons/create_shapefile_icons/minus_icon.svg")
        self.remove_row_button.setIcon(remove_row_icon)

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
        self.buttons_layout.addWidget(self.add_row_button)
        self.buttons_layout.addWidget(self.remove_row_button)

        # Creating a vertical layout for the content
        self.content_layout = QVBoxLayout()
        self.content_layout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.content_layout.addWidget(csv_path_label)
        self.content_layout.addLayout(csv_path_layout)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(shapefile_path_label)
        self.content_layout.addLayout(shapefile_folder_layout)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(shapefile_name_label)
        self.content_layout.addLayout(shapefile_name_layout)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(create_button)
        self.content_layout.addSpacing(70)
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

        csv_path_button.clicked.connect(self.choose_csv)
        shapefile_path_button.clicked.connect(self.choose_folder)
        create_button.clicked.connect(self.convert_to_shapefile)
        self.add_row_button.clicked.connect(self.add_row)
        self.remove_row_button.clicked.connect(self.remove_row)
        self.csv_path_line_edit.textChanged.connect(self.csv_columns_to_shapefile)

    #FUNCTIONS
    #//////////////////////////////////////////////////////////////////////////

    def choose_csv(self):
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

    def csv_columns_to_shapefile(self):
        #delete the previous layout if there is one
        if self.content_layout.count() > 11:
            self.content_layout.removeItem(self.csv_to_shapefile_layout)
            self.content_layout.removeItem(self.buttons_layout)
            while self.csv_to_shapefile_layout.count():
                item = self.csv_to_shapefile_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.csv_to_shapefile_layout.removeItem(item)
            self.csv_to_shapefile_layout.deleteLater()
            self.add_row_button.setHidden(False)
            self.remove_row_button.setHidden(True)

        self.csv = pd.read_csv(self.csv_path_line_edit.text())
        self.csv_columns = self.csv.columns.tolist()

        self.csv_to_shapefile_layout = QFormLayout()

        self.csv_combo_boxes = [CSVComboBox(self.csv_columns, 0), CSVComboBox(self.csv_columns, 1), CSVComboBox(self.csv_columns, 2)]

        self.csv_to_shapefile_layout.addRow(QLabel("Shapefile Column:"), QLabel('CSV Column:'))
        self.csv_to_shapefile_layout.addRow(QLabel('Date'), self.csv_combo_boxes[0])
        self.csv_to_shapefile_layout.addRow(QLabel('Latitude'), self.csv_combo_boxes[1])
        self.csv_to_shapefile_layout.addRow(QLabel('Longitude'), self.csv_combo_boxes[2])

        self.content_layout.insertLayout(3, self.csv_to_shapefile_layout)
        self.content_layout.insertLayout(4, self.buttons_layout)

    def add_row(self):
        self.csv_combo_boxes.append(CSVComboBox(self.csv_columns, len(self.csv_combo_boxes)))
        self.csv_to_shapefile_layout.addRow(QLineEdit(), self.csv_combo_boxes[-1])
        self.csv_combo_boxes[-1].disable_items_after_creation()
        self.remove_row_button.setVisible(True)
        if len(self.csv_columns) == len(self.csv_combo_boxes):
            self.add_row_button.setHidden(True)

    def remove_row(self):
        row_num = self.csv_to_shapefile_layout.rowCount()
        index = self.csv_combo_boxes[-1].currentIndex()
        del self.csv_combo_boxes[-1]
        for combo_box in self.csv_combo_boxes:
            combo_box.enable_item(index)
        self.csv_to_shapefile_layout.removeRow(row_num - 1)
        if row_num <= 5:
            self.remove_row_button.setHidden(True)
        if self.add_row_button.isHidden():
            self.add_row_button.setVisible(True)

    def page_validation(self):
        csv_path = self.csv_path_line_edit.text()
        shapefile_directory = self.shapefile_path_line_edit.text()
        shapefile_name = self.shapefile_name_line_edit.text()
        
        if not csv_path:
            QMessageBox.warning(self, "CSV File Not Specified", "Please specify the CSV file")
            return -1
        if not shapefile_directory:
            QMessageBox.warning(self, "Destination Folder Not Specified", "Please specify the destination folder for the Shapefile")
            return -1
        if not shapefile_name:
            QMessageBox.warning(self, "Field not filled", "Please specify the Shapefile's name")
            return -1

    def convert_to_shapefile(self):
        if self.page_validation() == -1:
            return
        
        config = sh.SHConfig()
        config.sh_client_id= r'9bd0a46d-3d5b-4dc0-98b5-546b3635f9f3'
        config.sh_client_secret = r'~)x%O:RiSc|F5i+SIL}^fZUlWOa.;E^{_:&!J6@:'
        config.save()
        
        shapefile_dir_path = self.shapefile_path_line_edit.text() + '/' + self.shapefile_name_line_edit.text()
        try:
            os.mkdir(shapefile_dir_path)
        except FileExistsError:
            pass
        shapefile_path = shapefile_dir_path + '/' + self.shapefile_name_line_edit.text() + '.shp'

        schema = {
            'geometry':'Point',
            'properties':[('pedlabsampnum','str'),('observation_date','int'),('date','date'),('ca_nh4_ph_7','float'),('mg_nh4_ph_7','float'),('na_nh4_ph_7','float'),('k_nh4_ph_7','float'),('exchangeable_sodium','float'),('cec7_clay_ratio','float'),('cec_nh4_ph_7','float'),('ph_cacl2','float')]
        }
        
        pointShp = fiona.open(shapefile_path, mode='w', driver='ESRI Shapefile', schema = schema, crs = "WGS84")

        for i in range(2, self.line_num + 1):
            
            widget = self.content_layout.itemAt(i+7).widget()
            dict_row_info = {
                'pedlabsampnum': widget.samp_num_line_edit.text(), 
                'observation_date': '', 
                'date': widget.date_edit.date().toPython(), 
                'ca_nh4_ph_7': widget.calcium_line_edit.value(), 
                'mg_nh4_ph_7': widget.magnesium_line_edit.value(), 
                'na_nh4_ph_7': widget.sodium_line_edit.value(), 
                'k_nh4_ph_7': widget.potassium_line_edit.value(), 
                'exchangeable_sodium': widget.exchangeable_sodium_line_edit.value(), 
                'cec7_clay_ratio': widget.clay_ratio_line_edit.value(), 
                'cec_nh4_ph_7': widget.cec_nh4_ph_7_line_edit.value(), 
                'ph_cacl2': widget.cacl_line_edit.value()
            }
            print(dict_row_info)
            row_dict = {
                "geometry": {'type':'Point', 'coordinates': (widget.latitude_line_edit.value() , widget.longitude_line_edit.value())},
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
        for i in range (2, self.line_num):
            self.remove_line()
        self.content_layout.itemAt(9).widget().date_edit.setDate(QDate(2000,1,1))
        self.content_layout.itemAt(9).widget().latitude_line_edit.setValue(0)
        self.content_layout.itemAt(9).widget().longitude_line_edit.setValue(0)
        self.content_layout.itemAt(9).widget().samp_num_line_edit.clear()
        self.content_layout.itemAt(9).widget().calcium_line_edit.setValue(0)
        self.content_layout.itemAt(9).widget().magnesium_line_edit.setValue(0)
        self.content_layout.itemAt(9).widget().sodium_line_edit.setValue(0)
        self.content_layout.itemAt(9).widget().potassium_line_edit.setValue(0)
        self.content_layout.itemAt(9).widget().exchangeable_sodium_line_edit.setValue(0)
        self.content_layout.itemAt(9).widget().clay_ratio_line_edit.setValue(0)
        self.content_layout.itemAt(9).widget().cec_nh4_ph_7_line_edit.setValue(0)
        self.content_layout.itemAt(9).widget().cacl_line_edit.setValue(0)
        self.line_num = 2
