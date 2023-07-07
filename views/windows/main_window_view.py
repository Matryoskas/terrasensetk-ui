from qt_core import *
from views.pages.data_view import DataView
from views.pages.algorithms_view import AlgorithmsView
from views.pages.performance_evaluation_view import PerformanceEvaluationView
from resources.widgets.side_bar_button import SideBarButton

class MainWindowView(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # Set initial Parameters
        parent.resize(1000, 900)
        parent.setMinimumSize(900, 800)

        # Creating the main frame to hold the side_bar and pages
        self.main_frame = QFrame()
        self.main_layout = QHBoxLayout(self.main_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        # Creating the buttons in the sidebar
        self.data_button = SideBarButton("Data", "resources/icons/main_window_icons/Data_icon.png")
        self.algorithms_button = SideBarButton("Algorithms","resources/icons/main_window_icons/Algorithms_icon.png")
        self.Performance_evaluation_button = SideBarButton("Performance", "resources/icons/main_window_icons/Performance_evaluation_icon.png")
  
    
        # SIDE BAR
        self.side_bar = QFrame()
        self.side_bar.setStyleSheet("background-color: #DDDDDD;") 
        self.side_bar_layout = QVBoxLayout(self.side_bar)
        self.side_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.side_bar_layout.setSpacing(0)
        self.side_bar_layout.setAlignment(Qt.AlignTop)
        self.side_bar_layout.addWidget(self.data_button)
        self.side_bar_layout.addWidget(self.algorithms_button)
        self.side_bar_layout.addWidget(self.Performance_evaluation_button)

        # CONTENT #
        self.content = QFrame()
        # Content Layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # CONTENT -> PAGES 
        self.pages = QStackedWidget()
        self.data_view = DataView()
        self.algorithms_view = AlgorithmsView()
        self.performance_evaluation_view = PerformanceEvaluationView()
        
        # Adding the views to the pages
        self.pages.addWidget(self.data_view)
        self.pages.addWidget(self.algorithms_view)
        self.pages.addWidget(self.performance_evaluation_view)
        
        # CONTENT -> BOTTOM BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #CCCCCC")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar) 
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)

        # Create Left Label
        self.bottom_label_left = QLabel("")
        # Create Bottom Spacer
        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Create Right Label
        self.bottom_label_right = QLabel("©2023")
        # Add to Bottom Bar Layout
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)

        # Add to CONTENT LAYOUT
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # Adding the side_bar and pages to the main layout
        self.main_layout.addWidget(self.side_bar)
        self.main_layout.addWidget(self.content)

        # Setting the main frame as the central widget
        parent.setCentralWidget(self.main_frame)

    
