from qt_core import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from resources.widgets.push_button import PushButton
from resources.widgets.combo_box import ComboBox


class PlotDataView(QWidget):
    def __init__(self):
        super().__init__()
        self.dataframe = None
        
        # X AXIS
        #//////////////////////////////////////////////////////////////////////////
        self.x_axis_label = QLabel("X Axis")
        self.x_axis_label.setHidden(True)

        self.x_axis_combo_box = ComboBox()
        self.x_axis_combo_box.setHidden(True)

        # Y AXIS
        #//////////////////////////////////////////////////////////////////////////
        self.y_axis_label = QLabel("Y Axis")
        self.y_axis_label.setHidden(True)

        self.y_axis_combo_box = ComboBox()
        self.y_axis_combo_box.setHidden(True)

        # PLOT EVERYTHING BUTTON
        #//////////////////////////////////////////////////////////////////////////

        self.plot_everything_button = PushButton("Plot everything")
        self.plot_everything_button.setHidden(True)

        # MAIN LAYOUT
        #//////////////////////////////////////////////////////////////////////////
        main_layout = QHBoxLayout()
        # Frame to occupy space on the left
        left_empty_frame = QFrame()
        left_empty_frame.setFixedWidth(40)
        left_empty_frame.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # Adding the empty frame to the left side of the horizontal layout
        main_layout.addWidget(left_empty_frame)

        # Creating a vertical layout for the canvas
        self.canvas_layout = QVBoxLayout()
        # Creating a vertical layout for the content
        self.content_layout = QVBoxLayout()
        self.content_layout.addWidget(self.x_axis_label)
        self.content_layout.addWidget(self.x_axis_combo_box)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.y_axis_label)
        self.content_layout.addWidget(self.y_axis_combo_box)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.plot_everything_button)
        self.content_layout.addSpacing(10)
        self.content_layout.addLayout(self.canvas_layout)
        
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

        # Connect the combo box to the function
        self.x_axis_combo_box.currentIndexChanged.connect(self.plot_data)
        self.y_axis_combo_box.currentIndexChanged.connect(self.plot_data)
        self.plot_everything_button.clicked.connect(self.plot_everything)

    def plot_data(self):

        if self.dataframe is None:
            print("Dataframe is None")
            return
        if self.x_axis_combo_box.currentIndex() == -1:
            print("x_axis_combo_box is None")
            return
        if self.y_axis_combo_box.currentIndex() == -1:
            print("y_axis_combo_box is None")
            return
        
        self.clear_plot()
        fig, self.axes = plt.subplots(figsize=(10, 8))
        self.canvas = FigureCanvas(fig)

        self.canvas_layout.addWidget(self.canvas)

        x_axis = self.dataframe[self.x_axis_combo_box.currentText()]
        y_axis = self.dataframe[self.y_axis_combo_box.currentText()]

        self.axes.plot(x_axis, y_axis, 'o')
        self.axes.set_xlabel(self.x_axis_combo_box.currentText())
        self.axes.set_ylabel(self.y_axis_combo_box.currentText())

    def clear_plot(self):
        # Clear the existing plot by removing the canvas from the layout
        
        while self.canvas_layout.count():
            child = self.canvas_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        plt.close('all')

    def plot_everything(self):
        ncol = self.dataframe.shape[1]
        fig, axes = plt.subplots(nrows=ncol, ncols=ncol, figsize=(20, 16))
        canvas = FigureCanvas(fig)
        for i in range(ncol):
            for j in range(ncol):
                axes[i, j].plot(self.dataframe.iloc[:, j], self.dataframe.iloc[:, i], 'o')
                if i == 0:
                    axes[i, j].set_title(self.dataframe.columns[j], fontsize=8)
                if j == 0:
                    axes[i, j].set_ylabel(self.dataframe.columns[i], fontsize=8)
        canvas.show()

    def allow_input(self, dataframe=None):
        self.x_axis_label.setHidden(False)
        self.x_axis_combo_box.setHidden(False)
        self.y_axis_label.setHidden(False)
        self.y_axis_combo_box.setHidden(False)
        self.plot_everything_button.setHidden(False)

        self.dataframe = dataframe
        self.first_time = True
        # Select only the numeric columns
        self.dataframe = self.dataframe.select_dtypes(include=[np.number])
        dataframe_columns = self.dataframe.columns.tolist()
        self.x_axis_combo_box.addItems(dataframe_columns)
        self.y_axis_combo_box.addItems(dataframe_columns)
