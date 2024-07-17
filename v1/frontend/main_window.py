from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                             QScrollArea, QLineEdit, QComboBox, QPushButton,
                             QFileDialog)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSignal, Qt
import parameters as p
import os
import pandas as pd
# from frontend.ventana_juego import VentanaJuego
# from frontend.ventana_emergente import VentanaEmergente


class MainWindow(QWidget):
    # senal_verificar_nombre = pyqtSignal(str)
    # senal_crear_puzzle = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        # self.ventana_juego = VentanaJuego()
        self.file_path = ''
        self.init_gui()
        self.show()

    def init_gui(self) -> None:
        # Window:
        self.setGeometry(100, 100, p.WINDOW_WIDTH, p.WINDOW_HEIGHT)
        self.setWindowTitle('Data Visualizer')
        # self.setStyleSheet(f'background: {p.MAIN_BACKGROUND_COLOR};')

        # Select CSV file:
        self.label_select_file = QLabel('Select CSV file:', self)
        self.label_current_file = QLabel(self.file_path, self)
        self.button_select_file = QPushButton('Browse', self)
        self.button_select_file.clicked.connect(self.select_file)
        ## HBox:
        self.hbox_select_file = QHBoxLayout()
        self.hbox_select_file.addWidget(self.label_select_file)
        self.hbox_select_file.addWidget(self.label_current_file)
        self.hbox_select_file.addWidget(self.button_select_file)

        # Select horizontal axis' column name:
        self.label_horizontal_axis = QLabel('Horizontal axis:', self)
        self.combo_box_horizontal_axis = QComboBox(self)
        ## HBox:
        self.hbox_horizontal_axis = QHBoxLayout()
        self.hbox_horizontal_axis.addWidget(self.label_horizontal_axis)
        self.hbox_horizontal_axis.addWidget(self.combo_box_horizontal_axis)

        # Select vertical axis' column name:
        self.label_vertical_axis = QLabel('Vertical axis:', self)
        self.combo_box_vertical_axis = QComboBox(self)
        ## HBox:
        self.hbox_vertical_axis = QHBoxLayout()
        self.hbox_vertical_axis.addWidget(self.label_vertical_axis)
        self.hbox_vertical_axis.addWidget(self.combo_box_vertical_axis)

        # Show graph:
        self.button_show_graph = QPushButton('Show', self)

        #
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox_select_file)
        self.vbox.addLayout(self.hbox_horizontal_axis)
        self.vbox.addLayout(self.hbox_vertical_axis)
        self.vbox.addWidget(self.button_show_graph)

        self.setLayout(self.vbox)

    def select_file(self) -> None:
        """
        Save the CSV file path as an instance variable.
        """
        label = 'Open file'
        script_path = os.getcwd() # Path where the script is running
        filter_ = 'CSV Files (*.csv)'
        file = QFileDialog.getOpenFileName(self, label, script_path, filter_)
        self.file_path = file[0] # Save file path
        self.label_current_file.setText(self.file_path) # Update label
        self.open_file()
        self.update_columns_names()

    def open_file(self) -> None:
        """
        Save the columns' names of the chosen CSV file:
        """
        dataframe = pd.read_csv(self.file_path)
        self.columns = dataframe.columns.values.tolist()

    def update_columns_names(self) -> None:
        """
        Add the columns' names of the chosen CSV file to the drop-down menus of
        the horizontal and vertical axes.
        """
        # Clear drop-down menus:
        self.combo_box_horizontal_axis.clear()
        self.combo_box_vertical_axis.clear()
        # Add columns to the drop-down menus:
        for column in self.columns:
            self.combo_box_horizontal_axis.addItem(column)
            self.combo_box_vertical_axis.addItem(column)

    def open_graph(self) -> None:
        pass

    def abrir_ventana_juego(self) -> None:
        pass
        # nombre_usuario = self.line_edit.text()
        # self.verificar_nombre(nombre_usuario)
        # if self.nombre_valido == True:
        #     archivo_puzzle = self.combo_box.currentText()
        #     self.senal_crear_puzzle.emit(archivo_puzzle)
        #     t, f, c, n = self.tamano_puzzle, self.filas, self.columnas, nombre_usuario
        #     self.ventana_juego.mostrar_ventana(t, f, c, n)
        #     self.ventana_juego.senal_cerrar_programa.connect(self.salir)
        #     self.ventana_juego.senal_actualizar_salon_fama.connect(self.salon_de_la_fama)
        #     self.line_edit.clear()
        # else:
        #     texto_1 = 'Nombre inválido: debe ser alfanumérico y contener, al menos, una'
        #     texto_2 = ' letra mayúscula y un número.'
        #     self.popup = VentanaEmergente(texto_1 + texto_2)