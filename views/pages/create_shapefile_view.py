from qt_core import *
import fiona
import pandas as pd
import sentinelhub as sh
import os
from resources.widgets.push_button import PushButton
from resources.widgets.line_edit import LineEdit

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
        self.csv_path_line_edit = LineEdit()
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
        shapefile_name_label = QLabel("Shapefile name:")

        # Line edit for displaying and editing the name of the shapefile
        self.shapefile_name_line_edit = LineEdit()

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

        # ADD REMAINING ROWS BUTTON
        #//////////////////////////////////////////////////////////////////////////

        self.add_remaining_rows_button = PushButton('Add Remaining Rows')
        add_remaining_rows_icon = QIcon("resources/icons/create_shapefile_icons/add_icon.svg")
        self.add_remaining_rows_button.setIcon(add_remaining_rows_icon)

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
        self.add_remaining_rows_button.clicked.connect(self.add_remaining_rows)
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
        if self.content_layout.count() > 12:
            self.content_layout.removeItem(self.csv_to_shapefile_layout)
            self.content_layout.removeItem(self.buttons_layout)
            self.content_layout.removeWidget(self.add_remaining_rows_button)
            while self.csv_to_shapefile_layout.count():
                item = self.csv_to_shapefile_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.csv_to_shapefile_layout.removeItem(item)
            self.csv_to_shapefile_layout.deleteLater()
            self.remove_row_button.setHidden(True)

        if self.csv_path_line_edit.text() == "":
            self.add_row_button.setHidden(True)
            return
        
        self.add_row_button.setHidden(False)
        self.csv = pd.read_csv(self.csv_path_line_edit.text())
        self.csv_columns = self.csv.columns.tolist()

        self.csv_to_shapefile_layout = QFormLayout()

        self.csv_combo_boxes = [CSVComboBox(self.csv_columns, 0), CSVComboBox(self.csv_columns, 1), CSVComboBox(self.csv_columns, 2)]

        self.csv_to_shapefile_layout.addRow(QLabel("Shapefile Column:"), QLabel('CSV Column:'))
        self.csv_to_shapefile_layout.addRow(QLabel('Date'), self.csv_combo_boxes[0])
        self.csv_to_shapefile_layout.addRow(QLabel('Latitude'), self.csv_combo_boxes[1])
        self.csv_to_shapefile_layout.addRow(QLabel('Longitude'), self.csv_combo_boxes[2])

        self.content_layout.insertLayout(2, self.csv_to_shapefile_layout)
        self.content_layout.insertLayout(3, self.buttons_layout)
        self.content_layout.insertWidget(4, self.add_remaining_rows_button)
        

    def add_row(self):
        self.csv_combo_boxes.append(CSVComboBox(self.csv_columns, len(self.csv_combo_boxes)))
        self.csv_to_shapefile_layout.addRow(LineEdit(), self.csv_combo_boxes[-1])
        self.csv_combo_boxes[-1].disable_items_after_creation()
        self.remove_row_button.setVisible(True)
        if len(self.csv_columns) == len(self.csv_combo_boxes):
            self.add_row_button.setHidden(True)
            self.add_remaining_rows_button.setHidden(True)

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
        self.add_remaining_rows_button.setVisible(True)

    def add_remaining_rows(self):
        for i in range(len(self.csv_columns) - 3):
            if self.add_row_button.isHidden():
                break
            self.add_row()
        self.add_remaining_rows_button.setHidden(True)

    def page_validation(self):
        csv_path = self.csv_path_line_edit.text()
        shapefile_directory = self.shapefile_path_line_edit.text()
        shapefile_name = self.shapefile_name_line_edit.text()
        
        if not csv_path:
            QMessageBox.warning(self, "CSV File Not Specified", "Please specify the CSV file")
            return -1
        for i in range(1, self.csv_to_shapefile_layout.rowCount()):
            if i > 3:
                shapefile_column = self.csv_to_shapefile_layout.itemAt(i, QFormLayout.LabelRole).widget().text()
                if shapefile_column == "":
                    QMessageBox.warning(self, f"Field not filled", f"Please specify the Shapefile's column in row {i}")
                    return -1
            csv_column = self.csv_to_shapefile_layout.itemAt(i, QFormLayout.FieldRole).widget().currentIndex()
            if csv_column == -1:
                QMessageBox.warning(self, f"Field not filled", f"Please specify the CSV's column in row {i}")
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

        schema_props = []
        shapefile_columns = []
        csv_columns = []
        csv_layout = self.csv_to_shapefile_layout

        # Get the data types of the CSV columns
        self.csv = self.csv.convert_dtypes()
        data_types = self.csv.dtypes.astype(str).tolist()
        for i in range (len(data_types)):
            if data_types[i] == 'string':
                data_types[i] = 'str'
            elif data_types[i] == 'Int64':
                data_types[i] = 'int'
            elif data_types[i] == 'Float64':
                data_types[i] = 'float'
            elif data_types[i] == 'Datetime64[ns]':
                data_types[i] = 'date'
            else:
                data_types[i] = 'str'

        for i in range(1, csv_layout.rowCount()):
            shapefile_column = csv_layout.itemAt(i, QFormLayout.LabelRole).widget().text()
            shapefile_columns.append(shapefile_column)
            csv_column = csv_layout.itemAt(i, QFormLayout.FieldRole).widget().currentText()
            csv_columns.append(csv_column)

        for i in range(csv_layout.rowCount() - 1):
            # Check if the latitude and longitude columns are completely filled with real numbers
            if i == 1 or i == 2:
                if data_types[self.csv_columns.index(csv_columns[i])] != 'float':
                    QMessageBox.warning(self, "Invalid Data Type", "Latitude and Longitude must be real numbers")
                    return
                for bool in pd.isna(self.csv[csv_columns[i]]):
                    if bool:
                        QMessageBox.warning(self, "Invalid Data Type", "Latitude and Longitude must be real numbers")
                        return
            else:
                schema_props.append((shapefile_columns[i], data_types[self.csv_columns.index(csv_columns[i])]))

        schema = {
            'geometry':'Point',
            'properties':schema_props
        }
        
        pointShp = fiona.open(shapefile_path, mode='w', driver='ESRI Shapefile', schema = schema, crs = "WGS84")

        # Select relevant columns from the CSV file
        self.csv = self.csv[csv_columns]
        dict_rename_colums= {}
        for i in range(len(csv_columns)):
            dict_rename_colums[csv_columns[i]] = shapefile_columns[i]

        # Rename the columns to match the shapefile columns inputed by the user
        self.csv.rename(columns = dict_rename_colums, inplace=True)

        for index, row in self.csv.iterrows():
            dict_row_info = row.to_dict()
            del dict_row_info[shapefile_columns[1]]
            del dict_row_info[shapefile_columns[2]]

            row_dict = {
                "geometry": {'type':'Point', 'coordinates': (row[shapefile_columns[1]], row[shapefile_columns[2]])},
                "properties": dict_row_info
            }
            pointShp.write(row_dict)
        pointShp.close()
        QMessageBox.information(self, "Success", "Shapefile created successfully")
        self.clear_page()

    def clear_page(self):
        # Clear CSV file path field
        self.csv_path_line_edit.clear()
        # Clear shapefile destination field
        self.shapefile_path_line_edit.clear()
        # Clear shapefile name field
        self.shapefile_name_line_edit.clear()
