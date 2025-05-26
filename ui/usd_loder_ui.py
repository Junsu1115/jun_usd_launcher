from PySide6 import QtCore, QtGui, QtWidgets

class UsdLoderUi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Jun's USD Loader")
        self.resize(1200, 600)

        tab_widget = self.create_tabwidget()
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)

    def create_tabwidget(self):
        tab_widget = QtWidgets.QTabWidget()
        tab_widget.addTab(self.create_asset_tab(), "Assets")
        tab_widget.addTab(self.create_shot_tab(), "Shots")
        return tab_widget

    def set_layout(self):
        layout = QtWidgets.QHBoxLayout()
        low_layout = QtWidgets.QHBoxLayout()
        mid_layout = QtWidgets.QVBoxLayout()
        file_layout = QtWidgets.QVBoxLayout()

        low_layout.addLayout(self.create_dept_table())
        low_layout.addLayout(self.create_version_table())

        file_layout.addLayout(self.create_files_table())
        mid_layout.addLayout(low_layout)
        mid_layout.addLayout(self.create_table_info())
        mid_layout.addStretch()

        layout.addLayout(mid_layout)
        layout.addLayout(file_layout)
        return layout

    def create_asset_tab(self):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(QtWidgets.QTableWidget())
        layout.addLayout(self.set_layout())
        widget.setLayout(layout)
        return widget

    def create_shot_tab(self):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(QtWidgets.QTableWidget())
        layout.addLayout(self.set_layout())
        widget.setLayout(layout)
        return widget

    def create_dept_table(self):
        layout = QtWidgets.QVBoxLayout()
        dept_label = QtWidgets.QLabel()
        dept_label.setText("Department")
        dept_table_widget = QtWidgets.QTableWidget()
        dept_table_widget.setFixedSize(150, 200)
        layout.addWidget(dept_label)
        layout.addWidget(dept_table_widget)
        layout.addStretch()
        return layout

    def create_version_table(self):
        layout = QtWidgets.QVBoxLayout()
        version_label = QtWidgets.QLabel()
        version_label.setText("Version")
        version_table_widget = QtWidgets.QTableWidget()
        version_table_widget.setFixedSize(150, 200)
        layout.addWidget(version_label)
        layout.addWidget(version_table_widget)
        layout.addStretch()
        return layout

    def create_table_info(self):
        layout = QtWidgets.QVBoxLayout()
        name_layout = QtWidgets.QHBoxLayout()

        info_label = QtWidgets.QLabel()
        info_label.setText("Info")

        name_label = QtWidgets.QLabel()
        name_label.setText("Name")

        name_describe_label = QtWidgets.QLabel()
        name_describe_label.setText("hi")

        name_layout.addWidget(name_label)
        name_layout.addWidget(name_describe_label)

        layout.addWidget(info_label)
        layout.addLayout(name_layout)
        layout.addStretch()
        return layout

    def create_files_table(self):
        layout = QtWidgets.QVBoxLayout()
        files_label = QtWidgets.QLabel()
        files_label.setText("Files")
        files_table_widget = QtWidgets.QTableWidget()
        files_table_widget.setFixedSize(600, 600)
        layout.addWidget(files_label)
        layout.addWidget(files_table_widget)
        layout.addStretch()
        return layout

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = UsdLoderUi()
    widget.show()
    app.exec_()