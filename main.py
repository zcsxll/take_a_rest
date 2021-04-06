import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets

import zcs_tray

class WidgetMain(QtWidgets.QWidget):
    def __init__(self):
        super(WidgetMain, self).__init__()
        self.setWindowFlags(QtCore.Qt.Tool)

        self.resize(350, 250)

        self.tray = zcs_tray.ZcsTray(self)
        self.tray.show()

    def closeEvent(self, event):
        # print(event)
        event.ignore()
        self.tray.show()
        self.hide()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = WidgetMain()
    widget.show()
    sys.exit(app.exec_())
