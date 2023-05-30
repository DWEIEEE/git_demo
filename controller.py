from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog

import time
import os
import multiprocessing 
import threading

from video_controller import video_controller
from video_controller_2 import video_controller_2
from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        
    def setup_control(self):
        self.ui.button_openfile.clicked.connect(self.open_file)
        self.ui.button_openfile_2.clicked.connect(self.open_file_2)

    
    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Open file Window", "./", "Video Files(*.mp4 *.avi)")       
        self.video_path = filename
        basename = os.path.basename(filename)
        self.ui.label.setText(basename)
        self.video_controller = video_controller(video_path=self.video_path,ui=self.ui)
        self.ui.label_filepath.setText(f"video path: {self.video_path}")
        self.ui.button_play.clicked.connect(self.video_controller.play) # connect to function()
        self.ui.button_stop.clicked.connect(self.video_controller.stop)
        self.ui.button_pause.clicked.connect(self.video_controller.pause)
        
    def open_file_2(self):
        filename_2, filetype_2 = QFileDialog.getOpenFileName(self, "Open file Window", "./", "Video Files(*.mp4 *.avi)")   
        self.video_path_2 = filename_2
        basename_2 = os.path.basename(filename_2)
        self.ui.label_2.setText(basename_2)
        self.video_controller_2 = video_controller_2(video_path=self.video_path_2,ui=self.ui)
        self.ui.label_filepath_2.setText(f"video path: {self.video_path_2}")
        self.ui.button_play.clicked.connect(self.video_controller_2.play) # connect to function()
        self.ui.button_stop.clicked.connect(self.video_controller_2.stop)
        self.ui.button_pause.clicked.connect(self.video_controller_2.pause)