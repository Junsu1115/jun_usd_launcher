from usd_loder_ui import *

class JunLauncherUi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Jun Launcher")
        self.resize(300, 600)
        button_layout = self.create_button_layout()
        self.setLayout(button_layout)
        button_layout.setAlignment(QtCore.Qt.AlignCenter)

    def create_button_layout(self):
        Loader_button = self.create_Loader_button()
        Publisher_button = self.create_Publisher_button()
        setting_project_button = self.create_setting_project_button()

        Loader_button.clicked.connect(self.open_usd_loader)
        setting_project_button.clicked.connect(self.open_setting_project_ui)

        button_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(Loader_button)
        button_layout.addWidget(Publisher_button)
        button_layout.addWidget(setting_project_button)
        return button_layout

    def create_Loader_button(self):
        Loader_button = QtWidgets.QPushButton('Loader', self)
        Loader_button.setFixedSize(200, 30)
        return Loader_button

    def create_Publisher_button(self):
        Publisher_button = QtWidgets.QPushButton('Publisher', self)
        Publisher_button.setFixedSize(200, 30)
        return Publisher_button

    def create_setting_project_button(self):
        setting_project_button = QtWidgets.QPushButton('Setting Project', self)
        setting_project_button.setFixedSize(200, 30)
        return setting_project_button

    def open_usd_loader(self):
        self.usd_loader_window = UsdLoderUi()
        self.usd_loader_window.show()

    def open_setting_project_ui(self):
        self.setting_project_window = SettingProjectUi()
        self.setting_project_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = JunLauncherUi()
    widget.show()
    app.exec_()