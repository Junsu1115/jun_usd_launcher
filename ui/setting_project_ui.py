from PySide6 import QtCore, QtGui, QtWidgets

class SettingProjectUi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("setting project")
        self.resize(700, 200)
        layout = QtWidgets.QVBoxLayout()
        projectname_lineedit = self.create_projectname_lineedit()
        root_path_lineedit = self.create_root_path_lineedit()
        layout.addLayout(projectname_lineedit)
        layout.addLayout(root_path_lineedit)
        self.setLayout(layout)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        return projectname_lineedit

    def create_projectname_lineedit(self):
        layout = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Project name")
        lineedit = QtWidgets.QLineEdit(self)
        lineedit.setFixedSize(500, 30)
        layout.addStretch()
        layout.addWidget(label)
        layout.addWidget(lineedit)
        layout.addStretch()
        return layout

    def create_root_path_lineedit(self):
        layout = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Root path")
        lineedit = QtWidgets.QLineEdit()
        lineedit.setText("/Users/junsu/Desktop")
        lineedit.setFixedSize(500, 30)
        push_button = (QtWidgets.QPushButton())
        push_button.setText("search file")
        push_button.setFixedSize(100, 30)

        push_button.clicked.connect(self.search_file)

        layout.addStretch()
        layout.addWidget(label)
        layout.addWidget(lineedit)
        layout.addWidget(push_button)

        return layout

    def search_file(self):
        sercher = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "파일을 선택해주세요",
            "/Users/junsu/Desktop",
        )

        return sercher[0]

# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     widget = SettingProjectUi()
#     widget.show()
#     app.exec_()